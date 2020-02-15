import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outline-manager",
    version="0.0.3",
    author="Ching Jui Young",
    author_email="young.chingjui@youngandai.com",
    description="Manages access keys for servers with Outline server installed.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/youngchingjui/pyoutline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    setup_requires=['wheel'],
    install_requires=[
        'requests'
    ]
)
