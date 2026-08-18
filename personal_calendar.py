import calendar  # python module
from datetime import datetime
 
while True:
   print("\n=================================================================")
   print("              WELCOME TO THE PERSONAL CALENDAR                   ")
   print("=================================================================")

#(=======Choices from user==========)

   print("1  SHOW YEAR CALENDAR")
   print("2  SHOW MONTHS CALENDAR")
   print("3  FIND SUNDAYS ")
   print("4  FIND WEEKENDS")
   print("5  FIND DAY OF BIRTHDAY")
   print("6  CALCULATE DATE DIFFERENCE")
   print("7  QUIT")

   try:
       choice=int(input("Enter Your Choice: "))            # Getting choices from the user
   except ValueError:
    print("❌ Please enter a number between 1 and 7.")
    continue     

#(========For getting year=========)
   if choice==1:
        year = int(input("Enter the Year: "))
        print(calendar.calendar(year))            #  function of calendar module for inserting  year calendar in output



#(========For Month Of The Year==========)
   elif choice==2:
        year=int(input("Enter Year: "))
        month=int(input("Enter Month(1-12):"))
        print(calendar.month(year,month))          # Function of calendar module for showing month


#(===========For Finding Sunday's In a Specific Month=============)
   elif choice==3:
        year=int(input("Enter the Year:"))
        month=int(input("Enter the Month(1-12):"))
        print("SUNDAY'S ARE")
        for week in calendar.monthcalendar(year,month):         # For Finding Specific day i have use for loop 
           sunday=week[calendar.SUNDAY]
           if sunday !=0:
               print(sunday)

 #(============For Finding Weekend's In Month==================)       
   elif choice==4:
        year=int(input("Enter the Year:"))
        month=int(input("Enter the Month(1-12):"))
        for week in calendar.monthcalendar(year,month):          # For Finding A Specific Day
            saturday=week[calendar.SATURDAY]
            sunday=week[calendar.SUNDAY]
            if saturday !=0:
                print("WEEKEND'S ARE:-")
                print("🏖️ Saturday:",saturday)

            if sunday !=0:
                print("☀️ Sunday:",sunday)


#(==============For Finding Birthday From Year , Month And Day==============)
   elif choice==5:
        print("BIRTHDAY FINDER")
        try:
    
            day=int(input("Enter the Day:"))
            month=int(input("Enter the Month(1-12):"))
            year=int(input("Enter the Year:"))
            birthday=datetime(year,month,day)                                   # Function Of datetime ,creates a date object representing 
            print("🎂 Your birthday was on 🎉",birthday.strftime("%A"))        #birthday.strftime print's the What day of the week was this date?
        except ValueError:
          print("❌ Invalid date! Please enter a valid date.")    
#(================For Finding Date's difference in Two dates=================)
   elif choice==6:
        try:
        
         print("\nFor the First date")
        
         day1=int(input("Day: "))
         month1=int(input("Month:"))
         year1=int(input("Year:"))

         print("\nFor the Second Date")

         day2=int(input("Day: "))
         month2=int(input("Month:"))
         year2=int(input("Year:"))

         date1=datetime(year1,month1,day1)                         #datetime converts them into date
         date2=datetime(year2,month2,day2)                         #datetime converts them into date
         difference=abs(date1-date2)                                          #Python calculates
         print("Difference between the date is:",difference.days,"days")
        except ValueError:
         print("❌ Invalid date! Please enter a valid date.")
         

#(=============For Quiting the program==================)
   elif choice==7:
        print("Thanks for visiting your Personal Calendar! 📅")
        print("See you again! 👋")
        break

#(============For Invalid Number's=======================)
   else:
        print("Invalid Number")
        