class MobilePhone():
    def __init__(self, ten, he_dieu_hanh, dung_luong_pin, trang_thai):
        self.ten = ten
        self.he_dieu_hanh = he_dieu_hanh
        self.dung_luong_pin = dung_luong_pin
        self.trang_thai = trang_thai

    def turnOff(self):
        self.trang_thai = 'off'
        return self.trang_thai
    
    def turnOn(self):
        self.trang_thai = 'on'
        return self.trang_thai
    
    def checkBat(self):
        return self.dung_luong_pin
    
phone01 = MobilePhone('Iphone 15', 'IOS', '100%', 'off')
phone02 = MobilePhone('Zflip', 'Android', '70%', 'on')

print(phone02.turnOff())
print(phone01.turnOn())
print(phone01.checkBat())
print(phone02.checkBat())