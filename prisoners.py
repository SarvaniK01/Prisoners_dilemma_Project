print("********************PRISONER'S DILEMMA********************")
print("\nEnter the prisoner's choice as 'C' for confessed and 'NC' for not confessed(TYPE IN CAPITALS ONLY)")
print("**********************************************************")
def pd():
    ch=input("Do you want to Start?(y/n):")
    while(ch=="y"):
        prisoner1=(input("Enter the 1st prisoner's choice:"))
        prisoner2=(input("Enter the 2nd prisoner's choice:"))

        if (prisoner1=="NC" and prisoner2=="NC"):
            print("Both the prisoners DID NOT CONFESS")
            print("Prisoner 1 gets 2 years Jail")
            print("Prisoner 2 gets 2 years of Jail")
            ch=input("Do you want to continue?(y/n):")

        elif(prisoner1=="NC" and prisoner2=="C"):
            print("Prisoner 1 did not confess \n He gets 10 years of Jail")
            print("Prisoner 2 confessed \n He gets released")
            ch=input("Do you want to continue?(y/n):")

        elif(prisoner1=="C" and prisoner2=="NC"):
            print("Prisoner 1 confesses \n He gets released")
            print("Prisoner 2 does not confess \n He gets 10 years of Jail")
            ch=input("Do you want to continue?(y/n):")

        elif(prisoner1=="C" and prisoner2=="C"):
            print("Prisoner 1 confesses \n He gets 5 years of Jail")
            print("Prisoner 2 confesses \n He gets 5 years of Jail")
            ch=input("Do you want to continue?(y/n):")

        else:
            print("Wrong input.try again")
            ch=input("Do you want to continue?(y/n):")
pd()