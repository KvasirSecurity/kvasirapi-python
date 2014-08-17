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
        """
        Returns a list of vulnerabilities based on t_hosts.id or t_services.id.
        If neither are set then statistical results are added

        :param host_rec: db.t_hosts.id
        :param service_rec: db.t_services.id
        :param hostfilter: Valid hostfilter or None
        :return: [(vulndata) ...] if host_rec or service_rec set
        :return: [(vulndata, vuln_cnt, [vuln_ip, ...], [services ...]) ...] if nothing sent
        """
        return self.send.vuln_list(host_rec, service_rec, hostfilter)

    def info(self, vuln_name=None, vuln_id=None):
        """
        Returns information about a vulnerability

        :param vuln_name: t_vulndata.f_vulnid
        :param vuln_id: t_vulndata.id
        :return: vulnerability data
        """
        return self.send.vuln_info(vuln_name, vuln_id)

    def ip_info(self, vuln_name=None, vuln_id=None, ip_list_only=True, hostfilter=None):
        """
        List of all IP Addresses with a vulnerability

        :param vuln_name: t_vulndata.f_vulnid
        :param vuln_id: t_vulndata.id
        :param ip_list_only: IP List only (default) or rest of t_hosts fields
        :param hostfilter: Valid hostfilter or none
        :return: [(ip, hostname) ...] or [(ip, hostname, t_service_vulns.f_proof, t_service_vulns.f_status), ...]
        """
        return self.send.vuln_ip_info(vuln_name, vuln_id, ip_list_only, hostfilter)

    def service_list(self, vuln_name=None, vuln_id=None, hostfilter=None):
        """
        Returns a dictionary of vulns with services and IP Addresses

        :param vuln_name: t_vulndata.f_vulnid
        :param vuln_id: t_vulndata.id
        :param hostfilter: Valid hostfilter or none
        :return: {'vuln-id': {'port': [ ip, hostname ]} ...} ...
        """
        return self.send.vuln_service_list(vuln_name, vuln_id, hostfilter)
