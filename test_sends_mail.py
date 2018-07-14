from nameko.rpc import RpcProxy, rpc
from nameko.testing.services import worker_factory

def test_sends_mail():

    service = worker_factory(SendsMail)
