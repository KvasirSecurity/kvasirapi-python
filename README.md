kvasirapi-python
================

Python API to communicate with [Kvasir](https://github.com/KvasirSecurity/Kvasir).

At this time only the JSONRPC API is supported. RESTful API is in progress.


Features
--------

* Allows for third-party tools to communicate with multiple Kvasir instances
* Builds content which can be used for reporting
* Extend python scripts to access or update Kvasir data 


Installation
------------

    $ pip install KvasirAPI


Usage
-----

1. Create a YAML configuration file

```YAML
customer:
  id: 11-ACME-01
  full-name: ACME Widgets, Inc.
  short-name: ACME
  possessive: ACME Widget, Inc's
  short-capital: ACME
  possessive-capital: ACME's

instances:
  test:
    url: "http://test:test@localhost:8000/kvasir/"
    name: Test Network
    test_type: internal
    start: May 2, 2011
    end: May 6, 2011
```

2. Load the API module:

```
$ python
>>> import KvasirAPI
>>> kvasir = KvasirAPI.API('config.yml')
```

3. Access the API routines:

```
>>> kvasir.configuration.customer_info()
{'short-name': 'ACME', 'possessive': "ACME Widget, Inc's", 'full-name': 'ACME Widgets, Inc.', 'short-capital': 'ACME', 'id': '11-ACME-01', 'possessive-capital': "ACME's"}  
>>> kvasir.configuration.instances()
{'test': {'end': 'May 6, 2011', 'name': 'Test Network', 'url': 'http://test:test@localhost:8000/kvasir/', 'test_type': 'internal', 'hostfilter': {}, 'start': 'May 2, 2011'}}
```

Contributing
------------

1. Fork the [repository](https://github.com/KvasirSecurity/kvasirapi-python) on Github
2. Make a branch off of master and commit your changes to it.
3. Ensure that your name is added to the end of the AUTHORS file using the
   format ``Name <email@domain.com> (url)``, where the ``(url)`` portion is
   optional.
4. Submit a Pull Request to the master branch on GitHub.

