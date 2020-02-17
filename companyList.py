#FILE CONTAINING LIST OF COMPANIES THAT WE NEED TO SCRAPE. 
from company import Company
from people import People
import pandas as pd
import numpy as np



#create a new dataframe object
companyDF = pd.read_csv('Company Training Set - Sheet1.csv')
company_Text_List = [] #This list will contain company NAMES for each company in our list. TEXT ONLY

for company in companyDF.values:
    company_Text_List.append(company[0])

print(company_Text_List)

companyList = [] # This list will contain company OBJECTS of every company that is in our list

for name in company_Text_List:
    companyList.append(Company(name))


