# -*- coding: utf-8 -*-

##--------------------------------------#
## API for Kvasir
##
## (c) 2010-2014 Cisco Systems, Inc.
##
## JSONRPC-based DB Stats for KvasirAPI
##
## Author: Kurt Grutzmacher <kgrutzma@cisco.com>
##--------------------------------------#

from .connector import ConnectorJSONRPC


##-------------------------------------------------------------------------
class Stats(ConnectorJSONRPC):
    """Database Statistics"""

    def dbcount(self, tblist=[], hostfilter=None):
        """
        Database statistics

        :param tblist: List of table names to gather stats from
        :param hostfilter: Valid hostfilter or None
        :return: Dictionary of {table: count}
        """
        return self.send.tbl_count(tblist, hostfilter)
