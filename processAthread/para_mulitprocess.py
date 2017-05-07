# -*- coding:utf-8 -*-

import time
import subprocess
from functools import wraps
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from collections import namedtuple


def timecount(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print '%s' %(end - start)
        return ret
    return wrapper

def run_command(cmd):
    # print 'I am in %s' % cmd
    child = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = child.communicate()
    rc = child.returncode
    # print 'I am out %s' % cmd
    return cmd, out, err, rc

@timecount
def site_node_check_subprocess():
    '''run into error when just use subprocess to run in concrrency way
    '''

    site_version_cmd = ["nimbula-api", "-f", "json", "get", "siteinformation", "-u", "/root/root", "-a", "http://10.128.94.201", "-p", "password"]
    nodes_num_cmd = ["nimbula-admin", "list", "node", "/", "-Fendpoint,status", "-u", "/root/root", "-a", "http://10.128.94.201", "-p", "password"]
    nodes_version_cmd = ["nimbula-exec", "-c", "cat /etc/nimbula_version", "-a", "http://10.128.94.201", "-p", "password", "--nodepass", "password"]

    cmds = [site_version_cmd, nodes_num_cmd, nodes_version_cmd]
    cmd_result = namedtuple("cmd_result", ["cmd", "out", "err", "code"])
    result = {}
    result_keys = ['site_version_result', 'nodes_num_result', 'nodes_num_result']
    childs = []
    for cmd in cmds:
        child = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        childs.append(child)
    // error : ValueError: I/O operation on closed file
    for cmd, child, key in zip(cmds, childs, result_keys):
        result[key] = cmd_result(cmd, child.communicate()[0], child.communicate()[1], child.returncode)

    print result['site_version_result'].out


@timecount
def site_node_check():
    result = []
    cmd_result = namedtuple("cmd_result", ["cmd", "out", "err", "code"])
    pool = Pool(3)
    site_version_cmd = ["nimbula-api", "-f", "json", "get", "siteinformation", "-u", "/root/root", "-a", "http://10.128.94.201", "-p", "password"]
    nodes_num_cmd = ["nimbula-admin", "list", "node", "/", "-Fendpoint,status", "-u", "/root/root", "-a", "http://10.128.94.201", "-p", "password"]
    nodes_version_cmd = ["nimbula-exec", "-c", "cat /etc/nimbula_version", "-a", "http://10.128.94.201", "-p", "password", "--nodepass", "password"]
    cmds = [site_version_cmd, nodes_num_cmd, nodes_version_cmd ]
    for cmd in cmds:
        result.append(pool.apply_async(run_command, (cmd,)))
    pool.close()
    pool.join()
    # use _make to generate a namedtuple object with iterable
    site_version_result = cmd_result._make(result[0].get())
    nodes_num_result = cmd_result._make(result[1].get())
    nodes_version_result = cmd_result._make(result[2].get())

    print site_version_result.out


@timecount
def site_node_check_thread():
    result = []
    cmd_result = namedtuple("cmd_result", ["cmd", "out", "err", "code"])
    pool = ThreadPool(3)
    site_version_cmd = ["nimbula-api", "-f", "json", "get", "siteinformation",
                        "-u", "/root/root", "-a", "http://10.128.94.201", "-p",
                        "password"]
    nodes_num_cmd = ["nimbula-admin", "list", "node", "/", "-Fendpoint,status",
                     "-u", "/root/root", "-a", "http://10.128.94.201", "-p",
                     "password"]
    nodes_version_cmd = ["nimbula-exec", "-c", "cat /etc/nimbula_version", "-a",
                         "http://10.128.94.201", "-p", "password", "--nodepass",
                         "password"]
    cmds = [site_version_cmd, nodes_num_cmd, nodes_version_cmd]
    for cmd in cmds:
        result.append(pool.apply_async(run_command, (cmd,)))
    pool.close()
    pool.join()
    # use _make to generate a namedtuple object with iterable
    site_version_result = cmd_result._make(result[0].get())
    nodes_num_result = cmd_result._make(result[1].get())
    nodes_version_result = cmd_result._make(result[2].get())

    print site_version_result.out

site_node_check()
site_node_check_thread()
site_node_check_subprocess()