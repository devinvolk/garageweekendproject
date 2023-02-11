class Parking_Garage():
    def __init__(self):
        self.tickets= [1,1,1,1,1]
        self.parking_spaces=[1,1,1,1,1]
        self.current_ticket={'paid': False} 





    # take ticket method 
    # tickets .remove or delete ticket 
    # parking spaces .remove or delete  
      
    # <--------- Devin's code --------->
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
    # <--------- Devin's code --------->

    # <--------pay for parking method-------->
    # prompt customer for money in input statement and store in variable
    # balance = int(input("Please insert money for ticket. "))
    # # create in if statement if balance = 0 
    # # print statement saying balance paid 15 min to leave.
    # if balance == 0: 
    #     print("Thank you! Your ticket has been paid. You have 15 minutes to leave.")
    #     self.current_ticket['paid']=True  
    
    # #if or else statement  balance != 0 display input to promp payment 
    # # Devin you can work on doing this 
    # # Once payment is made display message "thank you have a nice day!" 
    # else:
    #     if balance != 0:
    #         self.current_ticket['paid']=False 
    #         print(balance) 

    # <--------- Devin's code --------->
    def payForParking(self):
        #Create an empty list to recieve payemnt from user input
        payment = []
        user_input = input("Please input $10. Type 10 when completed or exit to cancel: ").lower()
        #Check if payment was the correct string of '10' and append list
        if user_input == '10':
            payment.append(user_input)
            #Check if the list is not empty, meaning payment has been recieved
            if payment:
                print("Your ticket has been paid. You have 15 minutes to leave.")
                self.current_ticket['paid'] = True
            #Statement if the payment was not recieved    
            else:
                print("Please pay when you exit.")
    # <--------- Devin's code --------->
        
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
                self.payForParking()
            elif answer == 'leave':
                self.leaveGarage()
                break
            else:
                print('Your input was not recognized. Please try again: ')
                continue

user1 = Parking_Garage()
user1.runner()