import random
from datetime import date
import math
import sys
class vendor:
    def __init__(self):
        self.ven_db={}
        self.del_ven={}
        self.cus={}
        self.scorcard={}
    def create(self):
        while True:
            vi=random.randint(1000,9999)
            if vi not in self.ven_db:
                print("Enter the Vendor Profile Details:")
                vnm=input("Vendor Company Name:")
                phno=int(input("Phone No.:"))
                email=input("E-mail:")
                typ=input("Type of Vendor(Permanent,Contract):")
                cat=input("Category:")
                cat=cat.lower()
                if cat != "electronics":
                    print("\nInvalid category.... Vendor cannot be onboarded....!")
                    break
                inv=float(input("Average Inventory cost:"))
                sale=float(input("Sales per month (in lakhs):"))
                nor=int(input("Number of orders per month:"))
                ret=int(input("Total No. of returns: "))
                prso=int(input("Total No. of products sold: "))
                print("Names of recent 5 Customers:")
                nm_lst=[]
                for i in range(5):
                    nm=input("Name %d:"%(i+1))
                    nm_lst.append(nm)
                self.cus[vi]=nm_lst
                self.ven_db[vi]={'name':vnm,'phone no.':phno,'email':email,'type':typ,'category':cat,'sales':sale,'inventory':inv,'orders':nor,'returns':ret,'product sold':prso,'review':0}
                print("Vendor Profile Created Successfully")
                print("Your Vendor Profile ID is : %d"%vi)
                break
    
    def round_review(self,rev):
        dec=math.modf(rev)[0]
        if dec>0.5:
            rev=float(round(rev))
        elif dec<0.5:
            rev=math.ceil(rev * 2) / 2
        return rev
    
    def cus_review(self,vi):
        if vi in self.ven_db:
            c=5
            customer=self.cus[vi].copy()
            r=[]
            print("Take Customer Review:")
            while c>0:
                while True:
                    nm=input("\nEnter Name:")
                    if nm in customer:
                        print("Verified Customer")
                        rev=float(input("Enter the Review of product:"))
                        r_lst=[1.00,1.50,2.00,2.50,3.00,3.50,4.00,4.50,5.00]
                        if rev not in r_lst:
                            print("Invalid Review....! Try again....!")
                        else:
                            r.append(rev)
                            customer.pop(customer.index(nm))
                            c-=1
                            break
                    else:
                        print("\nCustomer not Verified.... Try Again...!")
            rev=self.round_review(sum(r)/5)
            del(self.ven_db[vi]['review'])
            self.ven_db[vi]['review']=rev
        else:
            print("Vendor ID not found")
    
    def validate_vendor(self,vi):
        if vi in self.ven_db:
            self.cus_review(vi)
            if (self.ven_db[vi]['type']=="Permanent" and float(self.ven_db[vi]['review'])>=4.0 and float(self.ven_db[vi]['sales'])>=15) or (self.ven_db[vi]['type']=="Contract" and float(self.ven_db[vi]['review'])>=3.0 and float(self.ven_db[vi]['sales'])>=8):
                print("\nVendor Profile validated Successfully")
                con=self.create_contract(self.ven_db[vi].get('type'))
                self.ven_db[vi]['contract']=con
                print("Contract Created Successfully")
                print("Vendor onboarded Successfully")
            else:
                print("\nVendor Profile Not meeting the Requirements")
                print("Vendor cannot be onboarded....!")
                self.delete(vi)
        else:
            print("Vendor ID not found")
            
    def create_contract(self,typ):
        if typ=='Permanent':
            con_prd='20 Years'
            pr_share='50 percent of profit'
        elif typ=='Contract':
            con_prd='5 Years'
            pr_share='35 Percent of profit'
        return (con_prd,pr_share)
    
    def read(self,vi):
        if vi in self.ven_db:
            print("Vendor Profile is as follows: ")
            print("------------------------------------------------------------------")
            print("Vendor ID: %d"%vi)
            print("Vendor Name: %s"%self.ven_db[vi]['name'])
            print("Contact Details:\n\tPhone No.: %d\n\tEmail: %s"%(int(self.ven_db[vi]['phone no.']),self.ven_db[vi]['email']))
            print("Vendor Type: %s\nProduct Category: %s"%(self.ven_db[vi]['type'],self.ven_db[vi]['category']))
            print("Sales per month: %.2f"%float(self.ven_db[vi]['sales']))
            print("Product Review: %.2f"%float(self.ven_db[vi]['review']))
            print("------------------------------------------------------------------")
        else:
            print("Vendor ID not found")

    def delete(self,vi):
        if vi in self.ven_db:
            self.del_ven[vi]=self.ven_db.pop(vi)
            self.cus.pop(vi)
            print("Vendor profile deleted Successfully")
        else:
            print("Vendor ID not found")
    
    def update(self,vi):
        if vi in self.ven_db:
            while True:
                field=input("\nEnter the field to be updated(or 'exit' to go back): ")
                field=field.lower()
                if field=='exit':
                     break
                else:
                    if field in self.ven_db[vi]:
                        if field=='review':
                            self.cus_review(vi)
                        else:
                            nval=input("Enter new value:")
                            del(self.ven_db[vi][field])
                            self.ven_db[vi][field]=nval
                        print(f"The {field} updated successfully")
                    else:
                        print("Invalid Field ...! Try again...!")
        else:
            print("Vendor ID not found")

    def generate_vendor_scorecard(self,vi):
        if vi in self.ven_db: 
            aov=((float(self.ven_db[vi]['sales'])*(10**5))/int(self.ven_db[vi]['orders']))
            naov=((aov-3500)/(9500-aov))*0.3
            rr=((int(self.ven_db[vi]['returns'])/int(self.ven_db[vi]['product sold']))*100)
            nrr=((rr-15)/(30-rr))*0.2
            in_to=float(self.ven_db[vi]['sales'])/float(self.ven_db[vi]['inventory'])
            nin_to=((in_to-2)/(8-in_to))*0.25
            crev=float(self.ven_db[vi]['review'])
            ncrev=((crev-2.5)/(5.5-crev))*0.25
            print("\n--------------------------------------------------------------------------------")
            print("\n\t\t\t!......The Vendor Scorecard......!\n")
            print("--------------------------------------------------------------------------------")
            print("Vendor ID: %d"%vi)
            print("Vendor Name: %s"%self.ven_db[vi]['name'])
            today = date.today()
            formatted_date = today.strftime('%d-%m-%Y')
            print("Scorcard Date: %s"%formatted_date)
            print("-------------------------------------------------------------------------------")
            print("%-25s\t%s\t\t%s\t\t%s"%("Scorecard Criteria","Score","Weight","Weighted Score"))
            print("-------------------------------------------------------------------------------")
            print("%-25s\t%7.2f\t\t%s\t\t%.2f"%("Average Order Value(AOV):",aov,"30%",naov))
            print("%-25s\t%7.2f\t\t%s\t\t%.2f"%("Average Customer Review: ",crev,"25%",ncrev))
            print("%-25s\t%7.2f\t\t%s\t\t%.2f"%("Return Rate:",rr,"20%",nrr))
            print("%-25s\t%7.2f\t\t%s\t\t%.2f"%("Inventory Turnover:",in_to,"25%",nin_to))
            print("-------------------------------------------------------------------------------")
            os=naov+ncrev+nrr+nin_to
            print("Overall score : %.2f "%os)
            grade=None
            print("-------------------------------------------------------------------------------")
            if os<2:
                grade='C'
                print(f"Grade: {grade}\nPoor Perofrmance")
            elif os<3:
                grade='B'
                print(f"Grade: {grade}\nAverage Performance")
            elif os<=5:
                grade='A'
                print(f"Grade: {grade}\nGood Perfornamce")
            print("-------------------------------------------------------------------------------")
            self.scorcard[vi]={'AOV':aov,'Customer Review':crev,'Return Rate':rr,'Inventory Turnover':in_to,'Overall Score':os,'Grade':grade}
        else:
            print("Vendor ID not found")  

    def display(self):
        if len(self.ven_db)==0:
            print("List is empty")
        else:
            print("List of Onboarder Vendors:")
            print("-------------------------------------------------------------------------------")
            print("%-10s\t%-25s\t%-12s\t%-5s"%('Vendor ID','Vendor Name','Overall Score','Grade'))
            for i in self.ven_db:
                print("%-10d\t%-25s\t%-12.2f\t%-s"%(i,self.ven_db[i]['name'],self.scorcard[i]['Overall Score'],self.scorcard[i]['Grade'])) 
            print("-------------------------------------------------------------------------------")     

v=vendor()
while True:
    print("\n1.Create 2.Validate Vendor 3.Read 4.Update 5.Delete \n6.Generate Scorecard 7.Display Vendors list 8.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        v.create()
    elif ch==2:
        vid=int(input("Enter Vendor Profile ID: "))
        v.validate_vendor(vid)
    elif ch==3:
        vid=int(input("Enter Vendor Profile ID: "))
        v.read(vid)
    elif ch==4:
        vid=int(input("Enter Vendor Profile ID: "))
        v.update(vid)
    elif ch==5:
        vid=int(input("Enter Vendor Profile ID: "))
        v.delete(vid)
    elif ch==6:
        vid=int(input("Enter Vendor Profile ID: "))
        v.generate_vendor_scorecard(vid)
    elif ch==7:
        v.display()
    elif ch==8:
        sys.exit()
    else:
        print("Invalid Choice")