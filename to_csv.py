import pymongo
import pandas as pd


def to_csv_wuxi():
    client = pymongo.MongoClient('localhost')
    cur = client["zhilian_jobs"]["wuxi_jobs"]
    data = pd.DataFrame(list(cur.find()))
    del data["_id"]
    del data["截止时间"]
    del data["招聘链接"]
    del data["福利"]
    # 存储的时候可以做一些数据清洗的工作,清洗脏数据
    data.to_csv("wuxi_jobs.csv")


def to_csv_suzhou():
    client = pymongo.MongoClient('localhost')
    cur = client["zhilian_jobs"]["suzhou_jobs"]
    data = pd.DataFrame(list(cur.find()))
    del data["_id"]
    del data["截止时间"]
    del data["招聘链接"]
    del data["福利"]
    # 存储的时候可以做一些数据清洗的工作,清洗脏数据
    data.to_csv("suzhou_jobs.csv")


def to_csv_shanghai():
    client = pymongo.MongoClient('localhost')
    cur = client["zhilian_jobs"]["shanghai_jobs"]
    data = pd.DataFrame(list(cur.find()))
    del data["_id"]
    del data["截止时间"]
    del data["招聘链接"]
    del data["福利"]
    # 存储的时候可以做一些数据清洗的工作,清洗脏数据
    data.to_csv("shanghai_jobs.csv")


if __name__ == '__main__':
    to_csv_wuxi()
    to_csv_suzhou()
    to_csv_shanghai()