import requests
import json

"""
Functions to manage Outline keys
Full documentation here: 
https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/shadowbox/server/api.yml

"""


def create_new_access_key(api_url):
    """
    Creates an access key at the specified server
    Does this command: curl --insecure -X POST $API_URL/access-keys
    Documentation for Outline API here: https://github.com/Jigsaw-Code/outline-server/tree/master/src/shadowbox

    Args:
        api_url (string): Outline server apiUrl

    Returns:
        (accessUrl, access_key_id) (string, string): Tuple with the accessUrl and access_key_id

    """
    post_request = api_url + '/access-keys'
    r = requests.post(post_request, verify=False)
    r = r.json()
    print('Created new access key: {}'.format(r))

    return (r.get('accessUrl'), r.get('id'))


def rename_access_key(name, access_key_id, api_url):
    """
    Renames the access key in Outline Manager

    Args:
        name (string): Name of user
        access_key_id (string): access key id
        api_url: Outline server apiUrl

    Returns:
        None
    """

    url = api_url + '/access-keys/' + access_key_id + '/name'
    data = {
        'name': name
    }
    requests.put(url=url, data=data, verify=False)


def add_limit(server_api_url, bytes, outline_access_key_id):
    """
    Adds a data limit on the access key

    Args:
        server_api_url (string): Outline server apiUrl
        bytes (int): How many bytes to limit to
        outline_access_key_id (int): access key Outline id

    Returns:
        response (response): Response from the request
    """
    headers = {'Content-Type': "application/json"}
    payload = {'limit': {'bytes': bytes}}
    response = requests.put(
        server_api_url+'/access-keys/'+str(outline_access_key_id)+'/data-limit', headers=headers, data=json.dumps(payload), verify=False)

    return response


def remove_limit(server_api_url, outline_access_key_id):
    """
    Removes data limit on the access key

    Args:
        server_api_url (string): Outline server apiUrl
        outline_access_key_id (int): access key Outline id

    Returns:
        response (response): Response from the request
    """
    headers = {'Content-Type': "application/json"}
    response = requests.delete(
        server_api_url+'/access-keys/'+str(outline_access_key_id)+'/data-limit', headers=headers, verify=False)

    return response


def list_access_keys(server_api_url):
    """
    Lists access keys for server

    Args:
        server_api_url (string): Outline server apiUrl

    Returns:
        access_keys ([dict]): List of all access keys in dictionary format
    """
    headers = {'Content-Type': "application/json"}
    response = requests.get(server_api_url + '/access-keys',
                            headers=headers, verify=False)
    return response.json()['accessKeys']
