#!/usr/bin/env python
# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## Utility functions
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

__author__ = "Kurt Grutzmacher <kgrutzma@cisco.com>"
__date__ = "3 August 2014"
__version__ = "1.0.0"

KVASIR_JSONRPC_PATH = '/api/call/jsonrpc'

__all__ = ['none_to_blank', 'make_good_url', 'build_kvasir_url']


##-------------------------------------------------------------------------
def none_to_blank(s, exchange=''):
    """Replaces NoneType with ''

    >>> none_to_blank(None, '')
    ''
    >>> none_to_blank(None)
    ''
    >>> none_to_blank('something', '')
    u'something'
    >>> none_to_blank(['1', None])
    [u'1', '']

    :param s: String to replace
    :para exchange: Character to return for None, default is blank ('')
    :return: If s is None, returns exchange
    """
    if isinstance(s, list):
        return [none_to_blank(z) for y, z in enumerate(s)]
    return exchange if s is None else unicode(s)


##-------------------------------------------------------------------------

def make_good_url(url=None, addition="/"):
    """Appends addition to url, ensuring the right number of slashes
    exist and the path doesn't get clobbered.

    >>> make_good_url('http://www.server.com/anywhere', 'else')
    'http://www.server.com/anywhere/else'
    >>> make_good_url('http://test.com/', '/somewhere/over/the/rainbow/')
    'http://test.com/somewhere/over/the/rainbow/'
    >>> make_good_url('None')
    'None/'
    >>> make_good_url()
    >>> make_good_url({})
    >>> make_good_url(addition='{}')

    :param url: URL
    :param addition: Something to add to the URL
    :return: New URL with addition"""

    if url is None:
        return None

    if isinstance(url, str) and isinstance(addition, str):
        return "%s/%s" % (url.rstrip('/'), addition.lstrip('/'))
    else:
        return None


##-------------------------------------------------------------------------

def build_kvasir_url(
        proto="https", server="localhost", port="8443",
        base="Kvasir", user="test", password="test",
        path=KVASIR_JSONRPC_PATH):
    """
    Creates a full URL to reach Kvasir given specific data

    >>> build_kvasir_url('https', 'localhost', '8443', 'Kvasir', 'test', 'test')
    'https://test@test/localhost:8443/Kvasir/api/call/jsonrpc'
    >>> build_kvasir_url()
    'https://test@test/localhost:8443/Kvasir/api/call/jsonrpc'
    >>> build_kvasir_url(server='localhost', port='443', password='password', path='bad/path')
    'https://test@password/localhost:443/Kvasir/bad/path'

    :param proto: Protocol type - http or https
    :param server: Hostname or IP address of Web2py server
    :param port: Port to reach server
    :param base: Base application name
    :param user: Username for basic auth
    :param password: Password for basic auth
    :param path: Full path to JSONRPC (/api/call/jsonrpc)
    :return: A full URL that can reach Kvasir's JSONRPC interface
    """
    uri = proto + '://' + user + '@' + password + '/' + server + ':' + port + '/' + base
    return make_good_url(uri, path)
