#!/usr/bin/env python
# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

__author__ = "Kurt Grutzmacher <kgrutzma@cisco.com>"
__date__ = "3 August 2014"
__version__ = "1.0.0"

import logging
from utils import *

try:
    import yaml
    from yaml.parser import ParserError
except ImportError:
    raise ImportError('PyYAML required. Please install it before continuing')


##-------------------------------------------------------------------------
class Configuration():
    """Loads configuration values from configuration files"""

    def __init__(self, configuration=None):
        self.config = {}
        self.web2py_dir = None
        self.customer = {}
        self.instances_dict = {}
        self.log = logging.getLogger(str(self.__class__))
        self.version = __version__
        self.api_type = None
        self.valid = False
        if configuration:
            self.load(configuration)

    def __getitem__(self, item):
        try:
            return self.instances_dict[item]
        except ValueError:
            return {}

    def keys(self):
        return self.instances_dict.keys()

    def load(self, configuration):
        """
        Load a YAML configuration file.

        :param configuration: Configuration filename or YAML string
        """
        try:
            self.config = yaml.load(open(configuration, "rb"))
        except IOError:
            try:
                self.config = yaml.load(configuration)
            except ParserError, e:
                raise ParserError('Error parsing config: %s' % e)

        # put customer data into self.customer
        if isinstance(self.config, dict):
            self.customer = self.config.get('customer', {})
            self.instances_dict = self.config.get('instances', {})
            self.web2py_dir = self.config.get('web2py', None)
            self.api_type = self.config.get('api_type', 'jsonrpc')
            self.valid = True
        else:
            self.customer = {}
            self.instances_dict = {}
            self.web2py_dir = None
            self.valid = False

    def instances(self, test_type=".*"):
        """
        Returns a dict of all instances defined using a regex

        :param test_type: Regular expression to match for self.instance['test_type'] value names
        """
        import re
        data = {}
        for k, v in self.instances_dict.iteritems():
            if re.match(test_type, v.get('test_type'), re.IGNORECASE):
                if 'filter_type' in v:
                    hostfilter = {
                        'filtertype': v['filter_type'],
                        'content': v['filter_value']
                    }
                else:
                    hostfilter = {}
                data[k] = {
                    'name': v.get('name'),
                    'start': v.get('start'),
                    'end': v.get('end'),
                    'url': v.get('url'),
                    'hostfilter': hostfilter,
                    'test_type': v.get('test_type')
                }
        return data

    def instance_uri(self, instance="internal"):
        """
        Returns the URI for a Kvasir instance

        :param instance: An instance name (exact)
        :return: The URL as parsed through make_good_url
        """
        return make_good_url(self.instances_dict.get(instance, '{}').get('url'), )

    def customer_info(self):
        """
        Returns the customer information
        """
        return self.customer

