
import sys
import logging
from ..utils import make_good_url


##-------------------------------------------------------------------------
class ConnectorJSONRPC():
    """Welcome to the grand ConnectorJSONRPC. It loves to talk to Kvasir
JSONRPC instances to send it commands and gobble its responses. That's all!

To use it: ConnectorJSONRPC.send.<api command>(variables)

:param instance: dict of KvasirAPI.instance
:param web2py_dir: string of web2py directory, if configured, for simplejsonrpc library
:return: JSONRPC connector routine
"""

    def __init__(self, instance=None, web2py_dir=None):
        self.log = logging.getLogger(str(self.__class__))
        self.instance = instance or {}
        self.web2py_dir = web2py_dir
        self.kvasir_jsonrpc_path = '/api/call/jsonrpc'
        if self.web2py_dir:
            sys.path.append(self.web2py_dir)
        try:
            import jsonrpclib
            has_jsonrpclib = True
        except ImportError:
            try:
                from gluon.contrib import simplejsonrpc
                has_jsonrpclib = False
            except ImportError:
                raise ImportError("""**** ERROR ****\n

    Unable to find and load the JSONRPC library. There are two options:

    Option 1: Set web2py path in your YAML configuration file
    Option 2: pip install jsonrpclib

    sys.path = %s
        """ % sys.path)
        kvasir_path = make_good_url(self.instance.get('url'), self.kvasir_jsonrpc_path)
        if has_jsonrpclib:
            self.send = jsonrpclib.Server(kvasir_path)
        else:
            self.send = simplejsonrpc.ServerProxy(kvasir_path)

    def version_check(self):
        # TODO: error handling when server isn't up
        version = self.send.version()
        if version != self.api_version:
            raise RuntimeError("Expected API version %s but communicating with version %s" %
                               (self.api_version, version))
