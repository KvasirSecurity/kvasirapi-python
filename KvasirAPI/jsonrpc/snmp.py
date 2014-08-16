# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based SNMP for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class SNMP(ConnectorJSONRPC):
    """SNMP"""

    def list_communities(self, hostfilter=None):
        return self.send.snmp_list_communities(hostfilter)

    def list(self, community=None, hostfilter=None):
        return self.send.snmp_list(community, hostfilter)

    def add(self, host=None, f_community=None, f_access=None, f_version=None):
        return self.send.snmp_add(host, f_community, f_access, f_version)

    def delete(self, record=None):
        return self.send.snmp_del(record)

    def rpt_table(self, hostfilter=None):
        return self.send.snmp_rpt_table(hostfilter)
