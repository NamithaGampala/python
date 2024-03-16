
class car:
    def login(self):
        c=['toyota','mahindra','mercedes','1','2','3']
        while(1):
            company=input("Enter the company name from the options 1.Toyota 2.Mahindra 3.Mercedes:")
            if company in c:
                break
            else:
                print("Enter a valid company")
        self.a=company
    def model(self):
        if self.a=="toyota" or self.a=='1':
            print("Welcome to Toyota family..")
            b=['hatchback','suv','muv','1','2','3']
            while(1):
                model=input("Select the model name from the options 1.Hatchback 2.Muv 3.Suv:")
                if model in b:
                    break
                else:
                    print("Enter the valid model name")
            self.m=model     
        if self.a=="mahindra"  or self.a=='2':
            print("Welcome to Mahindra family..")
            d=['thar','xuv700','Scorpio','1','2','3']
            while(1):
                model=input("Select the model name from the options 1.Thar 2.XUV700 3.Scorpio:")
                if model in d:
                    break
                else:
                    print("Enter the valid model name")
            self.m=model
            
        if self.a=="mercedes" or self.a=='3':
            print("Welcome to Mercedes family..")
            e=['e_class','c_class','gla','1','2','3']
            while(1):
                model=input("Select the model name from the options 1.e_class 2.c_class 3.gla:")
                if model in e:
                    break
                else:
                    print("Enter the valid model name")
                    
            self.m=model
            
    def variant(self):
        f=['petrol','diesel','1','2']
        while(1):
            v=input("Enter the variant you want either 1.petrol or 2.diesel:")
            if v in f:
                break
            else:
                print("Enter valid varient name")
        self.y=v
    def display(self):
        if (self.a=="toyota" or self.a=='1') and (self.m=="hatchback" or self.m=='1') and (self.y=="petrol" or self.y=='1'):
            price=600000
        if (self.a=="toyota" or self.a=='1') and (self.m=="hatchback" or self.m=='1') and (self.y=="diesel" or self.y=='2'):
            price=750000
        if (self.a=="toyota" or self.a=='1') and (self.m=="muv" or self.m=='2') and (self.y=="petrol" or self.y=='1'):
            price=1000000
        if (self.a=="toyota" or self.a=='1') and (self.m=="muv" or self.m=='2') and (self.y=="diesel" or self.y=='2'):
            price=1150000
        if (self.a=="toyota" or self.a=='1') and (self.m=="suv" or self.m=='3') and (self.y=="petrol" or self.y=='1'):
            price=2000000
        if (self.a=="toyota" or self.a=='1') and (self.m=="suv" or self.m=='3') and (self.y=="diesel" or self.y=='2'):
            price=2200000
        if (self.a=="mahindra" or self.a=='2') and (self.m=="thar" or self.m=='1') and (self.y=="petrol" or self.y=='1'):
            price=2000000
        if (self.a=="mahindra" or self.a=='2') and (self.m=="thar" or self.m=='1') and (self.y=="diesel" or self.y=='2'):
            price=2300000
        if (self.a=="mahindra" or self.a=='2') and (self.m=="xuv700" or self.m=='2') and (self.y=="petrol" or self.y=='1'):
            price=1300000
        if (self.a=="mahindra" or self.a=='2') and (self.m=="xuv700" or self.m=='2') and (self.y=="diesel" or self.y=='2'):
            price=1400000
        if (self.a=="mahindra" or self.a=='2') and (self.m=="scorpio" or self.m=='3') and (self.y=="petrol" or self.y=='1'):
            price=1500000
        if (self.a=="mahindra" or self.a=='2') and (self.m=="scorpio" or self.m=='3') and (self.y=="diesel" or self.y=='2'):
            price=1650000
        if (self.a=="mercedes" or self.a=='3') and (self.m=="e_class" or self.m=='1') and (self.y=="petrol" or self.y=='1'):
            price=5000000
        if (self.a=="mercedes" or self.a=='3') and (self.m=="e_class" or self.m=='1') and (self.y=="diesel" or self.y=='2'):
            price=5300000
        if (self.a=="mercedes" or self.a=='3') and (self.m=="c_class" or self.m=='2') and (self.y=="petrol" or self.y=='1'):
            price=6000000
        if (self.a=="mercedes" or self.a=='3') and (self.m=="c_class" or self.m=='2') and (self.y=="diesel" or self.y=='2'):
            price=6200000
        if (self.a=="mercedes" or self.a=='3') and (self.m=="glc" or self.m=='3') and (self.y=="petrol" or self.y=='1'):
            price=6500000
        if (self.a=="mercedes" or self.a=='3') and (self.m=="glc" or self.m=='3') and (self.y=="diesel" or self.y=='2'):
            price=6700000
        sgst=(10/100)*price
        cgst=(5/100)*price
        insurance=(12/100)*price
        print("Xshowroom Price:",price)
        onroad=sgst+cgst+insurance+price
        print("Onshowroom Price:",onroad)
obj=car()
obj.login()
obj.model()
obj.variant()
obj.display()
            
