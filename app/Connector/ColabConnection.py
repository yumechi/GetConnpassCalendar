#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ConnpassConnectionBase import ConnpassConnectionBaseMixin

__all__ = [
    'ColabConnection',
]

class ColabConnection(ConnpassConnectionBaseMixin):
    """
    Colab用コネクション設定
    """
    default_base_url = 'https://supporterzcolab.com/api/v1'
