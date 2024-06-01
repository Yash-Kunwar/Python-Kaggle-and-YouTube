class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f'Name of the train is {self.name}')
        print(f'Seats available are {self.seats}')

    def fareInfo(self):
        print(f"Price of the ticket is Rs.{self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f'Your seat has been booked, seat no.: {self.seats}')
            self.seats = self.seats-1
        else:
            print('Sorry, train is full, please try TATKAL')


trainName = Train('Jan Shatabdi 15640', 150, 500)
trainName.getStatus()
trainName.bookTicket()
trainName.bookTicket()
trainName.bookTicket()
trainName.bookTicket()
trainName.bookTicket()
trainName.bookTicket()
trainName.bookTicket()
trainName.bookTicket()
print('\n')
trainName.getStatus()
