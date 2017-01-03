#coding=utf-8
import urllib
import urllib2

def print_list(list):
	for i in list:
	 print (i)

def demo():
	url = 'http://mobile.yangkeduo.com/goods.html?goods_id=1218219&is_spike=0&ts=1483424679878'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers ={"User-Agent":user_agent}
	request = urllib2.Request(url,headers = headers)
	retrieve(url, 'index.html')

def retrieve():
	url = 'http://www.qiushibaike.com/8hr/page/3'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers ={"User-Agent":user_agent}
	fname,msg = urllib.urlretrieve(url, 'index.html', headers = headers, reporthook=progress)
	print(fname)
	print_list(msg.items())

def progress(blk,blk_size,total_size):
	print('%d/%d - %.03f%%' % (blk*blk_size,total_size,(float)(blk*blk_size*100/total_size)))

if __name__ == '__main__':
	retrieve()