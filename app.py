from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from company import Company

@app.route("/")
def hello(): 
	return "Hello World!"

@app.route("/addCompany")
def add_Company():
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
		companies = companies.query.all()
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
	

if __name__ == '__main__': 
	app.run()


