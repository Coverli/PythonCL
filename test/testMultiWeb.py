import requests # 爬虫模块,获取网页文本

def gettext(gender):
	for i in range(1, gender+1):
		r = requests.get('https://www.readnovel.com/all?gender=%d&catId=-1' %i)
		r.encoding = 'apparent_encoding' # apparent_encoding 根据网页自动分析编码并使用
		return r.text
		name = '%d.html' %i
		print(file=open(name,'x',encoding='utf-8'))
    

gettext(2)
# url = 'https://music.163.com/#/search/m/?s=%E6%B8%85%E6%99%A8%E6%97%A5%E6%9A%AE&type=1' 
# 把 'https://music.163.com/#/search/m/?s=%E6%B8%85%E6%99%A8%E6%97%A5%E6%9A%AE&type=1' 改成需要爬取的网站网址
# name = '1.html' 
# 输出html文件

# print(gettext(url),file=open(name,'x',encoding='utf-8'))