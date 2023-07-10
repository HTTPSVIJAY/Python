class RailwayForm :
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

vijayApplication = RailwayForm()
vijayApplication.name = "vijay"
vijayApplication.train = "mahalaxmi express"
vijayApplication.printData()