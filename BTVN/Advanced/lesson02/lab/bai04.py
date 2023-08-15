class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def welcome(self):
        return f'Welcome, {self.username}'
    
    def check_password(self, check_pass):
        if check_pass == self.password:
            return True
        else:
            return False

from datetime import datetime

class SubscribedUser(User):
    def __init__(self, username, password, date):
        self.username = username
        self.password = password
        self.date = date

    def is_expired(self):
        now = datetime.now()
        
        if self.date < now:
            return True
        elif self.date == now:
            return True
        else:
            return False


user = User('mindx', '12345')
print(user.welcome())
print(user.check_password('1234'))

print('-------------------------------------------------------')
s_user = SubscribedUser('s_mindx', '1234', datetime(2024, 1, 1))
print(s_user.welcome())
print(s_user.check_password('1234'))
print(s_user.is_expired())