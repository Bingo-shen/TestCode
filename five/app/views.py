from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

import  requests
import  json
from pyecharts import  Bar

def index(request):
	return HttpResponse('<h2><center>Hello WuYa！</center></h2>')


def douBan(request):
	movies=[]
	for i in range(20):
		r=requests.get('https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20')
		title=r.json()['subjects'][i]['title']
		rate=r.json()['subjects'][i]['rate']
		url=r.json()['subjects'][i]['url']
		cover=r.json()['subjects'][i]['cover']
		movies.append({
			'title':title,
			'rate':rate,
			'url':url,
			'cover':cover
		})
	return render(request,'laGou.html',locals())



from pyecharts import Bar

def douBan():
	movies=[]
	for i in range(20):
		r=requests.get('https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20')
		title=r.json()['subjects'][i]['title']
		rate=r.json()['subjects'][i]['rate']
		movies.append({
			'title':title,
			'rate':rate
		})
	titles=list(map(lambda x:x['title'],movies))
	rates =list(map(lambda x: x['rate'], movies))
	titleRates=[]
	for rate in rates:
		titleRates.append(int(float(rate)))
	bar=Bar('豆瓣电影评分数据分析')
	bar.use_theme('dark')
	bar.add('豆瓣电影',titles,titleRates,is_more_utils=True)
	bar.render('douban.html')


douBan()



















# def laGou(request):
# 	positions = []
# 	r=requests.post(
# 		url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
# 		data={'first':False,'pn':2,'kd':'自动化测试'},headers=headers())
# 	for  i in range(15):
# 		company=r.json()['content']['positionResult']['result'][i]['companyFullName']
# 		salary=r.json()['content']['positionResult']['result'][i]['salary']
# 		positions.append({
# 			'company': company,
# 			'salary': salary
# 		})
# 	print(positions)
#
# 	return render(request,'laGou.html',locals())


# def laGou():
# 	salarys=[]
# 	companys=[]
# 	listMin=[]
# 	listMax=[]
# 	r=requests.post(
# 		url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
# 		data={'first':False,'pn':2,'kd':'自动化测试工程师'},headers=headers())
# 	for  i in range(15):
# 		company=r.json()['content']['positionResult']['result'][i]['companyFullName']
# 		salary=r.json()['content']['positionResult']['result'][i]['salary']
# 		companys.append(company)
# 		salarys.append(salary)
# 	for item in salarys:
# 		listMin.append(int(str(item.split('-')[0]).split('k')[0]))
#
# 	bar=Bar('拉钩网平台薪资分析')
# 	bar.add('薪资分析',companys,listMin,is_legend_show=True)
# 	bar.render('aa.html')


from pyecharts import  Bar

# def dataAnalysis():
# 	positions=[]
# 	data=json.load(open('lagou.json','r'))
# 	#获取招聘职位公司名称
# 	for i in range(15):
# 		company = data['content']['positionResult']['result'][i]['companyFullName']
# 		salary = data['content']['positionResult']['result'][i]['salary']
# 		positions.append({
# 			'company':company,
# 			'salary':salary
# 		})
# 	company=list(map(lambda x:x['company'],positions))
# 	salary=list(map(lambda x:x['salary'],positions))
# 	salaryMax=[]
# 	# 获取最高薪资
# 	for item in salary:
# 		salaryMax.append(int(str(item.split('-')[1]).split('k')[0]))
# 	bar=Bar('招聘平台薪资数据分析')
# 	bar.use_theme('dark')
# 	bar.add('薪资分析',company,salaryMax,is_legend_show=True)
# 	bar.render('lagou.html')
