class balance:
    def card(self):
        c=['rupay','visa','mastercard','1','2','3']
        while(1):
            print("choose one card from the options:\n 1.Rupay\n 2.visa\n 3.Mastercard")
            n=input()
            if n in c:
                break
            else:
                print("select the valid card")
        self.g=n
        
        
    def display(self,a):
        print("The remaning amount is ",a)
        self.z=a
class login(balance):
    def autentication(self):
        name=input("user name:")
        password=input("password:")
      
        if name==password:
            f=['checkbalance','cashwithdrawl','cashdeposit','lastthreetranasactions','1','2','3','4']
            while(1):
                print("choose any of the options:\n1.checkbalance \n2.cashwithdrawl\n3.cashdeposit\n4.lastthreetranasactions")
                e=input()
                self.x=e
                if e in f:
                    break
                else:
                    print("invalid select again")
        else:
            
            print("please enter again")
            while (name!=password):
                self.autentication()
                break
    
    def task(self):
        if self.x=="checkbalance" or self.x=="1":
            self.display(20000)
            
            
        
        if self.x=="cashwithdrawl" or self.x=="2":
            t=int(input("enter the amount:"))
            if (self.g=='rupay'or self.g=='1') and t<=2000:
                print("Amount withdrawn successfully")
                print("The remaining amount ",(self.z-t))
        
            elif (self.g=='visa'or self.g=='2') and t<=4000:
                print("Amount withdrawn successfully")
                print("The remaining amount ",(self.z-t))
        
            elif (self.g=='mastercard'or self.g=='3') and t<=8499:
                print("Amount withdrawn successfully")
                print("The remaining amount ",(self.z-t))
            else:
                print("Crossed the limit....Amount cannot be withdrawn...")
        if self.x=="cashdeposit" or self.x=="3":
            h=int(input("Enter the amount:"))
            print("The remaining amount ",(self.z+h))
        if self.x=="lastthreetransactions" or self.x=="4":
            print("The last three transactions are 2000,1500,5000")
                        
obj=login()
obj.card()
obj.display(20000)
obj.autentication()
obj.task()
            
            
            
        
    
    

            

                       
            

        
    
            
        
    
