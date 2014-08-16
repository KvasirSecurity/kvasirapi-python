# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based NetBIOS for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class NetBIOS(ConnectorJSONRPC):
    """NetBIOS"""

    def list(self, hostfilter=None):
        return self.send.netbios_list(hostfilter)

    def rpt_table(self, hostfilter=None):
        return self.send.netbios_rpt_table(hostfilter)

    def domain_members(self, domain=None, hostfilter=None):
        return self.send.netbios_domain_members(domain, hostfilter)

    def domain_controllers(self, domain=None, hostfilter=None):
        return self.send.netbios_domain_controllers(domain, hostfilter)
