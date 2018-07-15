#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = [
    'ValidateBaseAPIException',
]

class ValidateBaseAPIException(Exception):
    def __init__(self, errors):
        super().__init__('デフォルトのURLはセット不能です:{errors}'.format(
            errors=errors))
