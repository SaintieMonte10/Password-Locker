class User:
    """
    Class that generates new instances of Users
    """
    user_list = []

    def __init__(self, name, user_password):
        self.name = name
        self.user_password = user_password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes saved contact
        """
        User.user_list.remove(self)


class Credential:
    """
    Class that generates new instances of credentials
    """
    credential_list = []

    def __init__(self, account, account_username, account_password):
        self.account = account
        self.account_username = account_username
        self.account_password = account_password

    def save_credential(self):
        """
        save_credential method saves user objects into credential_list
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        delete_credential method deletes saved contact
        """
        Credential.credential_list.remove(self)

    def test_save_credential(self):
        pass
    
    @classmethod
    def find_by_account_username(cls, account_username):
        for credential in cls.credential_list:
            if credential.account_username == account_username:
                return credential
    @classmethod
    def credential_exists(cls, account_username):
        for credential in cls.credential_list:
            if credential.account_username == account_username:
                return True
            return False
    @classmethod
    def display_credentials(cls):
        return cls.credential_list

    @classmethod
    def display_all_credentials(cls):
        return cls.credential_list