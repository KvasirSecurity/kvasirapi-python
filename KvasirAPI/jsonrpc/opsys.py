# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based Operating Systems for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class OpSys(ConnectorJSONRPC):
    """Operating Systems"""

    def list(self, hostfilter=None):
        return self.send.os_list(hostfilter)

    def report_list(self, hostfilter=None):
        return self.send.os_report_list(hostfilter)