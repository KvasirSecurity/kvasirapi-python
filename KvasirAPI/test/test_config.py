# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## Configuration test routines
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

################################################################
## Test routines for yaml string format
################################################################


def test_web2py_string(configure_string):
    assert configure_string.configuration.web2py_dir == '/opt/web2py/'


def test_customer_string(configure_string):
    assert configure_string.configuration.customer.get('id') == '11-ACME-01'
    assert configure_string.configuration.customer.get('full-name') == 'ACME Widgets, Inc.'
    assert configure_string.configuration.customer.get('short-name') == 'ACME'
    assert configure_string.configuration.customer.get('possessive') == "ACME Widget, Inc's"
    assert configure_string.configuration.customer.get('short-capital') == 'ACME'
    assert configure_string.configuration.customer.get('possessive-capital') == "ACME's"


def test_instances_string(configure_string):
    assert configure_string.configuration.instances_dict.get('internal').get('url') == "http://username:password@localhost:8000/internal/"
    assert configure_string.configuration.instances_dict.get('internal').get('name') == 'Internal Network'
    assert configure_string.configuration.instances_dict.get('internal').get('start') == 'May 2, 2011'
    assert configure_string.configuration.instances_dict.get('internal').get('end') == 'May 6, 2011'
    assert configure_string.configuration.instances_dict.get('internal').get('filter_type') == 'assetgroup'
    assert configure_string.configuration.instances_dict.get('internal').get('filter_value') == 'organization'
    assert configure_string.configuration.instances_dict.get('external').get('url') == "http://username:password@localhost:8000/external/"
    assert configure_string.configuration.instances_dict.get('external').get('start') == 'May 2, 2011'
    assert configure_string.configuration.instances_dict.get('external').get('end') == "May 6, 2011"
    assert configure_string.configuration.instances_dict.get('external').get('name') == 'External Network'


def test_instance_uri_string(configure_string):
    assert configure_string.configuration.instance_uri('internal') == 'http://username:password@localhost:8000/internal/'
    assert configure_string.configuration.instance_uri('external') == 'http://username:password@localhost:8000/external/'


def test_instance_list_string(configure_string):
    internals = configure_string.configuration.instances('internal')
    assert len(internals) == 1
    externals = configure_string.configuration.instances('external')
    assert len(externals) == 1


################################################################
## Test routines for yaml configuration file
################################################################

def test_web2py_file(configure_file):
    assert configure_file.configuration.web2py_dir == 'build/web2py'


def test_customer_file(configure_file):
    assert configure_file.configuration.customer.get('id') == '11-ACME-01'
    assert configure_file.configuration.customer.get('full-name') == 'ACME Widgets, Inc.'
    assert configure_file.configuration.customer.get('short-name') == 'ACME'
    assert configure_file.configuration.customer.get('possessive') == "ACME Widget, Inc's"
    assert configure_file.configuration.customer.get('short-capital') == 'ACME'
    assert configure_file.configuration.customer.get('possessive-capital') == "ACME's"


def test_instances_file(configure_file):
    assert configure_file.configuration.instances_dict.get('internal').get('url') == "http://username:password@localhost:8000/internal/"
    assert configure_file.configuration.instances_dict.get('internal').get('name') == 'Internal Network'
    assert configure_file.configuration.instances_dict.get('internal').get('start') == 'May 2, 2011'
    assert configure_file.configuration.instances_dict.get('internal').get('end') == 'May 6, 2011'
    assert configure_file.configuration.instances_dict.get('internal').get('filter_type') == 'assetgroup'
    assert configure_file.configuration.instances_dict.get('internal').get('filter_value') == 'organization'
    assert configure_file.configuration.instances_dict.get('external').get('url') == "http://username:password@localhost:8000/external/"
    assert configure_file.configuration.instances_dict.get('external').get('start') == 'May 2, 2011'
    assert configure_file.configuration.instances_dict.get('external').get('end') == "May 6, 2011"
    assert configure_file.configuration.instances_dict.get('external').get('name') == 'External Network'


def test_instance_uri_file(configure_file):
    assert configure_file.configuration.instance_uri('internal') == 'http://username:password@localhost:8000/internal/'
    assert configure_file.configuration.instance_uri('external') == 'http://username:password@localhost:8000/external/'


def test_instance_list_file(configure_file):
    internals = configure_file.configuration.instances('internal')
    externals = configure_file.configuration.instances('external')
    assert len(internals) == 2
    assert len(externals) == 1

