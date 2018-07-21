# -*- coding： utf-8 -*-
# author：pengr

import requests
import time
import lxml
import json
import pymongo

# 最大爬取页数
MAX_PAGE = 100
"""
def get01():
    header = {
        'Cookie': 'urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti1; adfcid2=pzzhubiaoti1; adfbid=0; adfbid2=0; sts_deviceid=164b708c726141-0b5a721fc-3b444329-1049088-164b708c729a9; sts_sg=1; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fs%3Ftn%3D25017023_5_dg%26ch%3D1%26ie%3DUTF-8%26wd%3Dzhilianzhaopin; dywez=95841923.1532079163.3.3.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=zhilianzhaopin; __xsptplus30=30.1.1532079163.1532079163.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23M1CLi7jG6OM2mDiY8ntZv60N-ySC4BGh%23; __utmt=1; _jzqy=1.1526643282.1532079164.2.jzqsr=baidu.jzqsr=baidu|jzqct=zhilianzhaopin; _jzqckmp=1; qrcodekey=b0d72e663d784ceeb83d1db22b23aeda; _jzqa=1.2278863967071744800.1515904529.1526643282.1532079164.3; _jzqc=1; _jzqb=1.2.10.1532079164.1; firstchannelurl=https%3A//passport.zhaopin.com/login%3Fy7bRbP%3DdpodqL8ofg8ofg8oScnqZCnf748SEa5JdFDBb8XLuLQ; lastchannelurl=https%3A//passport.zhaopin.com/login; JsNewlogin=2123451650; JSloginnamecookie=13500732402; JSShowname=%E6%AD%A6%E7%91%9E%E9%B9%8F; at=15f0f1390d9c48d2b334f47174d1cf8e; Token=15f0f1390d9c48d2b334f47174d1cf8e; rt=b90230de76944924ae3ae9a1a6953571; JSsUserInfo=3d692e695671407155775e75516a557547775a695b695d714c7129772775546a557543775d695a695b71407156775b755d6a5475427753693f6925714a71031c370126f45f753577256957691b7112710b770e751b6a117519775d695f695e71427150772975586a527543774669096904711a715e773a753d6a5975417753692b693f714a71537744755c6a447541775f695069587144715e772875256a5975407753693f692a714a712f772575596a5375487759695d695971467153775e75526a3175247755695b69507124712c775475586a5f7525773869246956710771007707750e6a1675057701695f695e71427150775c75296a557546775b69446908711871087752756; uiioit=3b622a6459640f644764406a506e536e536456385577527751682c622a64596408644c646; dywea=95841923.3780843914165976000.1515904529.1526643281.1532079163.3; dywec=95841923; dywem=95841923.y; dyweb=95841923.3.10.1532079163; __utma=269921210.47306283.1515904529.1526643282.1532079164.3; __utmb=269921210.3.10.1532079164; __utmc=269921210; __utmz=269921210.1532079164.3.3.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=zhilianzhaopin; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1532079164; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1532079455; sts_evtseq=16; sts_sid=164b708c7312e3-0cae6079e-3b444329-1049088-164b708c732a8; ZP_OLD_FLAG=false; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; GUID=4833c4700857470ba3af93383fe4e817; ZL_REPORT_GLOBAL={%22//i%22:{%22actionIdFromI%22:%22b900c1f6-9ccc-4d87-9ab0-ff540a80a7f2-i%22}%2C%22sou%22:{%22actionIdFromSou%22:%22a95383de-4500-4c38-b773-576e1480a36e-sou%22%2C%22funczone%22:%22smart_matching%22}}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453'
    }

    url = 'https://sou.zhaopin.com/?p=2&jl=489&sf=2001&st=4000&kw=%E7%88%AC%E8%99%AB&kt=3'

    response = requests.get(url, headers=header)

    print(response.status_code)

    print(response.text[:1000])
"""


def get_page(page):
    header = {
        'Cookie': 'urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti1; adfcid2=pzzhubiaoti1; adfbid=0; adfbid2=0; sts_deviceid=164b708c726141-0b5a721fc-3b444329-1049088-164b708c729a9; sts_sg=1; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fs%3Ftn%3D25017023_5_dg%26ch%3D1%26ie%3DUTF-8%26wd%3Dzhilianzhaopin; dywez=95841923.1532079163.3.3.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=zhilianzhaopin; __xsptplus30=30.1.1532079163.1532079163.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23M1CLi7jG6OM2mDiY8ntZv60N-ySC4BGh%23; __utmt=1; _jzqy=1.1526643282.1532079164.2.jzqsr=baidu.jzqsr=baidu|jzqct=zhilianzhaopin; _jzqckmp=1; qrcodekey=b0d72e663d784ceeb83d1db22b23aeda; _jzqa=1.2278863967071744800.1515904529.1526643282.1532079164.3; _jzqc=1; _jzqb=1.2.10.1532079164.1; firstchannelurl=https%3A//passport.zhaopin.com/login%3Fy7bRbP%3DdpodqL8ofg8ofg8oScnqZCnf748SEa5JdFDBb8XLuLQ; lastchannelurl=https%3A//passport.zhaopin.com/login; JsNewlogin=2123451650; JSloginnamecookie=13500732402; JSShowname=%E6%AD%A6%E7%91%9E%E9%B9%8F; at=15f0f1390d9c48d2b334f47174d1cf8e; Token=15f0f1390d9c48d2b334f47174d1cf8e; rt=b90230de76944924ae3ae9a1a6953571; JSsUserInfo=3d692e695671407155775e75516a557547775a695b695d714c7129772775546a557543775d695a695b71407156775b755d6a5475427753693f6925714a71031c370126f45f753577256957691b7112710b770e751b6a117519775d695f695e71427150772975586a527543774669096904711a715e773a753d6a5975417753692b693f714a71537744755c6a447541775f695069587144715e772875256a5975407753693f692a714a712f772575596a5375487759695d695971467153775e75526a3175247755695b69507124712c775475586a5f7525773869246956710771007707750e6a1675057701695f695e71427150775c75296a557546775b69446908711871087752756; uiioit=3b622a6459640f644764406a506e536e536456385577527751682c622a64596408644c646; dywea=95841923.3780843914165976000.1515904529.1526643281.1532079163.3; dywec=95841923; dywem=95841923.y; dyweb=95841923.3.10.1532079163; __utma=269921210.47306283.1515904529.1526643282.1532079164.3; __utmb=269921210.3.10.1532079164; __utmc=269921210; __utmz=269921210.1532079164.3.3.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=zhilianzhaopin; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1532079164; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1532079455; sts_evtseq=16; sts_sid=164b708c7312e3-0cae6079e-3b444329-1049088-164b708c732a8; ZP_OLD_FLAG=false; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; GUID=4833c4700857470ba3af93383fe4e817; ZL_REPORT_GLOBAL={%22//i%22:{%22actionIdFromI%22:%22b900c1f6-9ccc-4d87-9ab0-ff540a80a7f2-i%22}%2C%22sou%22:{%22actionIdFromSou%22:%22a95383de-4500-4c38-b773-576e1480a36e-sou%22%2C%22funczone%22:%22smart_matching%22}}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453'
    }

#构造参数
    """
    data = {
        'pageSize': '60',
        'cityId': '489',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kw': '爬虫',
        'kt': '3',
        'lastUrlQuery': '{"p":2,"jl":"489","sf":"2001","st":"4000","kw":"爬虫","kt":"3"}',
        '': '2001'
    }
    """
    print('正在爬取第', page, '页')
    url = "https://fe-api.zhaopin.com/c/i/sou?start=" + str(page * 60) + "&pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%88%AC%E8%99%AB&kt=3&lastUrlQuery=%7B%22jl%22:%22489%22,%22kw%22:%22%E7%88%AC%E8%99%AB%22,%22kt%22:%223%22%7D"
    response = requests.get(url, headers=header)

    # print(response.status_code)

    # print(response.text[:1000])

    # return response.text
    # requests请求的response数据如果是json数据，可以用response.json()进行转化为字典对象
    return response.json()


def parse(html):
    # data = json.loads(data)
    # print(data)
    # 观察数据结构可得
    data = html['data']['results']
    for item in data:
        jobs = {
            'jobName': item['jobName'],
            'salary': item['salary'],
            'company_name': item['company']['name'],
            'emplType': item['emplType'],
            'workingExp': item['workingExp']['name']
        }
        print(jobs)
        """
        print('\t|  '.join(
            [item['jobName'], item['salary'], item['company']['name'], item['emplType'], item['workingExp']['name'],
             item['eduLevel']['name']]))
        print('-' * 120)
        """
        save_to_mongo(jobs)


MONGO_URL = 'localhost'
MONGO_DB = 'spider_zhilian'
MONGO_COLLECTION = 'jobs'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


def save_to_mongo(result):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


if __name__ == '__main__':
    # ------------ 获取数据 ---------------
    # get01()
    # get_page()
    for i in range(1, MAX_PAGE + 1):
        html = get_page(i)
    # ------------ 解析数据 ---------------
        parse(html)
        time.sleep(4)


