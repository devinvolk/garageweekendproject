class Parking_Garage():
    def __init__(self):
        self.tickets= [1,2,3,4,5]
        self.parking_spaces=[1,2,3,4,5]
        self.current_ticket={'paid':False} 





    # take ticket method 
    # tickets .remove or delete ticket 
    # parking spaces .remove or delete    

    
    # <--------pay for parking method-------->
    # prompt customer for money in input statement and store in variable 
    

    balance = int(input("Please insert money for ticket. "))
    # create in if statement if balance = 0 
    # print statement saying balance paid 15 min to leave.
    if balance == 0: 
        print("Thank you! Your ticket has been paid. You have 15 minutes to leave.")
        self.current_ticket['paid']=True  
    
    #if or else statement  balance != 0 display input to promp payment 
    # Devin you can work on doing this 
    # Once payment is made display message "thank you have a nice day!" 
    else:
        if balance != 0:
            self.current_ticket['paid']=False 
            print(balance)  
            
        

    #<---------updating parking_spaces----------->   
    #Dan you can work on this one
    #update parking space list to increase by 1 
    # update tickets list to increase by 1 (add tickets to list) 


    

    

    

    