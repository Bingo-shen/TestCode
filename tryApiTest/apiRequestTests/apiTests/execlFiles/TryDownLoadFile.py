#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
import json
import requests
'''高级文件操作'''
import shutil
'''
1.按照流的方式进行下载
2.下载好后写入文件中
'''

data={"username":"lyfadmin","password":"liuhaijun123456","type":1}
download_path = '/Users/apple/PycharmProjects/apiRequestTests/apiTests/execlFiles/loadTest2.xlsx'

def gitHeaders():
    headers = {'Content-Type':'application/json;charset=UTF-8','Referer':'http://lyfadmin.edu.laiyifen.com/plugins/platform-include/views/login.html'}
    return headers

'''登陆return cookies'''
def  urlTest():
    '''实例化session对象'''
    sessionID = requests.Session()
    '''直接调用session'''
    sessionID.post(url='http://lyfadmin.edu.laiyifen.com/ouser-web/mobileLogin/login.do',
                      data=json.dumps(data),
                      headers=gitHeaders()
                      )
    return sessionID

'''调用session'''
def getUrlTest():
    get = urlTest().get(url='http://lyfadmin.edu.laiyifen.com/guide/getBackGuideSetting.do')
    return get

def getsession():
    Headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    return Headers

# getSession = getSession()
# print(getSession().getsession(),type(getSession().getsession()))

# '''文件下载方法1'''
# def getCouponFile():
#     '''调用下载文件的接口'''
#     getCouponFile = urlTest().get('http://lyfadmin.edu.laiyifen.com/promotion-static/template/coupon.xlsx',headers=getsession(),stream=True)
#
#     '''判断是否请求成功'''
#     if getCouponFile.status_code == 200:
#         '''以write权限open文件'''
#         with open(download_path,'wb') as file:
#             '''以1kb写入下载内容'''
#             for chunk in getCouponFile.iter_content(chunk_size=1024):
#                 file.write(chunk)
#     return

'''文件下载方法2'''
def downloadCouponFile():
    '''调用下载文件的接口'''
    getCouponFile = urlTest().get('http://lyfadmin.edu.laiyifen.com/promotion-static/template/coupon.xlsx',headers=getsession(),stream=True)

    '''判断是否请求成功'''
    if getCouponFile.status_code == 200:
        '''以write权限open文件'''
        with open(download_path,'wb') as file:
            '''以1kb写入下载内容'''
            getCouponFile.raw.decode_content = True
            shutil.copyfileobj(getCouponFile.raw,file)
    return

downloadCouponFile()





