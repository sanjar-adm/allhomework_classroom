class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def get_values(self):
        print(self.number, self.model, self.weight)
        text = 'awdaacsevse cvwscaw'

    def sendMessage(self, *number):
        print(f'отправленные сообщения на номера {number}')

samsung = Phone(number=7676, model='Samsung', weight=0.7)
iphone = Phone(number=7777, model='iphone', weight=0.8)
honor = Phone(number=7879, model='honor', weight=0.90)
# samsung.get_values()
# iphone.get_values()
# honor.get_values()
print(samsung.__dict__)
print(iphone.__dict__)
print(honor.__dict__)
samsung.sendMessage(776887008,999456745)

