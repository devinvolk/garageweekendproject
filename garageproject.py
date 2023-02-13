# Group project: Devin, Shannon, and Dan
class Parking_Garage():
    def __init__(self):
        self.tickets = [1,1,1,1,1]
        self.parking_spaces = [1,1,1,1,1]
        self.current_ticket = {'paid': False} 

    def pay_for_parking(self, gatePay=False):
        '''Prompt customer for money.'''
        while True:
            balance = int(input("Please insert money for ticket. "))
            if balance != 0 and gatePay == False: 
                print("Your ticket has been paid. You have 15 minutes to leave.")
                self.current_ticket['paid'] = True
                break
            elif balance != 0 and gatePay == True: 
                print("Your ticket has been paid. Thank you, have a nice day.")
                self.current_ticket['paid'] = True
                break 
  
    def take_ticket(self):
        '''This function decreases available ticket and parking spaces by 1.'''
        try:
            self.tickets.remove(1)
        except ValueError:
            print("Sorry, there are no more spaces available.")
        else:
            self.parking_spaces.remove(1)
            print("Please proceed to an empty spot.")
    
    def leave_garage(self):
        '''This functions checks for payment. If not paid, prompts for payment. After confirmed payment, it resets parking spots and tickets.'''
        if self.current_ticket['paid'] == True:
            print("You have already paid. Thank you, have a nice day.")
            self.tickets.append(1)
            self.parking_spaces.append(1)
            self.current_ticket['paid'] = False
        else:
            self.pay_for_parking(True)
            self.tickets.append(1)
            self.parking_spaces.append(1)
            self.current_ticket['paid'] = False
        
    def runner(self):
        '''Runner funciton. Use a while loop to display the options to the user. Break when the users exits the garage'''
        while True:
            answer = input("Would you like to enter, pay for ticket, leave, or quit the app? <enter or pay or leave or quit> ").lower()
            if answer == 'enter':
                self.take_ticket()
            elif answer == 'pay':
                self.pay_for_parking()
            elif answer == 'leave':
                self.leave_garage()
            elif answer == 'quit':
                break
            else:
                print('Your input was not recognized. Please try again: ')
                continue
        
        print(
            f"Available tickets: {len(self.tickets)}"
            f"\nAvaialable parking spaces: {len(self.parking_spaces)}"
        )

# Test the class.
user1 = Parking_Garage()
user1.runner()