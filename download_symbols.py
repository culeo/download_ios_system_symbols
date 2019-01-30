# coding=utf-8
import sys
import getopt
import subprocess
import os
import requests

url = 'https://raw.githubusercontent.com/culeo/download_ios_system_symbols/master/Keys.json'
path = os.path.expanduser('~') + '/Library/Developer/Xcode/iOS DeviceSupport/'
cache_path = '/Symbols/System/Library/Caches/'
cache_file_path = cache_path + 'com.apple.dyld'

def run_cmd(cmds):
    popen = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

    # 重定向标准输出
    while popen.poll() is None:
        r = popen.stdout.readline().decode("gbk")
        sys.stdout.write(r)


def download(version, cache=False):
    print '搜索中...'
    json = requests.get(url, timeout=30).json()
    key = ''
    name = ''
    system = ''
    for item in json:
        if item['version'] == version and (item['cache'] is cache):
            key = item['key'].encode('utf-8')
            name = item['name']
            system = item['system']
            break
    if key is '':
        print '未找到：' + version
        return
    print '找到文件：' + key
    print '下载中...'
    run_cmd(['gdrive', 'download', key])
    print '下载完成'
    print '正在解压...'
    if cache:
        run_cmd(['7z', 'e', name, '-y', '-spf'])
        base_path = os.path.split(os.path.realpath(__file__))[0] + '/' + name[:-3]
        original_path = base_path + cache_file_path
        target_path = path + system + ' (' + version + ')' + cache_path
        run_cmd(['mkdir', '-p', target_path])
        run_cmd(['cp', '-rf', original_path, target_path])
        run_cmd(['rm', '-r', base_path])
    else:
        run_cmd(['7z', 'e', name, '-y', '-spf', '-o'+path])
    print '解压完成'


def usage():
    print("""
download_symbols.py [version] [option]
-h (--help)：显示帮助信息
-v (--version)：下载版本号
-c (--cache)：下载Cache版本
""")


def main():
    if len(sys.argv) == 2:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcv:", ["help", "cache", "version"])
    except getopt.GetoptError:
        print("argv error,please input")
        exit()

    version = ''
    cache = False
    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
            sys.exit()
        elif cmd in ("-c", "--cache"):
            cache = True
        elif cmd in ("-v", "--version"):
            version = arg
    download(version, cache=cache)

if __name__ == '__main__':
    main()
