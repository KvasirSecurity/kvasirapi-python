# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## Configuration pytest fixtures
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#


import pytest
import KvasirAPI


@pytest.fixture(scope="module")
def configure_string():
    """KvasirAPI configuration using a string"""
    test_config = '''customer:
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
    start: May 2, 2011
    end: May 6, 2011
    name: External Network
    test_type: external

web2py: /opt/web2py/
api_type: jsonrpc
'''
    return KvasirAPI.API(test_config)


@pytest.fixture(scope="module")
def configure_file():
    """KvasirAPI configuration from a yaml file"""
    return KvasirAPI.API("test/test.yaml")
