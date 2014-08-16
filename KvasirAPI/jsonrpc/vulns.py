# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based Vulnerabilities for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class Vulns(ConnectorJSONRPC):
    """Vulnerabilities"""

    def list(self, host_rec=None, service_rec=None, hostfilter=None):
        return self.send.vuln_list(host_rec, service_rec, hostfilter)

    def info(self, vuln_name=None, vuln_id=None):
        return self.send.vuln_info(vuln_name, vuln_id)

    def ip_info(self, vuln_name=None, vuln_id=None, ip_list_only=True, hostfilter=None):
        return self.send.vuln_ip_info(vuln_name, vuln_id, ip_list_only, hostfilter)

    def service_list(self, vuln_name=None, vuln_id=None, hostfilter=None):
        return self.send.vuln_service_list(vuln_name, vuln_id, hostfilter)
