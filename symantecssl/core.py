from __future__ import absolute_import, division, print_function

from .auth import SymantecAuth
from .order import Order, GetOrderByPartnerOrderID, ModifyOrder
from .session import SymantecSession


class Symantec(object):

    order_class = Order
    get_order_by_partner_order_id_class = GetOrderByPartnerOrderID
    modify_order_class = ModifyOrder

    def __init__(self, username, password,
                 url="https://api.geotrust.com/webtrust/partner"):
        self.url = url
        self.session = SymantecSession()
        self.session.auth = SymantecAuth(username, password)

    def submit(self, obj):
        resp = self.session.post(self.url, obj.serialize())
        resp.raise_for_status()

        return obj.response(resp.content)

    def order(self, **kwargs):
        obj = self.order_class(**kwargs)
        return self.submit(obj)

    def get_order_by_partner_order_id(self, **kwargs):
        return self.submit(self.get_order_by_partner_order_id_class(**kwargs))

    def modify_order(self, **kwargs):
        return self.submit(self.modify_order_class(**kwargs))
