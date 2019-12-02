#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
import requests

class filesHeader(object):
    '''文件传输头'''
    def fileHeader(self):
        sessionId = requests.Session
        headers = {'Accept':'application/json',
                   'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryNicLzxIDDIWaxMKM',
                   'Referer':'http://lyfadmin.edu.laiyifen.com/cms/h5-editor.html?platForm=2&pageId=1007099501000011&themeId=1&pageType=16&mode=1',
                   'Cookie':'ut=40279d073a3144ca84bef53a82c95cbb'
                   }
        return sessionId,headers

    '''data数据'''
    def datas(self):
        data = {}
        return data

    '''file数据'''
    def files(self):
        file = {'Filedata':
                    ('全渠道效果图.png',open('/Users/apple/Documents/罗马项目/营销域-主测试/全渠道效果图.png','rb'),'image/png',{})}
        return file


class upLoadFiles(filesHeader):

    def upLoadFilesPost(self):
        r = requests.post(url='http://lyfadmin.edu.laiyifen.com/cms/file/uploadFile.do',    data=filesHeader.datas(),headers=filesHeader.fileHeader())
        # print(r)

# if __name__ == '__main__':
#     upLoadFiles = upLoadFiles()
#     upLoadFiles.upLoadFilesPost()






