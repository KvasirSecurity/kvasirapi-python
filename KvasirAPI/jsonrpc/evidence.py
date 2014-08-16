# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based Evidence for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class Evidence(ConnectorJSONRPC):
    """Evidence"""

    def list(self, host=None):
        """
        List db.t_evidence records

        :param query: A record id, ipv4, ipv6, hostname or None for all records
        :returns t_evidence.id:
        :returns t_evidence.f_type:
        :returns t_evidence.f_other_type:
        :returns t_evidence.f_text:
        :returns t_evidence.f_evidence:
        :returns t_evidence.f_filename:
        """
        return self.send.evidence_list(host)

    def download(self, filename=None):
        """
        Download a specific evidence file

        :param filename: Filename to download
        :return: File content
        """
        return self.send.evidence_download(filename)

    def add(self, host, filename, data, f_type, f_other_type=None, f_text=''):
        """
        Add evidence

        :param host: db.t_hosts.id
        :param filename: Filename
        :param data: Content of file
        :param f_type: Evidence type
        :param f_other_type: If f_type is 'Other' what type it is
        :param f_text: Text information about the evidence
        :return: (True/False, response message)
        """
        return self.send.evidence_add(host, filename, data, f_type, f_other_type, f_text)

    def delete(self, evidence_records=None):
        """
        Delete evidence record(s)

        :param evidence_records: [db.t_evidence.id, db.t_evidence.id, ... ]
        :return: List of (True/False, response message) for each evidence
        """
        return self.send.evidence_del(evidence_records)
