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


class Solution:
    @staticmethod
    def findAgencyWithHighestPackagePrice(agencies):
        if not agencies:
            return 0
        # Determine the highest price among the agencies
        max_price = agencies[0].price
        for agency in agencies:
            if agency.price > max_price:
                max_price = agency.price
        return max_price

    @staticmethod
    def agencyDetailsForGivenIdAndType(agencies, regNo, packageType):
        for agency in agencies:
            # Check conditions: FlightFacility available, matching RegNo, matching PackageType (case insensitive)
            if (agency.flightFacility and 
                agency.regNo == regNo and 
                agency.pakageType.lower() == packageType.lower()):
                return agency
        return None


if __name__ == "__main__":
    # Reading input
    # Assuming the first line specifies the number of agencies (Standard for this problem type)
    try:
        n = int(input())  # Reads the count of travel agencies
        agencies_list = []

        for _ in range(n):
            reg_no = int(input())
            agency_name = input()
            package_type = input()
            price = int(input())
            # Convert string "true"/"false" to boolean
            flight_facility_str = input()
            flight_facility = True if flight_facility_str.lower() == 'true' else False

            agencies_list.append(TravelAgencies(reg_no, agency_name, package_type, price, flight_facility))

        # Input for search parameters
        search_reg_no = int(input())
        search_package_type = input()

        # Call method 1: Find highest package price
        highest_price = Solution.findAgencyWithHighestPackagePrice(agencies_list)
        print(highest_price)

        # Call method 2: Find agency details
        result_agency = Solution.agencyDetailsForGivenIdAndType(agencies_list, search_reg_no, search_package_type)

        if result_agency:
            print(f"{result_agency.agencyName}:{result_agency.price}")
        else:
            print("None")
            
    except Exception as e:
        pass
