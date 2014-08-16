# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## Kvasir API Class
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

__author__ = "Kurt Grutzmacher <kgrutzma@cisco.com>"
__date__ = "16 August 2014"
__version__ = "1.0.0"

from config import Configuration


##-------------------------------------------------------------------------
class Calls(dict):
    """A class of call routines to reach Kvasir through the API"""
    def __init__(self, *args, **kwargs):
        super(Calls, self).__init__(*args, **kwargs)
        self.__dict__ = self


##-------------------------------------------------------------------------
class API():
    """An API to communicate with Kvasir.

    Kvasir is a Penetration Testing Data Management system (https://github.com/KvasirSecurity/Kvasir).
    This API allows third-party tools to communicate with Kvasir through a JSONRPC library.

    To use:

    ```
    import KvasirAPI
    kvasir = KvasirAPI.API('config.yaml')
    ```

    Multiple Kvasir instances can be defined in the configuration file. A sample configuration:

    ```
    customer:
      id: 11-ACME-01
      full-name: ACME Widgets, Inc.
      short-name: ACME
      possessive: ACME Widget, Inc's
      short-capital: ACME
      possessive-capital: ACME's

    instances:
      internal:
      url: "http://username:password@localhost:8000/internal/"
      name: Internal Network
      test_type: internal
      start: May 2, 2011
      end: May 6, 2011
      filter_type: assetgroup
      filter_value: organization

    external:
      url: "http://username:password@localhost:8000/external/"
      test_type: external
      start: May 2, 2011
      end: May 6, 2011
      name: External Network

    web2py: build/web2py
    ```
    """
    def __init__(self, configuration=None):
        """
        Kvasir API initialization

        :param configuration: YAML configuration in a string or filename
        :return: instance
        """
        self.api_version = __version__
        self._representation = "Kvasir v%s" % __version__
        self.api_calls = None
        self.configuration = Configuration(configuration)
        self.call = Calls()
        if self.configuration.valid:
            self.load_calls(self.configuration.api_type)

    def __repr__(self):
        return self._representation

    @property
    def version(self):
        return self.api_version

    def load_calls(self, call_type='jsonrpc'):
        """Loads the KvasirAPI calls into API.call based on the call_type variable. Utilizes the `Calls` class to
        establish an attribute-based access method. For instance a configuration with an instance called 'internal'
        will create an API.call that can be used like this:

            API.call.internal.hosts.list()  # return all hosts from Kvasir instance 'internal'

        :param call_type: string of 'jsonrpc' or 'restapi'
        :return: self.call dictionary
        """
        valid = False
        if call_type == 'jsonrpc':
            #from jsonrpc import Hosts, Services, Accounts, Vulns, OS, NetBIOS, Evidence
            import jsonrpc as api_calls
            self.api_calls = api_calls
            valid = True
        #if call_type == 'rest'
            # TODO: Implement restful API functions
            #from restapi import hosts, services, accounts, vulns, os, netbios, evidence

        if valid:
            # if kvasir configuration is valid, go through the instances and build the self.call dict
            for instance, values in self.configuration.instances_dict.items():
                self.call[instance] = Calls()
                self.call[instance].call_type = call_type
                self.call[instance].hosts = self.api_calls.Hosts(values, self.configuration.web2py_dir)
                self.call[instance].services = self.api_calls.Services(values, self.configuration.web2py_dir)
                self.call[instance].accounts = self.api_calls.Accounts(values, self.configuration.web2py_dir)
                self.call[instance].vulns = self.api_calls.Vulns(values, self.configuration.web2py_dir)
                self.call[instance].os = self.api_calls.OpSys(values, self.configuration.web2py_dir)
                self.call[instance].snmp = self.api_calls.SNMP(values, self.configuration.web2py_dir)
                self.call[instance].netbios = self.api_calls.NetBIOS(values, self.configuration.web2py_dir)
                self.call[instance].evidence = self.api_calls.Evidence(values, self.configuration.web2py_dir)
                self.call[instance].stats = self.api_calls.Stats(values, self.configuration.web2py_dir)
