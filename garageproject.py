class Parking_Garage():
    def __init__(self):
        self.tickets= [1,1,1,1,1]
        self.parking_spaces=[1,1,1,1,1]
        self.current_ticket={'paid': False} 

    # take ticket method 
    # tickets .remove or delete ticket 
    # parking spaces .remove or delete  
      
              # <--------pay for parking method-------->
    # prompt customer for money in input statement and store in variable
    def pay_for_parking(self):

     while True:
    
        balance = int(input("Please insert money for ticket. "))
        if balance != 0: 
            print("Your ticket has been paid. You have 15 minutes to leave.")
            self.current_ticket['paid']=True 
            print("Thank You! Have a nice day!")
            break 

      #<------------Take Ticket method---------------->  
def takeTicket(self):
        #Takes a ticket if the user enters the garage
        #Removes 1 from available tickets and 1 from available parking spaces
        #Checks to see if there are available tickets/parking spaces for the user
        #to take/space to park before the user is allow to enter
        try:
            self.tickets.remove(1)
        except ValueError:
            print("Sorry, there are no more spaces available.")
        else:
            self.parking_spaces.remove(1)
            print("Please proceed to an empty spot.")
    

           #<---------updating parking_spaces----------->   
    #Dan you can work on this one
    #update parking space list to increase by 1 
    # update tickets list to increase by 1 (add tickets to list) 

    # <--------- Devin's code --------->
    #Create a runner for the for the program
    def runner(self):
        #Use a while loop to display the options to the user
        #Break when the users exits the garage
        while True:
            answer = input("Would you like to enter, pay for ticket, or leave? <enter or pay or leave> ").lower()
            if answer == 'enter':
                self.takeTicket()
            elif answer == 'pay':
                self.pay_for_parking()
            elif answer == 'leave':
                self.leaveGarage()
                break
            else:
                print('Your input was not recognized. Please try again: ')
                continue

user1 = Parking_Garage()
user1.runner()