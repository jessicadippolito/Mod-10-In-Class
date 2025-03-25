class Pakuri:
    def __init__(self,name):
        self.name = name

    def attack(self,attack_name):
        self.attack_name = attack_name
        print(f'{self.name} used {self.attack_name}!')

    def speak(self):
        print(f'{self.name}, {self.name}!')

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        if amount < 0:
            print('Invalid amount.')
        else:
            print(f'Deposited ${amount}')
            self.balance += amount

    def withdraw(self,amount):
        if amount < 0:
            print('Invalid amount.')
        elif amount > self.balance:
            print("You don't have enough money :(")
        else:
            print(f'Withdrew ${amount}')
            self.balance -= amount

    def display(self):
        print(f"Current balance: ${self.balance}")

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        if isinstance(other,Coordinate):
            if self.x == other.x:
                if self.y == other.y:
                    return True
            else:
                return False

    def __add__(self,other):
        if isinstance(other, Coordinate):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Coordinate(new_x,new_y)

    def __str__(self):
        return f'({self.x}, {self.y})'



