# coding:utf-8

import re
import string
import os
import json

orgin_path = os.path.split(os.path.realpath(__file__))[0]
save_path = os.path.split(os.path.realpath(__file__))[0] + "/Keys.json"

def update():
    res = []
    for i in range(4):
        with open(orgin_path + "/Google-" + str(i) + ".json", 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                res.append(item)

    print '有：%d 个' % len(res)
    print save_path
    with open(save_path, 'w') as json_file:
        json.dump(res, json_file, indent=1)


if __name__ == '__main__':
    update()
