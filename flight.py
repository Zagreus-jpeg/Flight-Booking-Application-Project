from datetime import datetime

class Flight:
    def __init__(self, flg_number, flg_type, flg_capacity, open_time, close_time,departure_time):
        self.flg_number = flg_number
        self.flg_type = flg_type.lower()
        self.flg_capacity = flg_capacity
        self.open_time = open_time
        self.close_time = close_time
        self.departure_time=departure_time
        self.bookings = []

    def is_booking_open(self, current_time):
        if(current_time >= self.open_time and current_time <= self.close_time):
            return True
        else:
            return False

    def availability(self):
        available_seats = self.flg_capacity - len(self.bookings)
        return available_seats

    def add_booking(self, booking, current_time):
        if not self.is_booking_open(current_time):
            print("Booking closed")
            return False
        elif self.availability() <= 0:
            print("Flight full")
            return False
        elif self.is_booking_open(current_time):
            self.bookings.append(booking)
            print("Booked Successfully")
            return True

    def get_proportional_time(self, current_time):
        total_time = (self.close_time - self.open_time).total_seconds()
        booked_time = (current_time - self.open_time).total_seconds()
        T = booked_time / total_time
        if T < 0:
            return 0
        elif T > 1:
            return 1
        return T 