class Parking_garage():
    def __init__(self):
        self.tickets = [1, 1, 1, 1]
        self.parkingSpaces = [1, 1, 1, 1]
        self.currentTicket = {'paid': False}
    
    def takeTicket(self):   
        try:
            self.tickets.remove(1)
        except ValueError:
            print("Sorry, there are no more spaces available.")
        else:
            self.parkingSpaces.remove(1)
            print("Please proceed to an empty spot.")

    def payForParking(self):
        payment = []
        user_input = input("Please input $10. Type 10 when completed or exit to cancel: ").lower()
        if user_input == '10':
            payment.append(user_input)
            if payment:
                print("Your ticket has been paid. You have 15 minutes to leave.")
                self.currentTicket['paid'] = True
            else:
                print("Please pay when you exit.")

    def leaveGarage(self):
        while True:
            if self.currentTicket['paid']:
                print("Thank you. Have a nice day!")
                break
            else:
                payment = []
                payment.append(input("Please pay $10. Type 10 when completed: "))
                if '10' in payment:
                    print("Thank you. Have a nice day!")
                    self.tickets.append(1)
                    self.parkingSpaces.append(1)
                    break
                else:
                    print("Your payment was not recieved. Please try again.")
                    continue

    def runner(self):
        while True:
            answer = input("Would you like to enter, pay for ticket, or leave? <enter or pay or leave> ").lower()
            if answer == 'enter':
                self.takeTicket()
            elif answer == 'pay':
                self.payForParking()
            elif answer == 'leave':
                self.leaveGarage()
                break
            else:
                print('Your input was not recognized. Please try again: ')
                continue

user1 = Parking_garage()
user1.runner()