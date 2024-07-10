
print("WE SHOULD KNOW ABOUT THE UNIVERSE WHICH WAS EARLY CREATED BY THE GOD.....")
print()
print()
print("                                                                        ****THE UNIVERSE****")
print()
print()

#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="sqladmin123*")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists Astronomy")
mycursor.execute("use Astronomy")
#creating required tables 
mycursor.execute("create table if not exists Solar_system(sno char(44) primary key,Name_planets varchar(130),surface_temp char(190),surface_gravity char(10),moon varchar(120))")
mycursor.execute("create table if not exists Galaxies(sno char(44) primary key,Name_galaxy varchar(130),Official_name char(120),solar_system_or_star char(190),balance int(6))")
mycursor.execute("create table if not exists Stars(sno char(44) primary key,name_stars varchar(30),State char(20),Surface_gravity char(10),surface_temp varchar(160),balance int(6))")
mycursor.execute("create table if not exists Exoplanets(sno char(44) primary key,Name_exoplanets varchar(190),Surface_gravity char(120),surface_temp char(10),Suitable_for_life varchar(200),Nearer_star varchar(120),balance int(6))")
mydb.commit()
while(True):
    
    print("1=Fill Information of solar system")
    print()
    print("2=Fill Information of Galaxies")
    print()
    print("3=Fill Information of Stars")
    print()
    print("4=Fill Information of Exoplanets")
    print()
    print("5=Display information of solar system")
    print()
    print("6=Display information of Galaxies")
    print()
    print("7=Display information of Stars")
    print()
    print("8=Display information of Exoplanets")
    print()
    print("9=Exit")
    print()
    print("10=About us")
    print()
    print()
    ch=int(input("Enter your choice:"))
    print()
    print()

    

    if(ch==1):
        print()
        Sno=str(input("Enter the serial number of the Planet :"))
        Name_of_planet=input("Enter the name of the planet:")
        Moons=str(input("Enter the number of moons of  {0}:".format(Name_of_planet)))
        Surface_gravity=str(input("Enter surface gravity of {0}:".format(Name_of_planet)))
        Surface_temp=str(input("Enter the surface temperature of the planet : "))
        balance=0
        mycursor.execute("insert into Solar_system values('"+Sno+"','"+Name_of_planet+"','"+Moons+"','"+Surface_gravity+"','"+Surface_temp+"')")
        mydb.commit()
        print()
        print("Information is successfully filled!!!")
        print()
        print()


    elif(ch==2):
        print()
        Sno=str(input("Enter the serial number of Galaxy :"))
        Name_of_galaxy=str(input("Enter the name of the Galaxy :"))
        Official_name=str(input("enter {0}'s official name(like NGC_224)".format(Name_of_galaxy)))
        solar_system_or_star=str(input("enter the name of solar system or star inside {0}...:".format(Name_of_galaxy)))
        balance=0     
        mycursor.execute("insert into Galaxies values('"+Sno+"','"+Name_of_galaxy+"','"+Official_name+"','"+solar_system_or_star+"','"+str(balance)+"')")
        mydb.commit()
        print("Information is successfully filled!!!")
        print()
        print()

        

    elif(ch==3):
        print()
        Sno=str(input("Enter the serial number of the Star:"))
        Name_of_star=input("Enter the name of the Star:")
        state=str(input("Enter the state of the {0}(red giant,white dwarf,etc) : ".format(Name_of_star)))
        Surface_gravity=str(input("Enter surface gravity of the {0}:".format(Name_of_star)))
        Surface_temp=str(input("Enter the surface temperature of the Star : "))
        balance=0
        mycursor.execute("insert into Stars values('"+Sno+"','"+Name_of_star+"','"+state+"','"+Surface_gravity+"','"+Surface_temp+"','"+str(balance)+"')")
        mydb.commit()
        print("Information is successfully filled!!!")
        print()
        print()


    elif(ch==4):
        print()
        Sno=str(input("Enter the serial number of Planets:"))
        Name_of_exoplanets=input("Enter the name of the exoplanet:")
        Surface_gravity=str(input("Enter surface gravity of the exoplanet:"))
        Surface_temp=str(input("Enter the surface temperature of the exoplanet : "))
        Suitable_for_life=input("Is the planet is suitable for life?:")
        Nearer_star=input("Enter the name of the nearer star or planet or any other objects...:")
        balance=0
        mycursor.execute("insert into Exoplanets values('"+Sno+"','"+Name_of_exoplanets+"','"+Surface_gravity+"','"+Surface_temp+"','"+Suitable_for_life+"','"+Nearer_star+"','"+str(balance)+"')")
        mydb.commit()
        print("Information is successfull filled!!!")
        print()
        print()


    elif(ch==5):
        sno=str(input("Enter the sno of the planet :"))
        mycursor.execute("select * from solar_system where sno='"+sno+"'")
        found=0
        for i in mycursor:
            if i!=():
                print()
                print(i)
                print()
                print()
                found=1
        if found==0:
            print()
            print("No record Found.....!!!! Try entering some records using the below menu.")
            print()
            print()
            
            
    elif(ch==6):
    
        sno=str(input("Enter the sno of the Galaxy :"))
        mycursor.execute("select * from Galaxies where sno='"+sno+"'")
        found=0
        for j in mycursor:
            if j!=():
                print()
                print(j)
                print()
                print()
                found=1
                
        if found==0:
            print()
            print("@@@@@@@@@@@@@@No Record Found....!!  Try entering some records using other options@@@@@@@@@@@@@@")
            print()
            print()


            
    elif(ch==7):
        sno=str(input("Enter the sno of the Star :"))
        mycursor.execute("select * from Stars where sno='"+sno+"'")
        found=0
        for a in mycursor:
            if a!=():
                print()
                print(a)
                print()
                print()
                found=1
                
        if found==0:
            print()
            print("No Record Found....!!  Try entering some records using other options")
            print()
            print()
            

            
    elif(ch==8):
        sno=str(input("Enter the sno of the Exoplanet :"))
        mycursor.execute("select * from Exoplanets where sno='"+sno+"'")
        found=0
        for o in mycursor:
            if o!=():
                print()
                print(o)
                print()
                print()
                found=1
                
        if found==0:
            print()
            print("No Record Found....!!  Try entering some records using other options")
            print()
            print()
               


    elif(ch==9):
        print("                                Thanks for Entering and Knowing about our Universe .....!")
        break

    elif(ch==10):
        print("PROGRAMMED BY: Dhanush N,Kathirvelan S,Rohith Krishna S")
        print("IDE's used : Python 3.8,Mysql 8.1")
        print("Under guidenence of: M.Tamilarasi")
        print("Class 12 Computer science")
        print("Batch:2020-2021")
        print(                            "THANK YOU"           )
        print()
        print()
        print()
