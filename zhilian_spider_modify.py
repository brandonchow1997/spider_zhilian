import requests
import urllib
import re
import pymongo

# 最大爬取页数
MAX_PAGE = 300

def get_page(page):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453'
    }
    # 构造参数
    # 可更改
    data = {
        'pageSize': '60',
        # 城市ID 可更改
        'cityId': '636',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        # 可更改参数
        'kw': '爬虫',
        'kt': '3',
        # 可更改参数
        'lastUrlQuery': '{"p":2,"jl":"489","sf":"2001","st":"4000","kw":"爬虫","kt":"3"}',
        '': '2001'
    }
    print('正在爬取第', page, '页')
    url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(page*60-60) + '&' + urllib.parse.urlencode(data)
    response = requests.get(url, headers=header)
    return response.json()


def parse(html):
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
        save_to_mongo(jobs)

# 连接到MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'spider_zhilian'
MONGO_COLLECTION = 'spider_jobs'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]




def save_to_mongo(data):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
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
        print('-'*100)
