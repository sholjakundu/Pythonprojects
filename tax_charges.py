"""
Calculate the total to charge for an order from an online store in Canada
"""
country=input("What country are you from? (enter in capital letters) ")
totalAmount=float(input("What is your total order amount? "))
if not country =="CANADA":
    print("Total amount with taxes is", totalAmount)
if country == "CANADA":
    province = input("What is your province from Canada? (Enter in capital letters only) ")
    if province == "ALBERTA" :
         print("Total amount with taxes is", totalAmount+(0.05*totalAmount))
    elif  province == "ONTARIO" or province =="NEW BRUNSWICK" or province =="NOVA SCOTIA":
         print("Total amount with taxes is",totalAmount+(0.13*totalAmount))
    else:
         print("Total amount with taxes is" ,totalAmount + (0.11 * totalAmount))
