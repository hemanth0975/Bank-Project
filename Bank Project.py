import csv
import datetime
import os


class Bank:
    bank_name = "SBI"
    location = "ALKAPURI"
    ifsc_code = "SBI0011"
    no_of_customer = 0

    customer_details = {}

    transaction_details = {}

    def __init__(self, name, age, gender, address, phone, adhaar_no, pinno, balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = self.validate_phone(phone)
        self.adhaar_no = self.validate_adhaar(adhaar_no)
        self.pinno = self.validate_pinno(pinno)
        self.balance_ = balance

        # INCREMENTING THE CUSTOMERS NUMBERS AND CREATING THE ACCOUNT NUMBER
        self.increment_customer()
        self.acc_num = 500 + self.no_of_customer

        # ADDING THE CUSTOMER METHOD
        self.add_customer(self.acc_num, self)
        # self.display_key_val(self.acc_num)

    @classmethod
    def increment_customer(cls):
        cls.no_of_customer += 1

    @classmethod
    def add_customer(cls, acc_num, object_address):
        cls.customer_details[
            acc_num] = object_address  #._dict#[dict_ key word is used when we use all customer details]

    @staticmethod
    def validate_phone(phone_number):
        if len(str(phone_number)) == 10 and str(phone_number).isdigit():
            return phone_number
        else:
            raise Exception("ENTER VALID (10 DIGIT) MOBILE NUMBER")

    @staticmethod
    def validate_adhaar(adhaar_no):
        if len(str(adhaar_no)) == 12 and str(adhaar_no).isdigit():
            return adhaar_no
        else:
            raise Exception("ADHAAR NUMBER LENGTH SHOULD BE 12-DIGITS")

    @staticmethod
    def validate_pinno(pinno):
        if len(str(pinno)) == 4 and str(pinno).isdigit():
            return pinno
        else:
            raise Exception("ENTER VALID 4 DIGIT NUMBER: ")

    @classmethod
    def add_new_customer(cls):
        print("-------------------adding new customer---------")
        adhaar_num = int(input("ENTER YOUR ADHAAR NUMBER :"))

        for acc_num in cls.customer_details:
            if adhaar_num == cls.customer_details[acc_num].adhaar_no:
                print("USER ALREADY EXIST")
                break
        else:
            name = input("Enter your name :")
            phone = int(input("Enter your mobile number :"))
            age = int(input("Enter your age :"))
            gender = input("Enter your gender :")
            address = input("Enter your address :")
            adhaar = adhaar_num
            pinno = int(input("Enter your pin no :"))
            min_balance = int(input("Enter your min balance :"))

            c = cls(name, age, gender, address, phone, adhaar, pinno, min_balance)

    @classmethod
    def display_balance(cls, chance=1):

        print("\n---------------BALANCE METHOD---------------\n")
        if chance == 4:
            print("ATTEMTS FOR BALANCE ENQUIRY ARE OVER")
            return

        user_acc_num = int(input("Enter your account number :"))
        user_pin_num = int(input("Enter your pin number :"))

        if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:
            print(f"your current acc balance is rs.{cls.customer_details[user_acc_num].balance_}")

        elif user_acc_num in cls.customer_details and user_pin_num != cls.customer_details[user_acc_num].pinno:
            print("invalid user password")

        else:
            print("invalid user details")
            cls.display_balance(chance + 1)

    @classmethod
    def deposit(cls, try_=0):

        print("\n---------------Deposite Method---------------\n")
        if try_ == 3:
            print("ATTEMPTS OVER")
            return

        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER : "))
        user_pin_num = int(input("ENTER YOUR PIN NUMBER : "))

        if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:
            amount = int(input("ENTER YOUR DEPOSITE AMOUNT :"))

            if amount > 0:
                cls.customer_details[user_acc_num].balance_ += amount
                print(
                    f"{amount} have been credited to your account and your current account balance Rs.{cls.customer_details[user_acc_num].balance_}")

                if user_acc_num not in cls.transaction_details:
                    cls.transaction_details[user_acc_num] = [{"DATE": datetime.datetime.now(),
                                                              "TYPE": "CREDIT",
                                                              "AMOUNT": amount,
                                                              "BALANCE": cls.customer_details[user_acc_num].balance_}]
                else:
                    cls.transaction_details[user_acc_num] += [{"DATE": datetime.datetime.now(),
                                                               "TYPE": "CREDIT",
                                                               "AMOUNT": amount,
                                                               "BALANCE": cls.customer_details[user_acc_num].balance_}]
            else:
                print("enter valid amount")

        else:
            print("invalid user details")
            cls.deposit(try_ + 1)

    @classmethod
    def withdraw(cls, chance=1):

        print("\n---------------Withdraw Method---------------\n")
        if chance == 4:
            print("ATTEMPTS OVER")
            return

        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER : "))
        user_pin_number = int(input("ENTER YOUR PIN NUMBER : "))

        if user_acc_num in cls.customer_details and user_pin_number == cls.customer_details[user_acc_num].pinno:
            amount = int(input("ENTER WITHDRAW AMOUNT : "))

            if amount <= cls.customer_details[user_acc_num].balance_:
                cls.customer_details[user_acc_num].balance_ -= amount
                print(
                    f"{amount} have been debited from your account and your current account balance is Rs.{cls.customer_details[user_acc_num].balance_}")

                if user_acc_num not in cls.transaction_details:
                    cls.transaction_details[user_acc_num] = [{"DATE": datetime.datetime.now(),
                                                              "TYPE": "DEBITED",
                                                              "AMOUNT": amount,
                                                              "BALANCE": cls.customer_details[user_acc_num].balance_}]
                else:
                    cls.transaction_details[user_acc_num] += [{"DATE": datetime.datetime.now(),
                                                               "TYPE": "DEBITED",
                                                               "AMOUNT": amount,
                                                               "BALANCE": cls.customer_details[user_acc_num].balance_}]

            else:
                print("INSUFICIENT BALANCE")

        else:
            print("invalid user details")
            cls.withdraw(chance + 1)

    @classmethod
    def pin_change(cls, chance=0):

        print("\n---------------PIN CHANGE METHOD---------------\n")

        if chance == 3:
            print("ATTEMPTS FOR PIN CHANGE ARE COMPLETED")
            return

        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER : "))
        user_pin_num = int(input("ENTER YOUR PIN NUMBER :"))

        if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:

            new_pin = int(input("ENTER YOUR NEW PIN NUMBER :"))
            conform_new_pin = int(input("CONFORM YOUR PIN NUMBER :"))

            if new_pin == conform_new_pin:
                cls.customer_details[user_acc_num].pinno = new_pin
                print("PIN CHANGED SUCCESSFULL")

        else:
            print("INVALID USER DETAILS")
            cls.pin_change(chance + 1)

    @classmethod
    def change_user_details(cls, chance=1):

        print("\n---------------Change User Details METHOD---------------")

        if chance == 4:
            print("ATTEMTS FOR NAME CHANGE ARE COMPLETED")
            return

        user_acc_num = int(input("ENTER YOR ACCOUNT NUMBER :"))
        user_pin_num = int(input("ENTER YOUR PIN NUMBER :"))

        if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:

            print("\nENTER 1 FOR CHANGE NAME :\nSELECT 2 FOR CHANGE PHONE NUMBER :\nSELECT 3 FOR CHANGE PIN NUMBER : ")

            select = int(input("ENTER A NUMBER : "))

            match select:
                case 1:

                    print("---------------NAME CHANGE METHOD---------------")

                    user_acc_num = int(input("ENTER YOR ACCOUNT NUMBER :"))
                    user_pin_num = int(input("ENTER YOUR PIN NUMBER :"))

                    if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:

                        new_name = input("ENTER YOUR NEW NAME :")
                        conform_name = input("CONFORM YOUR NEW NAME :")
                        print()

                        if new_name == conform_name:
                            cls.customer_details[user_acc_num].pinno = new_name
                            print("USER NAME HAVE BEEN CHANGED")
                        else:
                            raise Exception("NEW NAME AND CONFORM NAME ARE NOT MATCHING")

                case 2:
                    print("---------------MOBILE NUMBER CHANGE METHOD---------------")

                    user_acc_num = int(input("ENTER YOR ACCOUNT NUMBER :"))
                    user_pin_num = int(input("ENTER YOUR PIN NUMBER :"))

                    if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:

                        new_number = int(input("ENTER YOUR NEW MOBILE NUMBER :"))
                        conform_new_number = int(input("CONFORM YOUR MOBILE NUMBER :"))
                        print()

                        if new_number == conform_new_number:
                            if len(str(new_number)) == 10 and str(new_number).isdigit():
                                cls.customer_details[user_acc_num].pinno = new_number
                                print("PHONE NUMBER CHANGED SUCCESSFUL")
                            else:
                                raise Exception("ENTER VALID 10 DIGIT MOBILE NUMBER")

                case 3:

                    print("---------------PIN CHANGE METHOD---------------")

                    user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER : "))
                    user_pin_num = int(input("ENTER YOUR PIN NUMBER :"))

                    if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:

                        print()
                        new_pin = int(input("ENTER YOUR NEW PIN NUMBER :"))
                        conform_new_pin = int(input("CONFORM YOUR PIN NUMBER :"))

                        if new_pin == conform_new_pin:
                            cls.customer_details[user_acc_num].pinno = new_pin
                            print("PIN CHANGED SUCCESSFULL")

        else:
            print("INVALID USER DETAILS")
            cls.change_user_details(chance + 1)

    @classmethod
    def transfer_method(cls, chance=1):
        print("\n----------------------------- change_user_details---------------------------")
        if chance == 4:
            print("attemts over")
            return
        sender_acc_num = int(input("enter your account number :"))
        sender_pin_num = int(input("enter your pin number :"))

        if sender_acc_num in cls.customer_details and sender_pin_num == cls.customer_details[sender_acc_num].pinno:

            receiver_acc_num = int(input("enter receiver account number :"))
            receiver_pin_num = int(input("enter receiver pin number :"))

            if receiver_acc_num in cls.customer_details and receiver_pin_num == cls.customer_details[receiver_acc_num].pinno:

                amount = int(input("enter the amount to transfer :"))

                if cls.customer_details[sender_acc_num].balance_ >= amount:
                    cls.customer_details[sender_acc_num].balance_ -= amount
                    cls.customer_details[receiver_acc_num].balance_ += amount

                    print(f"money transfered successfully to {cls.customer_details[receiver_acc_num].name}")
                else:
                    print("insufficient balance ")
        else:
            print("invalid details")
            cls.transfer_method(chance + 1)

    @classmethod
    def mini_statement(cls):

        print("\n---------------MINI STATEMENTS---------------\n")

        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER :"))
        user_pin_num = int(input("ENTER YOUR PIN NUMBER :"))

        if user_acc_num in cls.customer_details and user_pin_num == cls.customer_details[user_acc_num].pinno:
            print()

            print("DATE_TIME".center(20), "TYPE".center(25), "AMOUNT".center(20), "BALANCE".center(20), sep=" | ")

            transaction_history = cls.transaction_details[user_acc_num]

            for d in transaction_history:
                print(str(d["DATE"]), str(d["TYPE"]).center(20), str(d["AMOUNT"]).center(20),
                      str(d["BALANCE"]).center(20))

        else:
            print("INVALID USER")

    @classmethod
    def convert_data_into_csv(cls):
        file_name = input("Enter file name which you want to store (Note: end the file name with .csv format): ")
        os.chdir(r"D:\Python old project file(CSV)")

        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ACC_NUM", "date", "Type", "Amount", "Balance"])

            for acc_num, transactions in cls.transaction_details.items():
                for transaction in transactions:
                    writer.writerow([
                        acc_num,
                        transaction["DATE"],
                        transaction["TYPE"],
                        transaction["AMOUNT"],
                        transaction["BALANCE"]
                    ])
        print(f"Transaction data has been written at {file_name}.csv file. Please open it for details.")



c1 = Bank("Hemanth", 22, "Male", "Nagole", 7995403535, 879687964296, 2445, 10000)
c2 = Bank("Aruna", 44, "Female", "Guntur", 9492346535, 879685664569, 8885, 50000)
c3 = Bank("Srinivasa Rao", 56, "Male", "Chilakaluripet", 6300636595, 879147967894, 6301, 60000)
# print(c1.deposite())
# print(c3.name)501

# print(c3.balance_)
# print(c1.name)
# print(c1.dispaly_balance())
c1.deposit()
# #
print(c1.display_balance())
#
print(c1.transaction_details)
#
c1.withdraw()
#
print(c1.transaction_details)

c1.mini_statement()
c1.convert_data_into_csv()

# c1.pin_change()
# c1.display_key_val()
# print(c1.customer_details)
# c1.change_user_details()
# c1 = Bank("narsi",27,"male","hyd",7894561230,789456123654,7412,70000)
# c1.add_new_customer()
# print(c1.customer_details)
# c1.display_key_val
# print(c1.customer_details)
# print(c1.balance_,": is before transfer money")
# print(c2.balance_,": is before receiving money")
# c1.transfer_method()
# print(c1.balance_,": is before transfer money")
# print(c2.balance_,": is before receiving money")
# print()
# print(c1.balance_,": is after transfer money")
# print(c2.balance_,": is after transfer money")
