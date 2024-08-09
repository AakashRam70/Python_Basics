class bikeRental:
    def __init__(self,stock):
        self.stock=stock

    def displayBike(self):
        print("Total Bikes", self.stock)
    def rentForBike(self,q):

        if q<=0:
            print("Invalid Quantity")
        elif q>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-q
            print("Total Prices",q*100)
            print("Total Bikes",self.stock)

while True:
    obj = bikeRental(100)
    uc = int((input(
        '''
1 Display Stocks
2 Rent a Bike
3 Exit
'''
    )))

    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter The Quentity :--"))
        obj.rentForBike(n)
    else:
        break;
