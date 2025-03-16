print("Baskin Robbins have developed a Kiosk to help the customers "
"in buying their different ice cream pack options. "
"Customers can enter the no of persons and it will suggest which pack to go for.")

user = int(input("Please type the number of people"))
if user == 1:
    print("Small or Regular")
elif user == 2:
    print("Double")
elif user == 3 or user == 4:
    print("Family Pack")
elif user == 5 or user == 6:
    print("Happiness Pack")

else:
   print("We do not have any packs for that many people!")
