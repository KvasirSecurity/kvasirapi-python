# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## Hosts test routines
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#


def test_hosts_add(configure_file):
    fields = {
        'f_ipaddr': '1.1.1.1',
        'f_macaddr': 'aa:bb:cc:dd:ee:ff',
        'f_hostname': 'kvasir-test',
        'f_netbios_name': 'KVASIR-TEST',
        'f_engineer': 'test',
        'f_asset_group': 'kvasir-test',
        'f_confirmed': False
    }
    host_id = configure_file.call.test.hosts.add(**fields)
    assert host_id

