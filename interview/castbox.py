# -*- coding:utf-8 -*-

'''
假设nginx日志格式如下
71.92.220.155 2016-06-28:00:07:05 GET /feed?key=6489498cbd5b607ae5cb7e7d70b48a320cac5e3b HTTP/1.1 200 1008 "id=d5dcb1c45132eef4dbc3858903c0fbbc;lang=en;model=SAMSUNG-SM-G890A;brand=samsung;countryCode=US;country=United+States"

使用空格分隔，每个字段分别是<IP> <TIME> <GET/POST> <PATH> <HTTP VERSION> <HTTP CODE> <BODY SIZE> <EXTRA_HEADER>. 其中extra_header里面的id是用户的唯一标识.

要求编写程序:
1. 统计IP请求次数， 并且按照降序输出
2. 给定一天的nginx log, 计算DAU

'''

import re


def parse_log(logfile):
    '''
    parse logfile and return list of all IPs and all user ids.
    '''
    user_ids = []
    ips = []
    with open(logfile, 'r') as f:
        for line in f:
            ip = line.split()[0]
            id = re.split(';|=', line.split()[7])[1]
            ips.append(ip)
            user_ids.append(id)
    return user_ids, ips


def get_DAU(ids_in_one_day):
    print 'DAU is ', len(set(ids_in_one_day))


def get_ip_request_nums(ips):
    '''
    print ip request numbers in descending order
    '''
    records = {}
    for i in ips:
        records[i] = records.get(i, 0) + 1
    result = sorted(records.iteritems(), key=lambda x: x[1], reverse=True)
    print '\n'.join(['%s\t%s' %(i, j) for i, j in result])


if __name__ == '__main__':
    # ips_sample = ['71.92.220.155', '71.92.220.155', '71.92.220.154']
    # get_ip_request_nums(ips_sample)
    # ids_sample = ['12', '13', '12']
    # get_DAU(ids_sample)
    input_file = raw_input('input your logfile >')
    ids, ips = parse_log(input_file)
    get_ip_request_nums(ips)
    get_DAU(ids)


