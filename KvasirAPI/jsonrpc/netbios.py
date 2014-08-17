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
        """
        List NetBIOS workgroups/domains for a hostfilter (or all if None)

        :param hostfilter: Valid hostfilter dict or None
        :return: (rec.t_hosts.f_ipaddr, rec.t_hosts.f_hostname,
                     rec.t_netbios.f_type, rec.t_netbios.f_advertised_names,
                     rec.t_netbios.f_domain, rec.t_netbios.f_lockout_limit,
                     rec.t_netbios.f_lockout_duration, rec.t_netbios.f_shares)
        """
        return self.send.netbios_list(hostfilter)

    def rpt_table(self, hostfilter=None):
        """
        Generate a list of domains and number of hosts in each

        :param hostfilter: Valid hostfilter dict or None
        :return: (t_netbios.f_domain, count)
        """
        return self.send.netbios_rpt_table(hostfilter)

    def domain_members(self, domain=None, hostfilter=None):
        """
        List domain member IP Addresses

        :param domain: Domain name
        :param hostfilter: Valid hostfilter dict or None
        :return: (t_hosts.f_ipaddr)
        """
        return self.send.netbios_domain_members(domain, hostfilter)

    def domain_controllers(self, domain=None, hostfilter=None):
        """
        Returns a list of domain controller IP Addresses

        :param domain: Domain name
        :param hostfilter: Valid hostfilter dict or None
        :return: (t_hosts.f_ipaddr)
        """
        return self.send.netbios_domain_controllers(domain, hostfilter)
