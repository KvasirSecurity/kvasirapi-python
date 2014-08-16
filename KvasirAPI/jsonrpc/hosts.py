# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based hosts for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from .connector import ConnectorJSONRPC


class Hosts(ConnectorJSONRPC):
    def list(self, hostfilter=None):
        return self.send.host_list(hostfilter)

    def add(self, f_ipaddr, f_macaddr, f_hostname, f_netbios_name, f_engineer, f_asset_group, f_confirmed):
        return self.send.host_add(f_ipaddr, f_macaddr, f_hostname, f_netbios_name, f_engineer,
                                  f_asset_group, f_confirmed)

    def info(self, host=None):
        return self.send.host_info(host)

    def detail(self, host=None):
        return self.send.host_details(host)

    def delete(self, host=None, ipaddr_list=None):
        return self.send.host_del(host, ipaddr_list)
