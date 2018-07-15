#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ConnpassConnectionBase import ConnpassConnectionBaseMixin

__all__ = [
    'ConnpassConnection',
]

class ConnpassConnection(ConnpassConnectionBaseMixin):
    """
    Connpass用コネクション設定
    """
    default_base_url = 'https://connpass.com/api/v1'
