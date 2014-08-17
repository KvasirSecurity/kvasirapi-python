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
        """
        Returns a list of all known SNMP community strings

        :param hostfilter: Valid hostfilter or None
        :return: list of community strings
        """
        return self.send.snmp_list_communities(hostfilter)

    def list(self, community=None, hostfilter=None, host=None):
        """
        Returns a list of SNMP information for a community, hostfilter or host
        :param snmpstring: A specific SNMP string to list
        :param hostfilter: Valid hostfilter or None
        :param host: t_hosts.id or t_hosts.f_ipaddr
        :return: [ [ record_id, ipaddr, hostname, community, access, version ] ... ]
        """
        return self.send.snmp_list(community, hostfilter, host)

    def add(self, host=None, f_community=None, f_access=None, f_version=None):
        """
        Add an SNMP community string to a host

        :param host: t_hosts.id or t_hosts.f_ipaddr
        :param f_community: Community string to add
        :param f_access: READ or WRITE
        :param f_version: v1, v2c or v3
        :return: (True/False, t_snmp.id/Error string)
        """
        return self.send.snmp_add(host, f_community, f_access, f_version)

    def delete(self, record=None):
        """
        Delete a t_snmp record

        :param record: [db.t_snmp.id, db.t_snmp_id, ...]
        :return: [(True/False, Response string) ...]
        """
        return self.send.snmp_del(record)

    def rpt_table(self, hostfilter=None):
        """
        Builds a report-like table of community strings, counts and permissions

        :param hostfilter: Valid hostfilter or None
        :return: ([t_snmp.f_community, count, t_snmp.f_access] ...)
        """
        return self.send.snmp_rpt_table(hostfilter)
