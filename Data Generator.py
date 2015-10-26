import random


#########################################################LISTS###############################################################
fname = ["Michelle","Phyllis","Sally","Stacey","Macey","Marilyn","Claudette","Claudia","Alannah","Anne","Emma","Emily","Orla","Aoife","Katie","Catherine","Yvonne","Simone","June","Carmel","Maureen","Helen","Lisa","Kym","Mary-Kate","Maggie","Miranda","Kelly","Leiha","Jane","Sarah","Michael","Jackson","Bobby","Billy","Shane","Sean","Graham","David","Niall","Seamus","Cathal","Callum","Karl","Carl","Josh","Joe","Joey","Richard","Dick","George","Alan","Abraham","Bryan","Bob","Barry","Will","Liam","Ben","James","Eric","Abdul"]

lastn = ["Thompson","Carroll","Hynes","Kelly","Ryan","Bachin","Murray","Findon","Strutt","Ramone","Austin","O'Keeffe","O'Brien","Mullen","Fanning","Curran","McNamara"]

phonenum = "3538{0}"

town = ["Enfield","Newtown","Johnstown","Leixlip","Summerhill","Blancardstown","Clifford","Kilcock","Maynooth","Swords","Carragh","Navan","Trim","Mullingar"]

county = ["Meath","Dublin","Cork","Kilkenny","Cavan","Wicklow","Wexford","West Meath","Louth","Leitrim","Roscommmon","Galway","Mayo","Clare",]

estate = ["Blackwater","Evergreen","New Inn","Glen Abhainn","Glenroyal","Delmere","NewRoad","Road",]

city = ["Dublin","Navan","London","Galway","Cork","Mullingar"]
storeaddr = ["11 Westmoreland St. Upper","7 Kennedy Road","131 Brompton Road","39 Shop St.","78 Patrick St.","Unit 7a Mullingar Shopping Centre"]
postcode = ["ZX31","ZX54","L12","ZXR4","ZXA3","ZX46"]

Country = ["Ireland", "Botswana", "Australia","Germany","France","Italy","Zimbabwe","South Africa","Poland","Romania","Luxembourg","Switzerland","Sweden","Norway","Holland","Belgium","Turkey","Egypt","Kenya","Spain"]
CountryCode= ["353","267","61","49","33","39","263","27","48","40","352","41","46","47","375","32","90","20","254","34"]
    
jobtitle = ["Sales Rep", "Supervisor", "Janitor", "Promoter", "Manager", "Till Operator", "Data Analyst", "IT Technician", "Data Warehouse Administrator", "Data Architect", "Security Technician", "Operations Manager", "Software Developer", "Research And Development"]

PhoneModel = ["Samsung Galaxy","Samsung Galaxy 2","Samsung Galaxy 3","Samsung Galaxy S4","Samsung Galaxy S5","iPhone 2","iPhone 3","iPhone 4","iPhone 4s","iPhone 5"]
PhonePrice = [80.00,120.00,150.00,180.00,200.00,400.,480.00,520.00,550.00,600.00]

#####################################################END LISTS###############################################################
dig = random.randint(1,120)
dig=str(dig)



########################################################TABLES####################################################

#f=open("C:\Python27\Database\Customer.sql",'w')
#f.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Customer(customerId,customerFirstName, customerLastName, customerAddress, customerDOB,customerGender,customerCity,customerEmail,salesRepEmpNum) VALUES\n\n\n")
#f.close()
#j=open("C:\Python27\Database\Account.sql",'w')
#j.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Account(accountNumber, accountCreationDate, accountType,accountManagerEmpId,customerId,phoneNumId,simNum,pricePlanId) VALUES\n\n")
#j.close()
f1=open("C:\Python27\Database\Phone.sql",'w')
f1.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Phone(phoneId,phoneModel, phoneIMEI, phonePrice) VALUES\n\n")
f1.close()
f2=open("C:\Python27\Database\Store.sql",'w')
f2.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Store(storeId,storeCity, storeAddress, storeCountry, storePostCode,storePhoneNum,storeManagerEmpId) VALUES\n\n")
f2.close()
f3=open("C:\Python27\Database\Employee.sql",'w')
f3.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Employee(employeeId,employeeFirstName, employeeLastName, employeeAddress, employeeDOB,employeeJobTitle,employeeCity,employeeEmail,employeeMobileNum,employeeDirectDial,employeephExtNum,storeId) VALUES\n")
f3.close()
f4=open("C:\Python27\Database\SIM.sql",'w')
f4.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO SIM(simNUM,simPUK, simRegDate) VALUES\n\n")
f4.close()
#f5=open("C:\Python27\Database\Phone_Number.sql",'w')
#f5.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Phone_Number(phoneNumId,phoneNum, phoneNumRegDate) VALUES\n\n")
#f5.close()
f7=open("C:\Python27\Database\Call.sql",'w')
f7.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO PhoneCall(callNum, callSourceNum, callDestinationNum, callStartTime, callEndTime, phoneId, sourceLocationId, destinationLocationId) VALUES\n\n")
f7.close()
f8=open("C:\Python27\Database\SMS.sql",'w')
f8.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO SMS(smsNum, smsSourceNum,smsDestinationNum,smsSize, smsStartTime,smsEndTime,phoneId,sourceLocationId,destinationLocationId) VALUES\n\n")
f8.close()
f9=open("C:\Python27\Database\Data.sql",'w')
f9.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Data(dataNum,dataStartTime, dataEndTime, phoneId,metaId) VALUES\n\n")
f9.close()
f10=open("C:\Python27\Database\Data_Meta.sql",'w')
f10.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Data_Meta(metaId,dataSourceIP, dataDestinationIP, dataHops, dataPing,dataSize,dataNumPackets,dataLocation,phoneId) VALUES\n\n")
f10.close()
f11=open("C:\Python27\Database\Location.sql",'w')
f11.write("SET FOREIGN_KEY_CHECKS = 0;\n\nINSERT INTO Location(locationId,locationDialingCode, locationCountry) VALUES\n\n")
f11.close()
###################################################END TABLES#####################################################

def Customers():
    #ref f
    a = 0
    while a < 5000:
        
            f =random.randint(0,61) 
            first = str(fname[f])
            
            l = random.randint(0,16)
            last = str(lastn[l])

            day = random.randint(1,30)
            month = random.randint(1,12)
            year = random.randint(1940,2005)

            dob = "{x}/{y}/{z}"
            date = dob.format(x=day, y=month, z=year)

            tre = random.randint(1,3)
            if(tre == 1):
                gender = "male"
            elif(tre ==2):
                gender = "female"
            else:
                gender = "N/A"

            num = str(random.randint(1000000, 9999999))
            number =phonenum.format(num)

            ci = random.randint(0,5)
            cit=str(city[ci])

            t = random.randint(0,13)
            c = random.randint(0,13)
            e = random.randint(0,7)

            to = str(town[t])
            co = str(county[c])
            es = str(estate[e])

            eem = random.randint(1,3)
            mail1 = str(first+last)
            number1 = str(random.randint(0,999))
            
            if(eem ==1):
                em = "{mail}{nu1}@gmail.com"
            elif(eem ==2):
                em = "{mail}{nu1}@yahoo.com"
            else:
                em = "{mail}{nu1}@mail.ru"
            email = em.format(mail=mail1,nu1=number1)
            f=open("C:\Python27\Database\Customer.sql",'a')
            f.write('('+str(a)+',"'+first+'","'+last+'","'+dig+' '+es+' '+to+' Co.'+co+'",NOW(),"'+gender+'","'+cit+'","'+email+'",'+str(random.randint(0,100))+'),\n\n')
        
            a = a+1
            fil= "No.{0} Customer has been made."
            print(fil.format(a))

            if a ==5000:
                f.write('('+str(a)+',"'+first+'","'+last+'","'+dig+' '+es+' '+to+' Co.'+co+'",NOW(),"'+gender+'","'+cit+'","'+email+'",'+str(random.randint(0,100))+');\n\n')
                print("Done.")

def Employee():
    #ref f3
    
    b = 0
    while b <100:
        
        jo = random.randint(0,13)
        jobt = str(jobtitle[jo])

        f =random.randint(0,61) 
        first = str(fname[f])
        
        l = random.randint(0,16)
        last = str(lastn[l])

        day = random.randint(1,30)
        month = random.randint(1,12)
        year = random.randint(1940,2005)

        dob = "{x}/{y}/{z}"
        date = dob.format(x=day, y=month, z=year)

        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)

        ci = random.randint(0,5)
        cit=str(city[ci])

        t = random.randint(0,13)
        c = random.randint(0,13)
        e = random.randint(0,7)

        to = str(town[t])
        co = str(county[c])
        es = str(estate[e])

        eem = random.randint(1,3)
        mail1 = str(first+"_"+last)
        number1 = str(random.randint(0,999))

        
        if(eem ==1):
            em = "{mail}{nu1}@phonejackal.com"
        elif(eem ==2):
            em = "{mail}{nu1}@phonejackal.ie"
        else:
            em = "{mail}{nu1}@phonejackal.co.uk"
        email = em.format(mail=mail1,nu1=number1)
        f3=open("C:\Python27\Database\Employee.sql",'a')
        f3.write('('+str(b)+',"'+first+'","'+last+'","'+dig+' '+es+' '+to+' Co.'+co+'",NOW(),"'+jobtitle[0]+'","'+cit+'","'+email+'","'+number+'","'+str(random.randint(0,999))+'","'+str(random.randint(0,9999))+'","'+str(ci)+'"),\n\n')

        b = b+1
        fil= "No.{0} Employee has been made."
        print(fil.format(b))
        f3.close()

        if b ==100:
            f3.write('('+str(b)+',"'+first+'","'+last+'","'+dig+' '+es+' '+to+' Co.'+co+'",NOW(),"'+jobt+'","'+cit+'","'+email+'","'+number+'","'+str(random.randint(0,999))+'","'+str(random.randint(0,9999))+'","'+ci+'");\n\n')
            print("Done.")
            f3.close()

def Account():
    #ref j (accountNumber, accountCreationDate, accountType,accountManagerEmpId,customerId,phoneNumId,simNum,pricePlanId)
    
    c1 = 0
    while c1 <5000:
        f =random.randint(0,61) 
        first = str(fname[f])
        
        l = random.randint(0,16)
        last = str(lastn[l])

        day = random.randint(1,30)
        month = random.randint(1,12)
        year = random.randint(2005,2014)

        dob = "{x}/{y}/{z}"
        date = dob.format(x=day, y=month, z=year)

        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)

        eem = random.randint(1,3)
        mail1 = str(first+"_"+last)
        number1 = str(random.randint(0,999))
        r = random.randint(0,20)
        if r == 15:
            t = "Corporate"
        else:
            t = "Personal"
        
        j=open("C:\Python27\Database\Account.sql",'a')
        j.write('('+str(c1)+',NOW(),"'+t+'",'+str(random.randint(0,100))+','+str(c1)+','+str(c1)+','+str(c1)+','+str(random.randint(0,15))+'),\n\n')

        c1 = c1+1
        fil= "No.{0} account has been made."
        print(fil.format(c1))

        if c1 ==5000:
            j.write('('+str(c1)+',NOW(),"'+t+'",'+str(random.randint(0,100))+','+str(c1)+','+str(c1)+','+str(c1)+','+str(random.randint(0,15))+');\n\n')
            print("Done.")
            j.close()

def Store():
    #ref f2
    c2 =0
    for i in range(0,30):

        cit = city[i]
        
        if(cit == city[2]):
            country = "England"
        else:
            country = "Ireland"
            
        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)
        f2=open("C:\Python27\Database\Store.sql",'a')
        f2.write('('+str(i)+',"'+cit+'","'+storeaddr[i]+'","'+country+'",'+postcode[i]+','+number+','+str(num)+'),\n\n')

        c2 = c2+1
        fil= "No.{0} Store has been made."
        print(fil.format(c2))
        f2.close()

        if i ==30:
            f2.write('('+str(i)+',"'+cit+'","'+storeaddr[i]+'","'+country+'",'+postcode[i]+','+number+','+str(num)+');\n\n')
            print("Done.")
            f2.close()

def Phone():
    #ref f1 (phoneId,phoneModel, phoneIMEI, phonePrice)
    a33 = 0

    while a33 <5000:

        phm = random.randint(0,9)
        phone = PhoneModel[phm]

        imei = random.randint(100000000000,999999999999)
        price = PhonePrice[phm]
        f1=open("C:\Python27\Database\Phone.sql",'a')
        f1.write('('+str(a33)+',"'+phone+'",'+str(imei)+','+str(price)+'),\n\n')

        a33 = a33+1
        fil= "No.{0} Phone has been made."
        print(fil.format(a33))
        if a33 == 5000:
              f1.write('('+str(a33)+',"'+phone+'",'+str(imei)+','+str(price)+');')
              print("Phone Table Done.")
              f1.close()
        
        

def Data():
    #ref f9 (dataNum,dataStartTime, dataEndTime, phoneId,metaId)
    an = 0

    while an <30000:
        PId = random.randint(0,5000)
        source = random.randint(0,19)
        destination = random.randint(0,19)
        day = random.randint(1,30)
        month = random.randint(1,12)
        year = random.randint(2005,2014)
        hour = random.randint(0,24)
        minute = random.randint(0,59)
        second = random.randint(0,59)
        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)
        dob = "{x}/{y}/{z} {h}:{m}:{s}"
        date = dob.format(x=day, y=month, z=year,h=hour,m=minute,s=second)
        duration = random.randint(2,20)
        finish = dob.format(x=day, y=month, z=year,h=hour,m=minute+duration,s=second+duration)
        f9=open("C:\Python27\Database\Data.sql",'a')
        f9.write('('+str(an)+',NOW(),NOW(),'+str(PId)+','+str(an)+')\n\n,')
        an = an+1
        fil= "No.{0} Data has been made."
        print(fil.format(an))
        if an == 30000:
            f9.write('('+str(an)+',NOW(),NOW(),'+str(PId)+','+str(an)+');')
            f9.close()
            print("Data Table finished.")
        

def Data_Meta():
    #ref f10 (metaId,dataSourceIP, dataDestinationIP, dataHops, dataPing,dataSize,dataNumPackets,dataLocation,phoneId)

    met = 0

    while met <30000:
        ip1= str(random.randint(0,268))
        ip2= str(random.randint(0,268))
        ip3= str(random.randint(0,268))
        ip4= str(random.randint(0,268))
        IP = "{a}.{b}.{c}.{d}"
        IpP = IP.format(a=ip1,b=ip2,c=ip3,d=ip4)
        ip5= random.randint(0,268)
        ip6= random.randint(0,268)
        ip7= random.randint(0,268)
        ip8= random.randint(0,268)
        IP2 = "{a}.{b}.{c}.{d}"
        Ip2 = IP2.format(a=ip5,b=ip6,c=ip7,d=ip8)

        hop = random.randint(2,5000)
        ping = random.randint(33,800)
        size = random.randint(32,42000)
        packets = random.randint(3,4000)
        location = random.randint(1,32)
        f10=open("C:\Python27\Database\Data_Meta.sql",'a') 
        f10.write('('+str(met)+',"'+IpP+'","'+Ip2+'",'+str(hop)+','+str(ping)+','+str(size)+','+str(packets)+',"'+str(location)+'",'+str(random.randint(0,5000))+'),\n\n')
        met = met+1

        fil= "No.{0} Data_Meta has been made."
        print(fil.format(met))

        if met == 30000:
            f10.write('('+str(met)+',"'+Ip+'","'+Ip2+'",'+str(hop)+','+str(ping)+','+str(size)+','+str(packets)+',"'+str(location)+'",'+str(random.randint(0,5000))+');')
            f10.close()
            print("Data_Meta Table finished")
        
    

def SIM():
    #ref f4 (simNUM,simPUK, simRegDate, phoneNumId)
    a3 = 1
    while a3 <5000:
        
        NUM = random.randint(1000,9999)
        PUK = random.randint(1000,9999)
        
        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)
        f4=open("C:\Python27\Database\SIM.sql",'a')
        f4.write('('+str(a3)+','+str(PUK)+',NOW()),\n\n')
        a3 = a3+1

        fil= "No.{0} SIM has been made."
        print(fil.format(a3))
        if a3 == 5000:
            f4.write('('+str(a3)+','+str(PUK)+',NOW());')
            f4.close()
            print("SIM table finished.")
        

def Location():
    #ref f11 (locationId,locationDialingCode, locationCountry)
    b32 = 0

    for i in range(0,19):
        Country1 = Country[i]
        Code = CountryCode[i]
        f11=open("C:\Python27\Database\Location.sql",'a')
        f11.write('('+str(i)+','+str(Code)+',"'+Country1+'"),')
        if i == 19:
            f11.write('('+str(i)+','+str(Code)+',"'+Country1+'");')
            f11.close()
            print("Locations have been made")

    

def Call():
    #ref f7 (callNum, callSourceNum, callDestinationNum, callStartTime, callEndTime,phoneId,sourceLocationId,destinationLocationId)
    n = 1
    while n <30000:
        PId = random.randint(0,5000)
        source = random.randint(0,19)
        destination = random.randint(0,19)
        day = random.randint(1,30)
        month = random.randint(1,12)
        year = random.randint(2005,2014)
        hour = random.randint(0,24)
        minute = random.randint(0,59)
        second = random.randint(0,59)
        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)
        num1 = str(random.randint(1000000, 9999999))
        number1 =phonenum.format(num1)
        dob = "{x}/{y}/{z} {h}:{m}:{s}"
        date = dob.format(x=day, y=month, z=year,h=hour,m=minute,s=second)
        duration = random.randint(2,20)
        finish = dob.format(x=day, y=month, z=year,h=hour,m=minute+duration,s=second+duration)
        f7=open("C:\Python27\Database\Call.sql",'a')
        f7.write('('+str(n)+','+number+','+number1+',NOW(),NOW(),'+str(random.randint(0,5000))+','+str(random.randint(1,32))+','+str(random.randint(1,32))+'),\n\n')
        n = n+1
        fil= "No.{0} Call has been made."
        print(fil.format(n))
        
        if n ==30000:
            f7.write('('+str(n)+','+number+','+number1+',NOW(),NOW(),'+str(random.randint(0,5000))+','+str(random.randint(1,32))+','+str(random.randint(1,32))+');\n\n')
            f7.close()
            print("Call Table Finished")
def SMS():
    #ref f8 (smsNum, smsSourceNum,smsDestinationNum,smsSize, smsStartTime,smsEndTime,phoneId,sourceLocationId,destinationLocationId)
    a44 = 0
    while a44 <30000:
      
        day = random.randint(1,30)
        month = random.randint(1,12)
        year = random.randint(2005,2014)
        hour = random.randint(0,24)
        minute = random.randint(0,59)
        second = random.randint(0,59)
        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)
        num1 = str(random.randint(1000000, 9999999))
        number1 =phonenum.format(num1)
        dob = "{x}/{y}/{z} {h}:{m}:{s}"
        date = dob.format(x=day, y=month, z=year,h=hour,m=minute,s=second)
        finish = dob.format(x=day, y=month, z=year,h=hour,m=minute,s=second+15)
        size = random.randint(0,24000)
        f8=open("C:\Python27\Database\SMS.sql",'a')
        f8.write('('+str(a44)+','+number+','+number1+','+str(size)+',NOW(),NOW(),'+str(random.randint(0,5000))+','+str(random.randint(1,32))+','+str(random.randint(1,32))+'),\n\n')

        a44 = a44+1
        fil= "No.{0} SMS has been made."
        print(fil.format(a44))

        if a44 == 100000:
            f8.write('('+str(a44)+','+number+','+number1+','+str(size)+',NOW(),NOW(),'+str(random.randint(0,5000))+','+str(random.randint(1,32))+','+str(random.randint(1,32))+');\n\n')
            f8.close()
            print("SMS Table Finished")
            

def Phone_Number():
    #ref f5
    a1 = 1

    while a1 < 5000:

        day = random.randint(1,30)
        month = random.randint(1,12)
        year = random.randint(2005,2014)
        hour = random.randint(0,24)
        minute = random.randint(0,59)
        second = random.randint(0,59)

        dob = "{x}-{y}-{z} {C}:{B}:{A}"
        date = dob.format(x=year, y=month, z=day,A=hour,B=minute,C=second)
        
        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)

        f5=open("C:\Python27\Database\Phone_Number.sql",'a')
        f5.write('('+str(a1)+','+number+',NOW()),\n\n')

        a1 = a1+1
        fil= "No.{0} Phone number has been made."
        print(fil.format(a1))

        if a1 == 5000:
            f5.write('('+str(a1)+','+number+',NOW());\n\n')
            f5.close()








#Location()           
#Phone_Number()
#Account()
#Customers()
#Employee()
#Phone()
Store()


    

                                                                                                                                           
    
