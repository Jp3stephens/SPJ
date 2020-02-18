from companyList import companyList
from company import Company
from people import People
import tweepy
import time





consumer_key = "h6oRWbbU7vHdVsby5AbJLUVdA"
consumer_secret = "d7d3ImS9Xt3AoxNURyTpcMoEOKVHnGjg2VMiDBf1zBiSeS7uC0"
access_token = "1130974963777789952-xGTpl06qV9QwkjjBdYZnkg105YxcNV"
access_token_secret = "5xfQkGRzPnKoRaZZ6CuaLKRy1Llm6TTDg4kR9Sf0tIeLT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api  = tweepy.API(auth,  wait_on_rate_limit=True)


def checkIfSubstring(string, sub_str):
	if  (len(sub_str) >  len(string)):
		temp = sub_str
		sub_str = string
		string = temp
	if (string.find(sub_str) == -1):
		return False
	else:
		return True
	








for company in companyList:
	try:
		acomp = api.get_user(id=company.company_name)
		if checkIfSubstring(acomp.name, acomp.screen_name):
			print("Valid company")
			company.addWebsite(acomp.url)
			print("Website being added: ", acomp.url)
		else:
			print("phony company")

			
	except BaseException as e: 
		print('failed on_status,', str(e))
		time.sleep(2)






