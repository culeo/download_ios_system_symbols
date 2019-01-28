# coding:utf-8

import re
import string
import os
import json

orgin_path = os.path.split(os.path.realpath(__file__))[0] + "/google.json"
save_path = os.path.split(os.path.realpath(__file__))[0] + "/Keys.json"

def update():
    res = []
    with open(orgin_path, 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            key = item['id']
            name = item['title']
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
            res.append(dic)
    print '有：%d 个' % len(res)
    print save_path
    with open(save_path, 'w') as json_file:
        json.dump(res, json_file, indent=1)


if __name__ == '__main__':
    update()