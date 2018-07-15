#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Connection import Connection
from MyConnectionError import ValidateBaseAPIException

__all__ = [
    'ConnpassConnectionBaseMixin',
]

class ConnpassConnectionBaseMixin(Connection):
    """
    Connpass系サービスアクセス用のMixin
    """
    default_base_url = None

    def __init__(self, **kward):
        if kward.get('access_base', None) or not self.default_base_url:
            raise ValidateBaseAPIException(kward)
        super().__init__(**kward)

    def get_events(self, params):
        return self.execute_get(api_point='/event/', params=params)
