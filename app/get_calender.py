#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
from pathlib import Path

def getMode(mode='s'):
    if mode.lower() == 'c':
        # connpass
        print('mode connpass')
        time.sleep(1)
        return { 
                'URL': 'https://connpass.com/api/v1/event/',
                'dir': 'connpass/',
                'etc': 'c',
                }
        # colab
    print('mode colab')
    time.sleep(1)
    return { 
            'URL': 'https://supporterzcolab.com/api/v1/event/',
            'dir': 'colab/',
            'etc': 's',
            }


template = """
<p>勉強会タイトル {title}</p>
<p>場所 {place}</p>
<p>説明 {description}</p>
<p>時間 {started_at} - {ended_at}</p>
<p>url {event_url}</p>
"""


def get_week_date(mode='s', **kward):
    from datetime import datetime as dt, timedelta

    settings = getMode(mode)    
    initFolder(settings['dir'])

    params = dict()
    params['order'] = kward.get('order', 1)
    params['count'] = kward.get('count', 10)
    start_date = dt.now()
    if kward.get('start_date'):
        sd = kward.get('start_date')
        if isinstance(str, sd):
            try:
                start_date = dt.strptime(sd, '%Y/%m/%d')
            except Exception as e:
                print('日付形式がおかしいです', sd)
                raise e
        elif isinstance(datetime, sd):
            start_date = sd
        else:
            print('start_dateはstring, datetimeのどちらかでお願いします。')
            raise TypeError
    
    print_seperetor = '###################################################'
    response_list = [] 
    for i in range(7):
        date_delta = timedelta(days=i)
        d = start_date + date_delta
        params['ymd'] = dt.strftime(d, '%Y%m%d')
        
        params_format = '&'.join([('{0}={1}').format(k, v) for k, v in params.items()])
        if not params_format:
            print('skip')
            continue
        print(settings, params_format)
        access_point = '{0}?{1}'.format(settings['URL'], params_format)

        if kward.get('debug'):
            print(access_point)
            print(print_seperetor)
            print()
            continue
        
        responce = requests.get(access_point).json()
        stack = []
        for elem in responce['events']:
            elem['description'] = elem['description'][:100]
            # print('\n'.join(['{0}={1}'.format(k, v) for k, v in elem.items()]))
            # stack.append('\n'.join(['{0}={1}'.format(k, v) for k, v in elem.items()]) + '\n')
            print(template.format(**elem))
            stack.append('\n'.join([print_seperetor, template.format(**elem), print_seperetor]))
        
        with open(settings['dir'] + params['ymd'] + settings['etc'] + '.txt', 'w') as f:
            f.write('\n'.join(stack))
            response_list.append('\n'.join(stack))
        
        print()
        time.sleep(1)
    return '\n'.join(response_list)

def initFolder(dirpath):
    Path(dirpath).mkdir(exist_ok=True)

if __name__== '__main__':
    mode = input('C: connpass, S:Colab -> ')
    get_week_date(mode=mode, count=80)
