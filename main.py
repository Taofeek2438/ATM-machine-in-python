def full_atm():
    print("WELCOME TO TAOFEEK ATM CENTRE")
    print("Please insert your ATM card")
    pin = int(input("Kindly enter your pin: "))
    if pin == 1520:
        print("1. WITHDRAW\n"
              "2. ENQUIRY\n"
              "3. DEPOSIT\n"
              "4. TRANSFER\n"
              "5. RECHARGE\n")
        operation = int(input("what operation do you want to perform: "))
        if operation == 1:
            print("1. 500\n"
                  "2. 1,000\n"
                  "3. 2,000\n"
                  "4. 5,000\n"
                  "5. 10,000\n"
                  "6. 20,000\n"
                  "7. 30,000\n")
            withdraw = int(input("How much do you want to withdraw: "))
            if withdraw == 1:
                print("You just withdraw #500")
                another_operation = input("Did you want to perform another operation: ")
                if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                    full_atm()
                elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                    print("THANK YOU FOR USING OUR ATM SERVICE")
                else:
                    print("Invalid input")
            elif withdraw == 2:
                print("You just withdraw #1,000")
                another_operation = input("Did you want to perform another operation: ")
                if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                    full_atm()
                elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                    print("THANK YOU FOR USING OUR ATM SERVICE")
                else:
                    print("Invalid input")

            elif withdraw == 3:
                print("You just withdraw #2,000")
                another_operation = input("Did you want to perform another operation: ")
                if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                    full_atm()
                elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                    print("THANK YOU FOR USING OUR ATM SERVICE")
                else:
                    print("Invalid input")

            elif withdraw == 4:
                print("You just withdraw #5,000")
                another_operation = input("Did you want to perform another operation: ")
                if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                    full_atm()
                elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                    print("THANK YOU FOR USING OUR ATM SERVICE")
                else:
                    print("Invalid input")

            elif withdraw == 5:
                print("You just withdraw #10,000")
                another_operation = input("Did you want to perform another operation: ")
                if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                    full_atm()
                elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                    print("THANK YOU FOR USING OUR ATM SERVICE")
                else:
                    print("Invalid input")
            elif withdraw == 6:
                print("You just withdraw #20,000")
                another_operation = input("Did you want to perform another operation: ")
                if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                    full_atm()
                elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                    print("THANK YOU FOR USING OUR ATM SERVICE")
                else:
                    print("Invalid input")
            elif withdraw == 7:
                print("You just withdraw #30,000")
                another_operation = input("Did you want to perform another operation: ")
                if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                    full_atm()
                elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                    print("THANK YOU FOR USING OUR ATM SERVICE")
                else:
                    print("Invalid input")
            else:
                print("Invalid input!!!")
        elif operation == 2:
            print("Kindly use your USSD code to check your your account details ")
            another_operation = input("Did you want to perform another operation: ")
            if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                full_atm()
            elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                print("THANK YOU FOR USING OUR ATM SERVICE")
            else:
                print("Invalid input")
        elif operation == 3:
            print("Kindly visit your nearest bank to deposit")
            another_operation = input("Did you want to perform another operation: ")
            if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                full_atm()
            elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                print("THANK YOU FOR USING OUR ATM SERVICE")
            else:
                print("Invalid input")
        elif operation == 4:
            print("1. Access Bank\t " "2. Jaiz Bank\t"
                  "3. Unity Bank " "4. Union Bank"
                  "5. Polaris Bank " "6. Keystone Bank"
                  "7. First Bank "   "8. FCMB Bank"
                  "9. Wema Bank\t"    "10. GT Bank\t")
            bank = int(input("SELECT THE BANK YOU WANT TO TRANSFER MONEY TO: "))
            if bank <= 10 and bank != 0:
                destination = int(input("Enter the account number: "))
                if destination:
                    print("TRANSACTION SUCCESSFUL ")
                    another_operation = input("Did you want to perform another operation: ")
                    if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                        full_atm()
                    elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                        print("THANK YOU FOR USING OUR ATM SERVICE")
                    else:
                        print("Invalid input")
                else:
                    print("TRANSACTION CANCELED ")
            else:
                print("WRONG INPUT")
        elif operation == 5:
            recharge = int(input("Which do you want to recharge to: "))
            print("1. MTN\n"
                  "2. GLO\n"
                  "3. AIRTEL\n"
                  "4. ETISALAT\n"
                  "5. 9MOBILE\n")
            if recharge <= 5 and recharge != 0:
                number = int(input("Please enter your number: "))
                if number:
                    print("1. 100\n"
                          "2. 200\n"
                          "3. 300\n"
                          "4. 400\n"
                          "5. 500\n"
                          "6. 1,000\n"
                          "7. 2,000\n"
                          "8. 5,000\n"
                          "9. 10,000\n"
                          "10. 20,000\n"
                          "11. 30,000\n")
                    amount = int(input("How much do you want recharge: "))
                    if amount <= 11 and amount != 0:
                        print("THANK YOU FOR USING OUR SERVICE")
                        another_operation = input("Did you want to perform another operation: ")
                        if another_operation == 'Yes' or another_operation == 'YES' or another_operation == 'yes':
                            full_atm()
                        elif another_operation == 'No' or another_operation == 'NO' or another_operation == 'no':
                            print("THANK YOU FOR USING OUR ATM SERVICE")
                        else:
                            print("Invalid input")
                    else:
                        print("Invalid input!!!")
                else:
                    print("TRANSACTION CANCELED")
            else:
                print("You have enter wrong input")
        else:
            print("INCORRECT INPUT")
    else:
        print("INCORRECT PIN")
        full_atm()

full_atm()

