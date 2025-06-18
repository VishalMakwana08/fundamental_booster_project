#welcome message
    
print("Welcome This Is Personal Data Collector Python Program Created By 'Vishal Makwana'")

#collect information from the user
name=input("Please Enter Your Name:")
age=int(input("Please Enter Your Age:"))
height=float(input("Please Eneter Your Height In Meters:"))
num=int(input("Please Enter Your Favorite Number:"))

#Data Processing
print("Name:",name,"(",type(name),"Memory Address:",id(name))
print("Age:",age,"(",type(age),"Memory Address:",id(age))
print("Height:",height,"(",type(height),"Memory Address:",id(height))
print("Favorite Number:",num,"(",type(num),"Memory Address:",id(num))
current_year=int(input("Enter Current Year:"))
print("\nYour Birth Year Is Approximately:",(current_year-age),"(Based On Your Age Of",age,")")

#Display Results
print("Dear User Here Are Your Information That Are Store Safely...")
print("Your Name Is:",name)
print("Your Age Is:",age)
print("Your Height Is:",height)
print("Your Favorite Number:",num)
print("\nDear User Thank You For Use Our Personal Data Collector.Good Bye!")