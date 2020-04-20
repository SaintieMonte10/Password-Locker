#!/usr/bin/env python3.6
from password import User, Credential
import random
import string
import getpass


def create_user(name, user_password):
    """
    Parameters
    ----------
    name
    user_password
    Returns
    -------
    """
    new_user = User(name, user_password)
    return new_user


def generate_password(user):
    """
    function to generate random password for user
    ----------
    user
    Returns
    -------
    """
    return user.generate_random_password()


def save_user(user):
    """
    Function to save user
    ----------
    user
    """
    user.save_user()


def delete_user(user):
    """
    Function to delete user
    ----------
    user
    """
    user.delete_user()


def create_credential(account, account_username, account_password):
    """
    Parameters
    ----------
    name
    credential_password
    Returns
    -------
    """
    new_credential = Credential(account, account_username, account_password)
    return new_credential


def save_credential(credential):
    """
    Function to save user
    ----------
    user
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete credential
    ----------
    credential
    """
    credential.delete_credential()


def find_credential(account_username):
    """
    Function to find credential
    ----------
    name
    Returns
    -------
    """
    return Credential.find_by_account_username(account_username)


def check_existing_credentials(account_username):
    """
    Function to check existing credential
    ----------
    name
    Returns
    -------
    user
    """
    return Credential.find_by_account_username(account_username)


def display_credentials():
    """
    Function to display credential
    Returns
    -------
    """
    return Credential.display_all_credentials()


def main():
    """
    Returns
    -------
    """
  
    user_name = input("Enter your full name: ")

    print(f"Heeeeey {user_name}, Welcome abroad")
    print("\n")
    print("*"*20)
    ask = input(f"Hello {user_name}. Do you have an Account? YES/N0 > ").lower()
    print("-"*50)
    if ask == "no":
        print("Signup with password locker to have access")
        user_name = input("Enter your User name: ")
        print("-"*20)
        create = input(
            f"Hello {user_name}. Do you want a generated password? YES/N0 > ")
        if create == "NO":
            print("-"*69)
            print("|Don't mind if your password is not visible as you type. WE go your password secured.|")#
            print("-"*70)
            getpass.getpass()
            print(f"You have succesfully joined {social_media} HAVE FUN!!")
        elif create == "YES":
            def random_password(string_length):
                """
                Parameters
                 ----------
                 string_length
                 Returns
                 -------
                 """
                letters = string.ascii_letters
                return "".join(random.choice(letters) for i in range(string_length))
            print("Your password is ")

            print(
                f"Your random password is: ", random_password(8))
            print("You have logged in successfully : ")
        while True:
            print("Kindly use these short codes \n nc: To create a new credential \n dc: To display credential details \n lc: To locate credential \n dl: to delete credential \n gp: To generate a random password \n ex: To exit")
            short_code = input("Use short-codes to continue\\")

            if short_code == "nc":
                print(" Create an account")
                print("-" * 10)

                print("Account type ....")
                account = input("=>")

                print("username ....")
                account_username = input("=>")

                print("Enter Password")
                account_password = input("=>")

                save_credential(create_credential(account, account_username, account_password))

                print("\n")
                print(f"New Credential for {account} {account_username} {account_password} has been created")
                print("\n")
                print("*" * 10)

            elif short_code == "gp":
                print(
                    "Please enter the type of account that you wanna generate a password for =>")
                social_media = input("Enter account type eg.(facebook) ")

                def random_password(string_length):
                    """
                    Parameters
                    ----------
                    string_length
                    Returns
                    -------
                    """
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))
                print(f"Your random password for {social_media} is: " "".join(random.choice(letters) for i in range(string_length)))

            elif short_code == "dc":

                if display_credentials():
                    print("Here is a list of all your Accounts and Passwords")
                    print("\n")
                    for credential in display_credentials():
                        print(f"{credential.account} {credential.account_username}{account_password}")
                        print("\n")
                else:
                    print("\n")
                    print(
                        "Sorry you don't have any details yet. Try generating using short codes")
                    print("\n")

            elif short_code == 'lc':

                print("Enter the account username you want to search for")

                search_account_username = input()
                if check_existing_credentials(search_account_username):
                    search_credential = find_credential(search_account_username)
                    print(f"{search_credential.account} {search_credential.account_username}")
                    print('-' * 20)

                    print(f"Account password.......{search_credential.account_password}")

                else:
                    print("That credential does not exist")

            elif short_code == "dl":
                print("Enter the account username of the credential you would like to delete.")
                my_delete = input("=>")
                my_del = find_credential(my_delete)
                Credential.credential_list.remove(my_del)
                print(
                    f"Credential with  account username {my_delete} has been removed succefully")
            elif short_code == "ex":
                print("Logged out")
                break

    elif ask == "yes":
        print("Welcome back to our password locker. Enter your username and password to login")
        user_name = input("Enter username: ")
        print("-"*87)
        print("|Don't mind if your password is not vissible as you type. Your password is secure.|")#
        print("-"*87)
        account_password= getpass.getpass()
        while True:
            print("Kindly use these short codes \n nc: To create a new credential \n dc: To display credential \n lc: To find credential \n dl: to delete credential \n gp: To generate a random password \n ex: To exit")
            short_code = input("Use short-codes to continue => ")

            if short_code == "nc":
                print(" Create account")
                print("-" * 10)

                print("Account ....")
                account = input("=> ")

                print("username ....")
                account_username = input("=> ")

                print("Enter Password")
                account_password = input("=> ")

                save_credential(create_credential(account, account_username, account_password))

                print("\n")
                print(f"New Credential {account} {account_username} {account_password} has been created")
                print("\n")

            elif short_code == "gp":
                print(
                    "Please enter the account you want to generate password for > ")
                social_media = input("Enter account type => ")

                def random_password(string_length):
                    """
                    Parameters
                    ----------
                    string_length
                    Returns
                    -------
                    """
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))

                print(
                    f"Your random password for {social_media} is: ", random_password(8))

            elif short_code == "dc":

                if display_credentials():
                    print("Here is a list of all your Credentials and passwords")
                    print("\n")
                    for credential in display_credentials():
                        print(f"{credential.account} {credential.account_username}:  {account_password}")
                        print("\n")
                else:
                    print("\n")
                    print(
                        "You don't have any saved credentials yet. Try saving one")
                    print("\n")

            elif short_code == 'lc':

                print("Enter the account username you want to search for")

                search_account_username = input()
                if check_existing_credentials(search_account_username):
                    search_credential = find_credential(search_account_username)
                    print(f"{search_credential.account} {search_credential.account_username}")
                    print('-' * 20)

                    print(f"Account password.......{search_credential.account_password}")

                else:
                    print("That credential does not exist")

            elif short_code == "dl":
                print("Enter the account username of the credential you would like to delete.")
                my_delete = input("=> ")
                my_del = find_credential(my_delete)
                Credential.credential_list.remove(my_del)
                print(
                    f"Credential with  account username {my_delete} has been removed succefully")
            elif short_code == "ex":
                print("You have logged out succesfully......See you soon!")
                break

    else:
        print("Please check your entry")


if __name__ == "__main__":
    main()
