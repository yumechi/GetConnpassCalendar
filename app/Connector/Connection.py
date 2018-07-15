#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

__all__ = [
    'Connection',
]


class Connection(object):
    """
    requestsのラッパー
    @param: default_base アクセスポイント
    """
    default_base_url = None

    def __init__(self, **kward):
        '''
        @param: access_base APIのベースURL
        '''
        self.access_base_url = kward.get('access_base',
                                         None) or self.default_base_url

    def execute_get(self, api_point: str, params: dict) -> dict:
        """
        get method を実行する
        @return: Request結果のdict
        """
        url = self.access_base_url + api_point
        if len(params) > 0:
            url += '?' + "&".join([f'{key}={value}'
                                   for key, value in params.items()])
        return requests.get(url).json()
