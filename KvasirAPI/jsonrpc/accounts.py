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
        """
        List user accounts

        :param svc_rec: db.t_services.id
        :param hostfilter:
        :param compromised: Show only compromised accounts
        :return: [acct.t_accounts.f_services_id, acct.t_hosts.f_ipaddr,
                     acct.t_hosts.f_hostname,
                     acct.t_accounts.id, acct.t_accounts.f_username,
                     acct.t_accounts.f_fullname, acct.t_accounts.f_password,
                     acct.t_accounts.f_compromised, acct.t_accounts.f_hash1,
                     acct.t_accounts.f_hash1_type, acct.t_accounts.f_hash2,
                     acct.t_accounts.f_hash2_type, acct.t_accounts.f_source,
                     acct.t_accounts.f_uid, acct.t_accounts.f_gid,
                     acct.t_accounts.f_level, acct.t_accounts.f_domain,
                     acct.t_accounts.f_message, acct.t_accounts.f_lockout,
                     acct.t_accounts.f_duration, acct.t_accounts.f_active,
                     acct.t_accounts.f_description,
                     acct.t_services.f_proto, acct.t_services.f_number,
                   ]
        """
        return self.send.accounts_list(svc_rec, hostfilter, compromised)

    def add(self, svc_rec=None, records=None):
        """
        Add account data

        :param svc_rec: db.t_services.id
        :param records: db.t_accounts field content dictionary
        :return: (True/False, db.t_accounts.id)
        """
        return self.send.accounts_add(svc_rec, records)

    def info(self, rec=None):
        """
        Information about an account

        :param rec: db.t_accounts.id
        :return: [True/False, hostrec.f_ipaddr, hostrec.f_hostname,
            svc_rec.f_proto, svc_rec.f_number,
            acct.id, acct.f_username, acct.f_fullname, acct.f_password,
            acct.f_compromised, acct.f_hash1, acct.f_hash1_type, acct.f_hash2,
            acct.f_hash2_type, acct.f_source, acct.f_uid, acct.f_gid,
            acct.f_level, acct.f_domain, acct.f_message, acct.f_lockout,
            acct.f_duration, acct.f_active, acct.f_description]
        """
        return self.send.accounts_info(rec)

    def update(self, rec=None, values=None):
        """
        Update a db.t_accounts record

        :param rec: db.t_accounts.id
        :param values: db.t_accounts fields to update
        :return: (True/False, Message)
        """
        return self.send.accounts_update(rec, values)

    def list_pw_types(self):
        """
        List the known password types
        :return:
        """
        return self.send.list_pw_types()

    def upload_file(self, service_rec=None, host_service=None, filename=None,
                    pw_data=None, f_type=None, add_to_evidence=True):
        """
        Upload a password file

        :param service_rec: db.t_services.id
        :param host_service: db.t_hosts.id
        :param filename: Filename
        :param pw_data: Content of file
        :param f_type: Type of file
        :param add_to_evidence: True/False to add to t_evidence
        :return: (True/False, Response Message)
        """
        return self.send.accounts_upload_file(service_rec, host_service, filename, pw_data, f_type, add_to_evidence)

    def delete(self, rec=None):
        """
        Delete a db.t_accounts record

        :param rec: [db.t_accounts.id, db.t_accounts.id, ... ]
        :return: (True/False, Message string)
        """
        return self.send.accounts_del(rec)

    def index_data(self, hostfilter=None):
        """
        List of IP Addresses and account statistics.

        :param hostfilter: Hostfilter dict
        :return:
        """
        return self.send.accounts_index_data(hostfilter)
