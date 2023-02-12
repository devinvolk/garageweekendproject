class Garage():
    def __init__(self):
        self.tickets = 3
        self.openSpaces = {1:True, 2:True, 3:True}
        self.balance = 0

    def takeTicket(self):
        '''This function checks to '''
        for k,v in self.openSpaces.items():
            if v == True:
                self.tickets-=1
                v = False
                print(f"Please park in space number {k}.")
                break
            else:
                print("There are currently no available parking spaces.")

    def payForParking(self):
        pass

    def leaveGarage(self):
        pass
