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
        """
        List a specific service or all services

        :param service_rec: t_services.id
        :param host_rec: t_hosts.id
        :param hostfilter: Valid hostfilter or None
        :return: [(svc.t_services.id, svc.t_services.f_hosts_id, svc.t_hosts.f_ipaddr,
             svc.t_hosts.f_hostname, svc.t_services.f_proto,
             svc.t_services.f_number, svc.t_services.f_status, svc.t_services.f_name,
             svc.t_services.f_banner), ...]
        """
        return self.send.service_list(service_rec, host_rec, hostfilter)

    def list_only(self, host_rec=None, hostfilter=None):
        """
        Returns a list of ports based on a t_hosts.id, hostfilter or all

        :param host_rec: t_hosts.id
        :param hostfilter: Valid hostfilter or None
        :return: [ service_id, host_id, ip, hostname, proto, number, status, name, banner, [ vuln list ...] ]
        """
        return self.send.service_list_only(host_rec, hostfilter)

    def info(self, svc_rec=None, ipaddr=None, proto=None, port=None):
        """
        Information about a service.

        :param svc_rec: t_services.id
        :param ipaddr: IP Address
        :param proto: Protocol (tcp, udp, info)
        :param port: Port (0-65535)
        :return: [ service_id, host_id, ipv4, ipv6, hostname, proto, number, status, name, banner ]
        """
        return self.send.service_info(svc_rec, ipaddr, proto, port)

    def add(self, ipaddr=None, proto=None, port=None, fields=None):
        """
        Add a service record

        :param ipaddr: IP Address
        :param proto: Protocol (tcp, udp, info)
        :param port: Port (0-65535)
        :param fields: Extra fields
        :return: (True/False, t_services.id or response message)
        """
        return self.send.service_add(ipaddr, proto, port, fields)

    def delete(self, svc_rec=None, ipaddr=None, proto=None, port=None):
        """
        Delete a t_services record

        :param svc_rec: t_services.id
        :param ipaddr: IP Address or t_hosts.id
        :param proto: Protocol (tcp, udp, info)
        :param port: Port (0-65535)
        :return: [True, Response Message]
        """
        return self.send.service_del(svc_rec, ipaddr, proto, port)

    def index_stats(self, hostfilter=None):
        """
        Returns a services index of statistics

        :param hostfilter: Valid hostfilter or None
        :return: { 'service': [t_service.f_name, host count, unique vuln count, total vuln count], ... }
        """
        return self.send.service_rpt_index_stats(hostfilter)

    def report_list(self, service_id=None, service_port=None, hostfilter=None):
        """
        Returns a list of ports with IPs, banners and vulnerabilities (warning, slow!)

        :param service_id: t_services.id
        :param service_port: Port (tcp/#, udp/#, info/#)
        :param hostfilter: Valid hostfilter or None
        :return: { 'port': [t_hosts.f_ipaddr, t_services.f_banner,
            (t_vulndata.f_vulnid, t_vulndata.f_title, t_vulndata.f_severity, t_vulndata.f_cvss_score), ...}
        """
        return self.send.service_report_list(service_id, service_port, hostfilter)

    def vulns_list(self, service_id=None, service_port=None, hostfilter=None):
        """
        List of vulnerabilities for a service

        :param service_id: t_services.id
        :param service_port: tcp/#, udp/# or info/#
        :param hostfilter: Valid hostfilter or None
        :return: t_services.rows.as_list()
        """
        return self.send.service_vulns_list(service_id, service_port, hostfilter)

    def vuln_iptable(self, hostfilter=None):
        """
        Returns a dict of services containing IPs with (vuln, severity)

        :param hostfilter: Valid hostfilter or None
        :return: '0/info': { 'host_id1': [ (ip, hostname), ( (vuln1, 5), (vuln2, 10) ... ) ] },
              { 'host_id2': [ (ip, hostname), ( (vuln1, 5) ) ] }

        """
        return self.send.service_vuln_iptable(hostfilter)
