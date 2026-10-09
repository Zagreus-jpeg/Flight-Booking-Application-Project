class Booking:
    def __init__(self, booking_id, passenger, flight, seat_class, price):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.seat_class = seat_class
        self.price = round(price, 2)

    def display_booking(self):
        print(f"Passenger: {self.passenger.name}")
        print(f"Flight: {self.flight.flg_number}")
        print(f"Seat Class: {self.seat_class}")
        print(f"Price: {self.price}")