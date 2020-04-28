# coding: utf-8

import json
import re
import os
import time
import string
import requests

urls = ['https://drive.google.com/drive/folders/0B-0LZDbSzubRaUdMdTJQc1ZzMUU',
        'https://drive.google.com/drive/folders/0B5oBYvBG2NS7aDVTR1JzX2JXaFE',
        'https://drive.google.com/drive/folders/0B9ItUz-PHtRLb3hidV9kUGJUMkE',
        'https://drive.google.com/drive/folders/1beYMn69Y36zAlB2E1htmejYYYwpZclJ6']

def update_google_url(index):
    
    url = urls[index]
    html = requests.get(url).text.encode('utf-8')
    print url
    # print html
    print '------------'
    regex = 'x22([0-9a-zA-Z_-]{18,})'
    res = re.findall(regex, html)
    res = list(set(res))
    array = []

    print res
    for key in res:
        # print key
        output = os.popen('gdrive --service-account key.json info ' + key + ' | grep \'^Name:\'')
        name = output.read()[6:-1]
        # print name
        if string.find(name, '7z') != -1:
            version = re.search('\((.*?)\)', name).group(1)
            system = re.search('[0-9.]*', name).group(0)
            isCache = string.find(name, 'Cache') != -1
            print 'key: ' + key
            print 'name: ' + name
            print 'system: ' + system
            print 'version: ' + version
            print 'cache: true' if isCache else 'cache: false'
            print '------------------------'
            dic = {'name': name, 'key': key, 'version': version, 'system': system, 'cache': isCache}
            array.append(dic)
        time.sleep(2)
    print '有：%d 个' % len(array)

    path = os.path.split(os.path.realpath(__file__))[0] + "/Google-" + str(index) + ".json"

    with open(path, 'w') as json_file:
        json.dump(array, json_file, indent=1)

