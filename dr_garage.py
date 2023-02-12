# Dan's parking garage code.
class Garage():
    def __init__(self):
        self.tickets = 3
        self.parkingSpot = {
            1: {
                "open":True,
                "paid":False,
            },
            2: {
                "open":True,
                "paid":False,
            },
            3: {
                "open":True,
                "paid":False,
            }
        }

    def takeTicket(self):
        '''This function assigns an open parking spot if it's available.'''
        for spot in self.parkingSpot.keys():
            if self.parkingSpot[spot]["open"] == True:
                self.parkingSpot[spot]["open"] = False
                print(f"Please park in parking spot number {spot}.")
                self.tickets -= 1
                break
            elif self.tickets == 0:
                print("There are no available parking spaces.")
                break

    def parkingPayment(self):
        '''This function closes out payment with customer and resets parking spot availability.'''
        # Cost of parking set to $5
        balance = 5 
        
        # Catch if invalid parking spot entered
        while True:
            spotNum = int(input("\nEnter your parking spot number: "))
            if spotNum <= 0 or spotNum > 3:
                print("Invalid input (parking spot doesn't exist)")
            else:
                break

        # Calculate payment
        while self.parkingSpot[spotNum]["paid"] == False:
            payment = round(float(input(f"Your balance is ${balance:.2f}. Enter payment: ")), 2)
            balance -= payment
            round(balance, 2)
            if balance > 0:
                print(f"Your remaining balance is ${balance:.2f}.")
            elif balance < 0:
                print("Invald payment amount (overpayment)")
                balance += payment
            else:
                print("Payment complete. Thank you, have a nice day.\n")
                self.parkingSpot[spotNum]["paid"] = True
                self.tickets += 1
        
        # Reset parking spot availability and balance.
        self.parkingSpot[spotNum]["open"] = True
        self.parkingSpot[spotNum]["paid"] = False

    def runner(self):
        '''Runner func.'''
        print('Welcome to the parking garage.')
        # Test if more than available spaces get assigned.
        for i in range(4):
            self.takeTicket()
        
        # Test payment and exit works.
        self.parkingPayment()
        
        # Test if you can reassign new available spot and still pay after
        self.takeTicket()
        self.parkingPayment()

# Test class.
iParked = Garage()
iParked.runner()

