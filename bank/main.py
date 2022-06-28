
import os
import random
import asyncio


class customer_cls():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = random.randrange(75, 125)
        self.stocks = 0

    def buy(self, quantity):
        self.price = random.randrange(int(quantity * 0.5), int(quantity * 1.5))
        print("You can buy " + str(quantity) + " Stocks for " + str(self.price))
        print("type y to buy: ", end='')
        if input() == "y":
            for customer in coustomers:
                if customer.name == self.name:
                    customer.stocks += quantity
                    customer.balance -= self.price
                    print("Your balance is now: " + str(customer.balance))
                    print("Your stocks are now: " + str(customer.stocks))
                    input()
                    break

    def sell(self, quantity):
        sold_price = random.randrange(int(quantity * 0.5), int(quantity * 1.5))
        print("You can sell " + str(quantity) + " Stocks for " + str(sold_price) + " bucks (type y to sell): ", end='')
        if input() == "y":
            self.stocks -= quantity
            self.balance += sold_price
            print("Your balance is now: " + str(self.balance))
            print("Your stocks are now: " + str(self.stocks))
            input()
            os.system('CLS')
        else:
            print("Break")

coustomers = []
coustomer_index = 0


def create_customer(name, password):
    new_customer = customer_cls(name, password)
    coustomers.append(new_customer)
    del new_customer

def return_coustomer_names():
    names = []
    for customer in coustomers:
        names.append(customer.name)
    return names

create_customer("asd", "asd")
coustomers[0].stocks = 20


def bank():
    while True:
        print("Welcome to the bank!")
        print("Please choose an option:")
        print("1. Create an account")
        print("2. Log in")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            os.system('CLS')
            name = input("Name: ")
            password = input("Password: ")

            already_exists = False
            for customer in coustomers:
                if customer.name == name:
                    already_exists = True

            if not already_exists:
                try:
                    create_customer(name, password)
                except TypeError:
                    print("===============Type Error===============")
                print("Your account has been created!")
                print("You can now login to your account")
                input("Press enter to continue")


            else:
                print("This name is already taken")
                input("Press enter to continue")
            os.system('CLS')
        elif choice == "2":

            os.system('CLS')
            name = input("Name: ")
            password = input("Password: ")
            not_found_index = 0
            for customer in coustomers:
                if customer.name == name and customer.password == password:
                    print("Welcome back " + name + " your balance is: " + str(customer.balance))
                    print("Would you like to make a transaction(s for stocks)? (y/n/s)", end = '')
                    choice = input()
                    if choice == "y":
                        print("Please enter the person you would like to transfer to (type \"ls\" for a list of coustomers) : ", end='')
                        transfer_name = input()

                        if transfer_name == "ls":
                            print("Coustomers: ")
                            print(return_coustomer_names())

                            print("Please enter the person you would like to transfer to: ", end='')
                            transfer_name = input()
                        if transfer_name == "exit":
                            break

                        for customer_to in coustomers:
                            if customer_to.name == transfer_name:
                                print("Enter the amount you would like to transfer: ", end='')
                                transfer_amount = int(input())
                                if transfer_amount > 0:
                                    if transfer_amount <= customer.balance:
                                        customer_to.balance += transfer_amount
                                        customer.balance -= transfer_amount
                                        print("Your balance is now: " + str(customer.balance))
                            else:
                                not_found_index += 1
                        #if not_found_index < len(coustomers):
                        #    print("Coustomer not found")
                    elif choice == "s":

                        print("You got " + str(customer.stocks) + " stocks")
                        print("Buy or sell stocks? (b/s)", end='')
                        choice_s = input()
                        if choice_s == "b":
                            print("Buy stocks(ammout of stocks you want to buy): ", end='')
                            money_ammount = input()
                            customer.buy(int(money_ammount))
                        elif choice_s == "s":
                            print("Sell stocks for(ammount of stocks you want to sell): ", end='')
                            money_ammount = input()
                            customer.sell(int(money_ammount))

            os.system('CLS')

        elif choice == "3":
            print("Thank you for using the bank!")
            break
        input("Press enter to continue")
        os.system('CLS')

bank()


