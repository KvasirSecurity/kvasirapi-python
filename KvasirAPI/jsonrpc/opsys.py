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

    def list(self, hostfilter=None, host=None):
        """
        Lists Operating Systems based on hostfilter or Address

        :param hostfilter: Valid hostfilter dict or None
        :param host: IP Address or t_hosts.id
        :return: [os_ref_rec.t_hosts.f_ipaddr,
                     os_ref_rec.t_hosts.f_hostname,
                     os_ref_rec.t_host_os_refs.f_certainty,
                     os_ref_rec.t_host_os_refs.f_class,
                     os_ref_rec.t_host_os_refs.f_family,
                     os_rec.f_cpename,
                     os_rec.f_title,
                     os_rec.f_vendor,
                     os_rec.f_product,
                     os_rec.f_version,
                     os_rec.f_update,
                     os_rec.f_edition,
                     os_rec.f_language
                     ]
        """
        return self.send.os_list(hostfilter, host)

    def report_list(self, hostfilter=None):
        """
        Lists top Operating Systems and host records based on hostfilter

        :param hostfilter: Valid hostfilter dict or None
        :return: [row.t_hosts.id,
                         row.t_hosts.f_ipaddr,
                         row.t_hosts.f_hostname,
                         highest[1].t_host_os_refs.f_certainty,
                         highest[1].t_host_os_refs.f_class,
                         highest[1].t_host_os_refs.f_family,
                         os_rec.f_cpename,
                         os_rec.f_title,
                         os_rec.f_vendor,
                         os_rec.f_product,
                         os_rec.f_version,
                         os_rec.f_update,
                         os_rec.f_edition,
                         os_rec.f_language
                         ]
        """
        return self.send.os_report_list(hostfilter)