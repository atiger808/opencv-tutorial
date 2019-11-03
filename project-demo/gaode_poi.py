# _*_ coding: utf-8 _*_
# @Time     : 2019/8/31 15:38
# @Author   : Ole211
# @Site     : 
# @File     : gaode_poi.py    
# @Software : PyCharm

'''
高德地图api接口
'''

import requests
from json import loads
import pandas as pd

KEY = '91971945901859e015eeb3850655f10f'
ak_2 = '3e4ae58aa9e8e3385e323084c3fcf9b4'
APIKEY = 'c9942476e78d0ce32f583af17729f3de'
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
'upgrade-insecure-requests':'1',
}

def getLocation(address):
    '''
    获取经纬度函数
    :param address:
    :return: 返回经纬度数据
    '''
    url = "http://restapi.amap.com/v3/geocode/geo?key={}&address={}".format(KEY, address)
    res = requests.get(url, headers=headers)
    res = loads(res.text)
    if res['status'] == '1':
        print(res)
        return res['geocodes'][0]['location']
    return None

def getLocation_2(address):
    '''
    获取经纬度函数
    :param address:
    :return: 返回经纬度数据
    '''
    data = {
        'key': APIKEY,
        'address': address
    }
    url = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(url, data, headers=headers)
    if res.status_code == 200:
        result = loads(res.text)
        return result['geocodes'][0]['location']
    return None

def calcDistance(origins, destination):
    '''
    计算两地距离函数
    :param origins: 起始位置经纬度
    :param destination: 目标位置经纬度
    :return: 两地距离
    '''
    url= 'http://restapi.amap.com/v3/distance'
    data = {
        'key':APIKEY,
        'origins': origins,
        'destination': destination
    }
    res = requests.get(url, data, headers=headers)
    if res.status_code == 200:
        result = loads(res.text)
        print(result)
        result = float(result['results'][0]['distance'])*1.0/1000
        return result
    return None

def gaodeAroundSearch(location, types, distance=5000):
    '''
    高德poi接口
    :param location:经纬度
    :param types: 周边服务类型
    :return: 返回周边服务
    '''
    url = 'https://restapi.amap.com/v3/place/around?key={}&location={}&radius={}&types={}'.format(APIKEY, location, distance, types)
    print(url)
    res = requests.get(url, headers=headers)
    result = loads(res.text)
    if result['status'] != '0':
        return result['pois']
    return None

def getStaticMap():
    url = 'https://restapi.amap.com/v3/staticmap?location=116.481485,39.990464&zoom=10&size=750*300&markers=mid,,A:116.481485,39.990464&key=<用户的key>'

def getWeather():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=<用户key>'

if __name__ == '__main__':
    # start = input('出发地：')
    # end = input('目的地：')
    # distance = calcDistance(getLocation(start), getLocation(end))
    # print(distance)
    types = ['学校', '购物中心', '超市', '银行', '写字楼', '餐饮',\
             '医院', '公园', '图书馆', '博物馆', '公交车站|地铁站']
    location = getLocation('杭州滨江区')
    print(location)
    res = gaodeAroundSearch(location, '足浴')
    if res:
        df = pd.DataFrame(res)
        df.loc[:, ['id', 'name', 'tel', 'distance', 'pname', 'cityname', 'adname', 'address']].to_csv('d:\\csv\\location.csv', encoding='utf-8')
        print(df.to_csv('d:\\csv\\poi.csv', encoding='utf-8'))
        print(df)
    else:
        print('None')