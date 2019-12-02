#!/use/bin/env python
#coding:utf-8
#Author:shenqiang

import  requests

'''传递的数据'''
data={
	"upload":"提交",
	"__channel":"renren",
	"privacyParams":'{"sourceControl": 99}',
	'hostid':'967004081',
	'requestToken':'-1124080368',
	'_rtk':'88c0e36a'}

'''上传文件的'''
files = {"file":
	        ("11.jpg", open("/Users/apple/Desktop/11.jpg", "rb"), "image/jpeg",{})}


'''hearders'''
headers={'Conteny-Type':'multipart/form-data',
         'Cookie':'wp_fold=0; jebe_key=2ebfe84a-ba39-4685-a7d4-2c2554a2c332%7Caa130ffbb5d8cc8d315a4ab7b5b427ae%7C1574763933779%7C1%7C1574763934663; jebecookies=bdca1d47-b697-4140-a2e0-ac30c4a5b558|||||; loginfrom=null; ver=7.0; WebOnLineNotice_972956233=1; XNESSESSIONID=abbe86d381c3; id=972956233; societyguester=0b0dfda34622b4fdc5f63d33bc8bbae53; t=0b0dfda34622b4fdc5f63d33bc8bbae53; xnsid=58c37e4b; ick=0a1287c1-023e-4868-bd07-bb96efea9185; ick_login=34b7eeb3-51ed-4d82-9c49-37d953b00269; __utma=151146938.1362702986.1574763700.1574763700.1574763700.1; __utmb=151146938.3.10.1574763700; __utmc=151146938; __utmz=151146938.1574763700.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; _de=199FB1745CB4DC6D74D4674661EB8018; _r01_=1; anonymid=k3fpklmh-s0sajh; depovince=ZGQT',
         'User-Aaent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

'''文件上传'''
r=requests.post(
	url='http://head2.upload.renren.com/head2/UploadFacade.do?pagetype=customheadupload&hostid=972956233&uploadid=1574764014376',
	data=data,
	headers=headers,
	files=files)

'''上传状态和文本内容'''
print(r.status_code)
print(r.text)
