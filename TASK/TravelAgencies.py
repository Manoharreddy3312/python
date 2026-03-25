

class TravelAgencies:
    def __init__(self, regNo, agencyName, pakageType, price, flightFacility):
        self.regNo = regNo
        self.agencyName = agencyName
        self.pakageType = pakageType
        self.price = price
        self.flightFacility = flightFacility

    # Getters
    def get_regNo(self):
        return self.regNo

    def get_agencyName(self):
        return self.agencyName

    def get_pakageType(self):
        return self.pakageType

    def get_price(self):
        return self.price

    def get_flightFacility(self):
        return self.flightFacility

    # Setters
    def set_regNo(self, regNo):
        self.regNo = regNo

    def set_agencyName(self, agencyName):
        self.agencyName = agencyName

    def set_pakageType(self, pakageType):
        self.pakageType = pakageType

    def set_price(self, price):
        self.price = price

    def set_flightFacility(self, flightFacility):
        self.flightFacility = flightFacility

