import hashlib
from tkinter import Tk, Entry, Label, Button
import re
import string
import sqlite3
from random import randint
from Database_Querying import Database

class safety_login:
    def __init__(self):

        self.__accepted = False
        self.__pepper_pass = "Pm76#%Ffvbnmcxy@.ftfgd"
        self.__pepper_user = "GdFter@9767DFsdwa.,$2sd"
        self.__salt_string = string.printable

        self.__Upattern = r"^[\w\d\_)+@[\w\d]+\.[\w\d]+$"
        self.__Ppattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,}$"


    def begin(self):


        self.__root = Tk()

        self.__label = Label(self.__root, text="Enter your username and password")

        self.__enter_username = Entry(self.__root, width=40, borderwidth=3)

        self.__enter_password = Entry(self.__root, show="*", width=40, borderwidth=3)

        self.__submit = Button(self.__root, text="Login", command=self.__regex)

        self.__create = Button(self.__root, text="Create Account", command=self.__create_account)

        self.__label.pack()
        self.__enter_username.pack()
        self.__enter_password.pack()
        self.__submit.pack()
        self.__create.pack()

        self.__root.mainloop()


    def __regex(self):
        self.__username = self.__enter_username.get()

        self.__password = self.__enter_password.get()
        if re.match(self.__Upattern, self.__username):
            self.__username += self.__pepper_user
            self.__username = hashlib.sha3_512(bytes(self.__username, 'utf-8')).hexdigest()

            self.__password_hash = Database.password(self.__username)
        else:
            return False
        if(re.search(self.__Ppattern, self.__password)):
            self.__hash_details()
        else:
            return False


    def __hash_details(self):
        self.__pepper()
        i = 0
        while self.__accepted == False:
            self.__salt(i)
            self.__riffle()

            checker = hashlib.sha3_512(bytes(self.__riffled_pass, 'utf-8')).hexdigest()


            if checker == self.__password_hash:
                print("Password Matched")
                self.__accepted = True

            i = i + 1


        self.__accepted = False

        self.Player_id = Database.get_player_id(self.__username, checker)

        self.__root.destroy()






    def __pepper(self):

        self.__pepper_password = self.__password
        self.__pepper_password += self.__pepper_pass

        self.__pepper_username = self.__username
        self.__pepper_username += self.__pepper_user

        self.__part_1_pass_hash_pepper = hashlib.sha3_512(bytes(self.__pepper_password, 'utf-8')).hexdigest()
        self.__user_hash_pepper = hashlib.sha3_512(bytes(self.__pepper_username, 'utf-8')).hexdigest()



    def __salt(self, i):
        self.__salt_test = self.__salt_string[i]
        print(self.__salt_test)
        self.__salt_password = self.__password

        self.__salt_password += self.__salt_test
        self.__part_2_pass_hash_salt = hashlib.sha3_512(bytes(self.__salt_password, 'utf-8')).hexdigest()




    def __riffle(self):
        self.__riffled_pass = ""
        for i in range(len(self.__part_1_pass_hash_pepper)):
            self.__riffled_pass += self.__part_1_pass_hash_pepper[i]
            self.__riffled_pass += self.__part_2_pass_hash_salt[i]




    def __create_account(self):


        self.__root.destroy()

        self.__root = Tk()

        self.__enter_username = Entry(self.__root, width=40, borderwidth=3)

        self.__enter_password = Entry(self.__root, show="*", width=40, borderwidth=3)
        self.__enter_password_confirmation = Entry(self.__root, show="*", width=40, borderwidth=3)

        self.__confirm = Button(self.__root, text="Create Account", command=self.__check_validity)

        self.__enter_username.pack()
        self.__enter_password.pack()
        self.__enter_password_confirmation.pack()
        self.__confirm.pack()


        self.__root.mainloop()

    def __check_validity(self):

        list_of_emails = Database.all_emails()

        self.__username = self.__enter_username.get()
        self.__password = self.__enter_password.get()

        self.__pepper()


        if self.__user_hash_pepper in list_of_emails:
            print("Email already exists")
            self.__root.destroy()
            self.begin()

        if self.__enter_password.get() != self.__enter_password_confirmation.get():
            print("Passwords don't match")
            return False
        if re.match(self.__Upattern, self.__enter_username.get()):
            pass
        else:
            print("email not valid")
            return False
        if re.match(self.__Ppattern, self.__enter_password.get()):

            self.__password = self.__enter_password.get()
            self.__username = self.__enter_username.get()

            self.__salt_password = self.__password

            salt = randint(0, len(self.__salt_string) - 1)
            self.__salt_true = self.__salt_string[salt]
            self.__salt_password += self.__salt_true

            self.__part_2_pass_hash_salt = hashlib.sha3_512(bytes(self.__salt_password, 'utf-8')).hexdigest()
            self.__riffle()
            self.__password_new = hashlib.sha3_512(bytes(self.__riffled_pass, 'utf-8')).hexdigest()
            self.__username_new = self.__user_hash_pepper
            self.__update()
        else:
            return False


    def __update(self):

        self.__root.destroy()

        email_input = self.__username_new
        password_input = self.__password_new

        Database.New_user(email_input, password_input)

        self.begin()










if __name__ == '__main__':
    login()
