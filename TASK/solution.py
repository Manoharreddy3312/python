
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
        n = int(input("Enter the number of travel agencies: "))  # Reads the count of travel agencies
        agencies_list = []

        for i in range(0,n):
            reg_no = int(input("Enter the registration number: "))
            agency_name = input("Enter the agency name: ")
            package_type = input("Enter the package type: ")
            price = int(input("Enter the price: "))
            # Convert string "true"/"false" to boolean
            flight_facility_str = input("Enter the flight facility (true/false: ")
            flight_facility = True if flight_facility_str.lower() == 'true' else False

            agencies_list.append(TravelAgencies(reg_no, agency_name, package_type, price, flight_facility))

        # Input for search parameters
        search_reg_no = int(input("Enter the registration number: "))
        search_package_type = input("Enter the package type: ")

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
