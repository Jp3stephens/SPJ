from people import People #provide the people class


class Company:
    def __init__(self, company_name, employees = [], location = "", company_telephone = "", social_media = [], website = ""):
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

    def addSocialMedia(selfs, social_media):    #THIS NEEDS TO BE CHANGED. SHOULD SOCIAL MEDIA BE ITS OWN CLASS?? PROB
        self.social_media = social_media


    def displayEmployeeNames(self): #Display people objects in company
        for person in self.employees:
            print(person.name)




