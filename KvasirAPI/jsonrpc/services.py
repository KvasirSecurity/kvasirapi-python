# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based Services for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class Services(ConnectorJSONRPC):
    """Services"""

    def list(self, service_rec=None, host_rec=None, hostfilter=None):
        return self.send.service_list(service_rec, host_rec, hostfilter)

    def list_only(self, host_rec=None, hostfilter=None):
        return self.send.service_list_only(host_rec, hostfilter)

    def info(self, svc_rec=None, ipaddr=None, proto=None, port=None):
        return self.send.service_info(svc_rec, ipaddr, proto, port)

    def add(self, ipaddr=None, proto=None, port=None, fields=None):
        return self.send.service_add(ipaddr, proto, port, fields)

    def delete(self, svc_rec=None, ipaddr=None, proto=None, port=None):
        return self.send.service_del(svc_rec, ipaddr, proto, port)

    def index_stats(self, hostfilter):
        return self.send.service_rpt_index_stats(hostfilter)

    def report_list(self, service_id=None, service_port=None, hostfilter=None):
        return self.send.service_report_list(service_id, service_port, hostfilter)

    def vulns_list(self, service_id=None, service_port=None, hostfilter=None):
        return self.send.service_vulns_list(service_id, service_port, hostfilter)

    def vuln_iptable(self, hostfilter=None):
        return self.send.service_vuln_iptable(hostfilter)
