class User:
    def __init__(self, name, password, site_url): #constructor
        self.name = name
        self.password = password
        self.url = site_url

    def login(self):
        print(f"User {self.name} was logged in {self.url}")

    def logout(self):
        print(f"User {self.name} was logged out {self.url}")


dev_user = User("dev_user", "dev_password", "http://dev-site.org") #instance creation

print(dev_user.name) #attribute
dev_user.login() #method
dev_user.logout() #method

stage_user = User("stage_user", "stage_password", "http://stage-site.org")
prod_user = User("prod_user", "prod_password", "http://prod-site.org")