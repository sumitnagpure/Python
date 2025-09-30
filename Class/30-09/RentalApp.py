from VehiclePortal import Taxi
# from VehiclePortal import Bus
from RentalService import Rental

class RentalApp:
    @staticmethod
    def display_rent(rental_vehicle: Rental):
        print('-------Rental App-------')
        hrs=int(input('Enter the hours to rent:'))
        amt=rental_vehicle.calculate_rent(hrs)
        print(f'Total rent for {rental_vehicle} : Rs {amt}')

print('--------The USER---------')

taxi = Taxi('MS', 'Dzire', 12000, 12345)
RentalApp.display_rent(taxi)