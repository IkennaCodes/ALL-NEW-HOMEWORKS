while True:
    try:
        age = int(input("Enter your age!"))  

        if age < 0 or age > 100:
            raise ValueError("Your age is either too low or high!")

        print(f"Your age is {age}, cool! 😎")  
        break

    except ValueError:
        print("Error fixed ✅")
        print("Reason: Your age is either too low or high!")
