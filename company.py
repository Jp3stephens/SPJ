from people import People  # provide the people class
from app import db


class Company(db.Model):
    __tablename__ = 'Company'
    company_name = db.Column(db.String(), primary_key=True)
    location = db.Column(db.String())
    website = db.Column(db.String())

    def __repr__(self):
        return "<company_name {}>".format(self.company_name)

    def serialize(self):
        return {
            "name": self.company_name,
            "location": self.location,
            "website": self.website
        }

    def __init__(self, company_name, employees=[], location="", company_telephone="", social_media={}, website=""):
        self.company_name = company_name
        self.employees = employees
        self.location = location
        self.company_telephone = company_telephone
        self.social_media = social_media
        self.website = website

    def addPerson(self, person: People):
        self.employees.append(person)

    def addWebsite(self, website):
        self.website = website
        print("test")

    def addMultiplePeople(self, people: [People]):
        for person in people:
            self.employees.append(person)

    def addLocation(self, location):
        self.location = location

    def addTelephone(self, company_telephone):
        self.company_telephone = company_telephone

    def addSocialMedia(self, key, value):  # THIS NEEDS TO BE CHANGED. SHOULD SOCIAL MEDIA BE ITS OWN CLASS?? PROB
        self.social_media[key] = value

    def displayEmployeeNames(self):  # Display people objects in company
        for person in self.employees:
            print(person.name)

    def printCompanyInfo(self):
        print("Company: ", self.company_name)
        if (self.employees):
            print("employees")
            for employee in self.employees:
                print(employe)
        if (self.website):
            print("Website: ", self.website)
        if (self.location):
            print("Location: ", self.location)

        if (self.company_telephone):
            print("Telephone number: ", self.telephone)
        if (self.social_media):
            for key, value in self.social_media.items():
                print(key, ":", value)
