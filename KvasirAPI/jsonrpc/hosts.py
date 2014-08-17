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
        """
        List of t_hosts

        :param hostfilter: Valid hostfilter or None
        :return: [(host.id, host.f_ipaddr, host.f_macaddr, host.f_hostname,
             host.f_netbios_name, db.auth_user[host.f_engineer].username, host.f_asset_group,
             host.f_confirmed) ...]
        """
        return self.send.host_list(hostfilter)

    def add(self, f_ipaddr, f_macaddr, f_hostname, f_netbios_name, f_engineer, f_asset_group, f_confirmed):
        """
        Add a t_hosts record

        :param f_ipaddr: IP address
        :param f_macaddr: MAC Address
        :param f_hostname: Hostname
        :param f_netbios_name: NetBIOS Name
        :param f_engineer: Engineer username
        :param f_asset_group: Asset group
        :param f_confirmed: Confirmed boolean
        :return: (True/False, t_hosts.id or response message)
        """
        return self.send.host_add(f_ipaddr, f_macaddr, f_hostname, f_netbios_name, f_engineer,
                                  f_asset_group, f_confirmed)

    def info(self, host=None):
        """
        Info about a t_hosts record

        :param host: t_hosts.id or IP Address
        :return: t_hosts fields
        """
        return self.send.host_info(host)

    def detail(self, host=None):
        """
        Detailed information about a host, not just t_hosts record

        :param host: t_hosts.id or IP Address
        :return: Dictionary of t_hosts record, additional points, services, accounts, vulns and snmp
        """
        return self.send.host_details(host)

    def delete(self, host=None, ipaddr_list=None):
        """
        Delete a t_hosts record or list of records

        :param host: t_hosts.id or list of ids
        :param ipaddr_list: IP Address or list of IP Addresses
        :return: [host_recs deleted, ip_recs deleted]
        """
        return self.send.host_del(host, ipaddr_list)
