print("Welcome to the tip calculator.")

Bill = input("What was the total bill?  $  ")
Tip = input("What percentage tip would you like to give? 10,12 or 15?    ")

People = input("How many people to split the bill?  ")


dividedbill = float(float(Bill)/float(People))

a =  round(dividedbill + dividedbill*int(Tip)/100 , 2)

print(f"Each person should pay: $ {a} ")
