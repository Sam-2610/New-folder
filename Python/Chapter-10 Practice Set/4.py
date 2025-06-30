""" Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. """

class Train:
    Company = "Indian Railways"

    def __init__(self, booking_method, no_of_seats, train_no, fare):
        self.booking_method = booking_method
        self.no_of_seats = no_of_seats
        self.train_no = train_no
        self.fare = fare

    def book_ticket(self):
        if self.no_of_seats > 0:
            self.no_of_seats -= 1
            print(f"Ticket booked successfully! Seats left: {self.no_of_seats}")
        else:
            print("Sorry, no seats available.")

    def get_status(self):
        print(f"Current seats available: {self.no_of_seats}")

    def get_fare_info(self):
        print(f"Fare for Train No. {self.train_no}: ₹{self.fare}")

# Creating Train instances
t1 = Train("Online", 32, 1002, 150)
t2 = Train("Offline", 30, 1001, 120)
t3 = Train("Online", 25, 1005, 180)

# Sample usage
print(f"Train No: {t1.train_no} | Company: {t1.Company}")
t1.get_status()
t1.get_fare_info()
t1.book_ticket()
t1.get_status()
