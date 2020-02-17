class People:
    #People need name, company name, position title, location, phone number, etc...

    def __init__(self, name, company_name, location="", job_title = "", phone_number = "", social_media = []):
        self.name = name
        self.company_name = company_name
        self.location = location
        self.job_title = job_title
        self.phone_number = phone_number
        self.social_media = social_media





def test():
    print("this is a test")