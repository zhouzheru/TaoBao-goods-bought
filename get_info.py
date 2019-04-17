from lxml import etree
import re
import requests
import time
import os
import csv
import json


def save_cookies():
    os.system("python get_cookies.py") #运行webdriver,获取cookies

    time.sleep(10)

    f = open("cookies.txt",'r')
    s=f.read()
    name = re.findall("\'name\': \'(.*?)\'",s,re.S)
    value  =re.findall("\'value\': \'(.*?)\'",s,re.S)

    list1 =[]
    for i in range(len(name)):
        list1.append("{0}={1}".format(name[i],value[i]))
    cookies = ';'.join(list1)
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
    # print(cookies)
    return cookies

def get_info(cookies,pageNum,prePageNo):
    url = "https://buyertrade.taobao.com/trade/itemlist/asyncBought.htm?action=itemlist/BoughtQueryAction&event_submit_do_query=1&_input_charset=utf8&sm"
    # 这里的URL 好像每个人都是相同的 如果不同，手动登录复制一下#
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'referer': url,
    }
    data = {'buyerNick': '',
    'dateBegin': '0',
     'dateEnd': '0',
     'lastStartRow': '',
      'logisticsService': '',
       'options': '0',
       'orderStatus': '',
        'pageNum': pageNum,
         'pageSize': '15',
          'queryBizType': '',
          'queryOrder': 'desc',
          'rateStatus': '',
           'refund': '',
           'sellerNick': '',
           'prePageNo': prePageNo}

    Session = requests.session()
    s = Session.post(url,headers=headers,data=data,cookies = cookies)
    text = s.text
    # print(text)
    content = json.loads(text)
    info_list = content.get("mainOrders")
    for each_info in info_list:
        item = {}
        status = each_info.get("statusInfo").get("text")
        if "关闭" not in status:  #过滤交易关闭的订单
            item["goods_id"] = each_info.get("extra").get("id")
            item["goods_time"] = each_info.get("orderInfo").get("createTime")
            item["goodes_title"] = each_info.get("subOrders")[0].get("itemInfo").get("title")
            item["goods_price"] = each_info.get("subOrders")[0].get("priceInfo").get("realTotal")
            yield item

def save_to_csv(item):
        with open("TaoBao.csv",'a',newline="") as f:
            writer  = csv.writer(f)
            for each in item:
                writer.writerow([each["goods_id"],each["goods_time"],each["goodes_title"],each["goods_price"]])

def main():
    cookies=save_cookies()

    for pageNum in range(1,47):
        prePageNo = pageNum-1
        s=get_info(cookies,pageNum,prePageNo)
        save_to_csv(s)
        print("第{}页已保存！".format(pageNum))
        time.sleep(5)  #设置5s 勉强不出现滑块验证。如果觉得慢自行修改






main()

