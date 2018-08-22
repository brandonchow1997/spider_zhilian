# -*- coding： utf-8 -*-
# author:brandonchow1997
# email:136269209@qq.com
# date:2018-8-22 15:35
import requests
import urllib
from fake_useragent import UserAgent
import re
import pymongo
import time

"""
def get_page():
    get_page_wuxi()
    get_page_suzhou()
    get_page_shanghai()
"""


def get_page_wuxi(page):
    # 伪装浏览器
    ua = UserAgent()
    header = {
        'User-Agent': ua.random
    }
    # 构造参数 无锡 cityID 636
    data = {
        'pageSize': '60',
        'cityId': '636',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kt': '3',
        'lastUrlQuery': '{"jl": "636"}'
    }
    print('正在爬取第', page+1, '页')
    url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(page*60) + '&' + urllib.parse.urlencode(data)
    response = requests.get(url, headers=header)
    return response.json()


def get_page_suzhou(page):
    ua = UserAgent()
    header = {
        'User-Agent': ua.random
    }
    # 构造参数 苏州 cityID 639
    data = {
        'pageSize': '60',
        'cityId': '639',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kt': '3',
        'lastUrlQuery': '{"jl": "639"}'
    }
    print('正在爬取第', page+1, '页')
    url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(page*60) + '&' + urllib.parse.urlencode(data)
    response = requests.get(url, headers=header)
    return response.json()


def get_page_shanghai(page):
    ua = UserAgent()
    header = {
        'User-Agent': ua.random
    }
    # 构造参数 上海 cityID 538
    data = {
        'pageSize': '60',
        'cityId': '538',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kt': '3',
        'lastUrlQuery': '{"jl": "538"}'
    }
    print('正在爬取第', page+1, '页')
    url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(page*60) + '&' + urllib.parse.urlencode(data)
    response = requests.get(url, headers=header)
    return response.json()


def parse_wuxi(html):
    # data = json.loads(data)
    # print(data)
    # 观察数据结构可得
    data = html['data']['results']
    # 取工资均值
    for item in data:
        pattern = re.compile('\d+')
        salary = item['salary']
        if salary != '薪资面议':
            res = re.findall(pattern, salary)
            avg = 0
            sum = 0
            for i in res:
                a = int(i)
                sum = sum + a
                avg = sum / 2
        else:
            # 薪资面议取5k
            avg = 5.0

        jobs = {
            '职位名称': item['jobName'],
            '薪资': item['salary'],
            'int薪资': avg,
            '公司名称': item['company']['name'],
            '工作城市': item['city']['display'],
            '工作经历要求': item['workingExp']['name'],
            '学历要求': item['eduLevel']['name'],
            '福利': item['welfare'],
            '截止时间': item['endDate'],
            '招聘链接': item['positionURL']
        }
        print(jobs)
        save_to_mongo_wuxi(jobs)


def parse_suzhou(html):
    # data = json.loads(data)
    # print(data)
    # 观察数据结构可得
    data = html['data']['results']
    # 取工资均值
    for item in data:
        pattern = re.compile('\d+')
        salary = item['salary']
        if salary != '薪资面议':
            res = re.findall(pattern, salary)
            avg = 0
            sum = 0
            for i in res:
                a = int(i)
                sum = sum + a
                avg = sum / 2
        else:
            # 薪资面议取5k
            avg = 5.0

        jobs = {
            '职位名称': item['jobName'],
            '薪资': item['salary'],
            'int薪资': avg,
            '公司名称': item['company']['name'],
            '工作城市': item['city']['display'],
            '工作经历要求': item['workingExp']['name'],
            '学历要求': item['eduLevel']['name'],
            '福利': item['welfare'],
            '截止时间': item['endDate'],
            '招聘链接': item['positionURL']
        }
        print(jobs)
        save_to_mongo_suzhou(jobs)


def parse_shanghai(html):
    # data = json.loads(data)
    # print(data)
    # 观察数据结构可得
    data = html['data']['results']
    # 取工资均值
    for item in data:
        pattern = re.compile('\d+')
        salary = item['salary']
        if salary != '薪资面议':
            res = re.findall(pattern, salary)
            avg = 0
            sum = 0
            for i in res:
                a = int(i)
                sum = sum + a
                avg = sum / 2
        else:
            # 薪资面议取5k
            avg = 5.0

        jobs = {
            '职位名称': item['jobName'],
            '薪资': item['salary'],
            'int薪资': avg,
            '公司名称': item['company']['name'],
            '工作城市': item['city']['display'],
            '工作经历要求': item['workingExp']['name'],
            '学历要求': item['eduLevel']['name'],
            '福利': item['welfare'],
            '截止时间': item['endDate'],
            '招聘链接': item['positionURL']
        }
        print(jobs)
        save_to_mongo_shanghai(jobs)

"""
# 连接到MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'zhilian_jobs'
MONGO_COLLECTION = 'city_jobs'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


def save_to_mongo(data):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')
"""

# 配置并存入wuxi_jobs表中
def save_to_mongo_wuxi(data):
    # 连接到MongoDB
    MONGO_URL = 'localhost'
    MONGO_DB = 'zhilian_jobs'
    MONGO_COLLECTION = 'wuxi_jobs'
    client = pymongo.MongoClient(MONGO_URL, port=27017)
    db = client[MONGO_DB]
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


# 配置并存入suzhou_jobs表中
def save_to_mongo_suzhou(data):
    # 连接到MongoDB
    MONGO_URL = 'localhost'
    MONGO_DB = 'zhilian_jobs'
    MONGO_COLLECTION = 'suzhou_jobs'
    client = pymongo.MongoClient(MONGO_URL, port=27017)
    db = client[MONGO_DB]
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


# 配置并存入shanghai_jobs表中
def save_to_mongo_shanghai(data):
    # 连接到MongoDB
    MONGO_URL = 'localhost'
    MONGO_DB = 'zhilian_jobs'
    MONGO_COLLECTION = 'shanghai_jobs'
    client = pymongo.MongoClient(MONGO_URL, port=27017)
    db = client[MONGO_DB]
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


def main(MAX_PAGE):
    # ------------ 获取数据 ---------------
    # get_page_wuxi()
    for i in range(0, MAX_PAGE):
        html = get_page_wuxi(i)
        # ------------ 解析数据 ---------------
        parse_wuxi(html)
        print('-' * 100)
    print('==' * 60)

    # get_page_suzhou()
    for i in range(0, MAX_PAGE):
        html = get_page_suzhou(i)
        # ------------ 解析数据 ---------------
        parse_suzhou(html)
        print('-' * 100)
    print('==' * 60)

    # get_page_shanghai()
    for i in range(0, MAX_PAGE):
        html = get_page_shanghai(i)
        # ------------ 解析数据 ---------------
        parse_shanghai(html)
        print('-' * 100)
    print('==' * 60)


if __name__ == '__main__':
    # 最大爬取页数
    main(MAX_PAGE=2000)
    # 每页一秒间隔时间，防止被封ip