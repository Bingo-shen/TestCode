#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

'''
注意：定义类的时候，内部方法之间的互调
步骤：
1.按照流的方式进行下载
2.存储在某个文件中
'''
import requests
import shutil
import time

class DownLoadFile():

    def readyDatas(self):
        '''
        准备数据：固定参数
        :param datas 接口参数
        :param downLoadPath 下载文件地址
        '''
        times = time.strftime("%Y-%m_%d %H_%M_%S", time.localtime(time.time()))

        self.datas = {"username":"lyfadmin","password":"liuhaijun123456","type":1}
        self.downLoadPath = '/Users/apple/Documents/TestCode/tryApiTest/requestsPractice/Files{0}.xlsx'.format(times)

        return self.datas,self.downLoadPath

    def getHearders(self):
        '''
        :return: Hearders 接口报文的头信息
        '''
        self.Hearders = {'Content-Type':'application/json;charset=UTF-8','Referer':'http://lyfadmin.edu.laiyifen.com/plugins/platform-include/views/login.html',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
        return  self.Hearders

    def setSession(self):
        '''
        :return: SessionId 返回网址的Session信息
        '''
        self.readyDatas()
        self.getHearders()
        self.sessionId = requests.Session()
        self.sessionId.post(url='http://lyfadmin.edu.laiyifen.com/ouser-web/mobileLogin/login.do',
                                  json = self.datas,
                                  headers = self.Hearders)
        return self.sessionId

    def downFiles(self):
        '''
        下载文件
        '''
        self.setSession()
        loginStatus = self.sessionId.get('http://lyfadmin.edu.laiyifen.com/promotion-static/template/coupon.xlsx',
                                         headers = self.Hearders,
                                         stream = True )
        if loginStatus.status_code == 200:
            with open(self.downLoadPath,'wb') as files:
                '''Function1'''
                # for chunk in loginStatus.iter_content(chunk_size=1024):
                #     files.write(chunk)
                '''function2'''
                loginStatus.raw.decode_content = True
                shutil.copyfileobj(loginStatus.raw, files)
            print('file download succeed')
        else:
            print('file download failed')


if __name__ == '__main__':
    DownLoadFile = DownLoadFile()
    DownLoadFile.downFiles()