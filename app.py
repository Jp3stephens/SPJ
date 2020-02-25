from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from company import Company
from companyList import companyList
from TwitterScrape import getAllCompanies, updatedCompanyObjectList

@app.route("/")
def hello(): 
	return "Hello World!"


@app.route("/getTwitterScrape")
def add_company_info_from_TwitterScrape():
	companiesNotFound = getAllCompanies(companyList, updatedCompanyObjectList)
	for company in updatedCompanyObjectList:
		
		try:
			print("Printing company,", company.company_name) 
			company = Company(
				company_name = company.company_name, 
				location = company.location,
				website = company.website
				)
			
			db.session.add(company)
			db.session.commit()	
		#	return "Company added from TwitterScrape. Company name = {}".format(company.company_name)
		except Exception as e: 
			return(str(e))
	return "Company added from TwitterScrape. Company name = {}, company website = {}, company location = {}".format(company.company_name, company.website, company.location)





@app.route("/addCompany")
def add_Company():
	#add_company_info_from_TwitterScrape(companyList)
	company_name=request.args.get('company_name')
	location=request.args.get('location')
	website=request.args.get('website')
	try: 
		company = Company(
			company_name=company_name, 
			location=location,
			website=website
			)
		db.session.add(company)
		db.session.commit()
		return "Company added. company_name={}".format(company.company_name)
	except Exception as e: 
		return (str(e))

@app.route('/getall')
def get_all_companies(): 
	try: 
		companies = Company.query.all()
		return jsonify([e.serialize() for e in companies])
	except Exception as e: 
		return(str(e))

@app.route('/get/<company_name_>')
def get_by_name(company_name_): 
	try: 
		company = Company.query.filter_by(company_name=company_name_).first()
		return jsonify(company.serialize())
	except Exception as e:
		return(str(e))
	
@app.route("/add/form", methods=['GET', 'POST'])
def add_company_form(): 
	if request.method == 'POST':
		company_name=request.form.get('company_name')
		website = request.form.get('website')
		location = request.form.get('location')
		try: 
			company = Company(
				company_name = company_name, 
				location = location, 
				website = website
				)
			db.session.add(company)
			db.session.commit()
			return "Company added. Company name = {}".format(company.company_name)
		except Exception as e: 
			return(str(e))
	return render_template("getdata.html")


if __name__ == '__main__': 
	app.run()

		
