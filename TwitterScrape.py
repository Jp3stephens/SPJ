from companyList import companyList, company_Text_List
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
	if (string.lower().find(sub_str.lower()) == -1):
		return False
	else:
		return True
	




def findCompanyTwitter(companyList):
	companies_Without_Twitter = companyList
	for company in companyList:
		try:
			acomp = api.get_user(id=company.company_name.replace(" ", ""))
			print("company name with spaces removed: ", company.company_name.replace(" ", ""))
			if checkIfSubstring(acomp.name.replace(" ",  ""), acomp.screen_name):
				print("Valid company")
				company.addWebsite(acomp.url)
				print("Website being added: ", acomp.url)
				company.addSocialMedia("Twitter", "@"+acomp.screen_name)
				company.addLocation(acomp.location)
				company.printCompanyInfo()
				companies_Without_Twitter.remove(company)
				continue 
			elif(findBCompanyTwitter(company)):
				companies_Without_Twitter.remove(company)
				
			else:
				print("phony company")

			
		except BaseException as e: 
			print('failed on_status,', str(e))
			time.sleep(2)
	return companies_Without_Twitter

def findBCompanyTwitter(company):
	try: 
		bcomp = api.get_user(id=company.company_name.replace(" ", "") + "inc")
		if checkIfSubstring(bcomp.name.replace(" ", ""), bcomp.screen_name): 
			print("Valid B company")
			company.addSocialMedia("Twitter", "@"+bcomp.screen_name)
			company.addWebsite(bcomp.url)
			company.addLocation(bcomp.location)
			company.printCompanyInfo()
			return True
		else: 
			return False
	except BaseException as e:
		print('failed on_status,', str(e))
		return False
		time.sleep(2)



def findCompaniesWithSearch(company_To_Search): 
	company = api.search_users(company_To_Search.company_name)
	for user in company: 
		print(user.screen_name, ", ", user.name)
		if checkIfSubstring(user.name.replace(" ", ""), company_To_Search.company_name.replace(" ", "")):
			company_To_Search.addWebsite(user.url)
			company_To_Search.addSocialMedia("Twitter", "@" + user.screen_name)
			company_To_Search.addLocation(user.location)
			company_To_Search.printCompanyInfo()
			return True	
		elif checkIfSubstring(user.name.replace(" ", ""), company_To_Search.company_name.replace(" ", "")+"security"):
			company_To_Search.addWebsite(user.url)
			company_To_Search.addSocialMedia("Twitter", "@" + user.screen_name)
			company_To_Search.addLocation(user.location)
			company_To_Search.printCompanyInfo()
			return True
		else:
			continue
	return False




def getRemainderOfCompanies(companies_Without_Twitter):
	for company in companies_Without_Twitter:
		if (findCompaniesWithSearch(company)):
			companies_Without_Twitter.remove(company)
		else:
			continue
	return companies_Without_Twitter


	
def getAllCompanies(companyList):
	companiesNotFound = findCompanyTwitter(companyList)
	print("Getting remainder companies")
	companiesNotFound = getRemainderOfCompanies(companiesNotFound)
	if companiesNotFound:
		return companiesNotFound
	else:
		return

companyNotFoundList = getAllCompanies(companyList)
