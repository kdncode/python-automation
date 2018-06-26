class Person:
    __name = '' #Private
    __email = '' #Private

    # Constructor to pass value into def
    def __init__(self, name, email):
        self.__name = name
        self.__email = email


    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)

# john = Person('JOHN', '123')

# # john.set_name('John Wick')
# # john.set_email('John@gmail.com')
# print(john.get_name())
# print(john.get_email())
# print(john.toString())

# Inherit
class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name =name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def toString(self):
        return '{} can be contacted at {} with the salary {}'.format(self.__name, self.__email, self.__balance)

wick = Customer('Wick', '@gmail', 200)

wick.set_balance(400)

print(wick.toString())