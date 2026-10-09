from flight import Flight
from booking import Booking

class BookingSystem:
    def __init__(self):
        self.flights = []
        self.bookings = []
        self.passengers = []

    def addflight(self, flight):
        self.flights.append(flight)

    def removeFlight(self,flight_name):
        for i in range (len(self.flights)):
            curr_flight=self.flights[i]
            if(curr_flight.flg_number==flight_name):
                self.flights.pop(i)
    def viewflight(self):
        print("\n--- AVAILABLE FLIGHTS ---")
        for flight in self.flights:
            print(f"""
            Flight number: {flight.flg_number}
            Flight Type: {flight.flg_type}
            Available seats: {flight.availability()}
            Booking Open: {flight.open_time}
            Booking Close: {flight.close_time}
            """)

    def find_flight(self, flight_number):
        for flight in self.flights:
            if flight.flg_number == flight_number:
                return flight
        return None

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def find_passenger(self, passenger_name):
        for p in self.passengers:
            if p.name.lower() == passenger_name.lower():
                return p
        return None

    def createBooking(self, booking_id, passenger_name, flight_number, seat_class, price, current_time):
        flight = self.find_flight(flight_number)
        if flight is None:
            print("Flight not found")
            return None
        passenger = self.find_passenger(passenger_name)
        if passenger is None:
            print("Passenger not found")
            return None
        booking = Booking(booking_id, passenger, flight, seat_class, price)
        success = flight.add_booking(booking, current_time)
        if success:
            self.bookings.append(booking)
            return booking
        return None
    
    def total_revenue_per_flight(self):
        dt={}
        for i in range (len(self.bookings)):
           p=self.bookings[i].price
           flight_number=self.bookings[i].flight.flg_number
           dt[flight_number]=dt.get(flight_number,0)+p
        return dt   

