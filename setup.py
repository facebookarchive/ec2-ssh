"""
EC2-SSH
=======

A simple command line utility, allowing you to SSH into you Amazon EC2 instances
by their "Name" tag.

A few examples:

::

    % ec2-ssh nginx2
    # equivalent to
    # ssh ubuntu@ec2-123-45-67-89.compute-1.amazonaws.com

    % ec2-ssh root@appserver
    % ec2-ssh deploy@nginx2 sudo restart nginx

    # accompanying ec2-host script

    # w/o arg: prints all active instances
    % ec2-host
    django1 ec2-123-45-67-89.compute-1.amazonaws.com
    django2 ec2-132-45-67-89.compute-1.amazonaws.com
    django3 ec2-231-45-67-89.compute-1.amazonaws.com

    # w/ arg: prints host name of matching instance
    % ec2-host django2
    django2 ec2-132-45-67-89.compute-1.amazonaws.com


Links
`````

* `Website <http://github.com/Instagram/ec2-ssh>`_
* `Instagram <http://instagram.com>`_

Changelog
`````````

* 1.0 - initial release
* 1.1 - override prompt (PS1) to show tag name
* 1.1.1 - Add line echoing host before establishing SSH connection
* 1.2 - Merged pull requests to add region and tag support

"""


import os
from setuptools import setup


setup(
    name = "ec2-ssh",
    version = "1.2",
    author = "Shayne Sweeney",
    author_email = "shayne@instagram.com",
    description = "SSH into EC2 instances via tag name",
    long_description = __doc__,
    license = "MIT",
    url = "https://github.com/Instagram/ec2-ssh",
    keywords = ["amazon", "aws", "ec2", "ami", "ssh", "cloud", "boto"],
    install_requires = ['boto>=1.0'],
    scripts = ["bin/ec2-host", "bin/ec2-ssh"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities"
        ],
)
