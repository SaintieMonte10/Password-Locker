# import pyperclip


# class credentials:
#     credentials_list = []
#     def save_credentials(self):


#         credentials.credentials_list.append(self)

#     def __init__(self,account_name,pass_word,phone_number,email):

         
          
#         self.account_name = account_name
#         self.pass_word = pass_word
#         self.phone_number = phone_number
#         self.email = email

#     def delete_credentials(self):

#         '''
#         delete_user method deletes a saved credentials from the credentials_list
#         '''

#         credentials.credentials_list.remove(self)

#     @classmethod
#     def find_by_number(cls,number):
        
#         for credentials in cls.credentials_list:
#             if credentials.phone_number == number:
#                 return credentials

#     @classmethod
#     def credentials_exist(cls,number):
       
#         for credentials in cls.credentials_list:
#             if credentials.phone_number == number:
#                     return True

#         return False

#     @classmethod
#     def display_credentials(cls):
#         '''
#         method that returns the credentials list
#         '''
#         return cls.user_list

#     @classmethod
#     def copy_email(cls,number):
#         credentials_found = credentials.find_by_number(number)
#         pyperclip.copy(credentials_found.email)