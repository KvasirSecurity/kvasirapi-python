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
    """Evidence files"""

    def list(self, host=None):
        return self.send.evidence_list(host)

    def download(self, filename=None):
        return self.send.evidence_download(filename)

    def add(self, host, filename, data, f_type, f_other_type=None, f_text=''):
        return self.send.evidence_add(host, filename, data, f_type, f_other_type, f_text)

    def delete(self, evidence_records=None):
        return self.send.evidence_del(evidence_records)
