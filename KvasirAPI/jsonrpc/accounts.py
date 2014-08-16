# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based Accounts for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from .connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class Accounts(ConnectorJSONRPC):
    """User accounts"""

    def list(self, svc_rec=None, hostfilter=None, compromised=False):
        return self.send.accounts_list(svc_rec, hostfilter, compromised)

    def add(self, svc_rec=None, records=None):
        return self.send.accounts_add(svc_rec, records)

    def info(self, rec=None):
        return self.send.accounts_info(rec)

    def update(self, rec=None, values=None):
        return self.send.accounts_update(rec, values)

    def list_pw_types(self):
        return self.send.list_pw_types()

    def upload_file(self, service_rec=None, host_service=None, filename=None,
                    pw_data=None, f_type=None, add_to_evidence=True):
        return self.send.accounts_upload_file(service_rec, host_service, filename, pw_data, f_type, add_to_evidence)

    def delete(self, rec=None):
        return self.send.accounts_del(rec)

    def index_data(self, hostfilter=None):
        return self.send.accounts_index_data(hostfilter)
