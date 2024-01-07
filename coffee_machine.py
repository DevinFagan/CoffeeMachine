class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = ""

    def amount_check(self):
        if self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.beans < 12:
            print("Sorry, not enough coffee beans!")
        elif self.beans < 1:
            print("Sorry, not enough cups!")

    def buy_coffee(self):

        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if self.water >= 200 and self.milk >= 75 and self.beans >= 12 and self.cups >= 1:

            if coffee_type == "back":
                pass

            elif int(coffee_type) == 2:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7

            elif int(coffee_type) == 3:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6

            elif int(coffee_type) == 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4

        else:
            self.amount_check()

    def fill_coffee(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans you want to add:"))
        self.cups += int(input("Write how many disposable cups you want to add:"))

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def main(self):

        self.state = "not_exit"

        while self.state != "exit":

            self.state = input("Write action (buy, fill, take, remaining, exit):")

            if self.state == "exit":
                break
            elif self.state == "buy":
                self.buy_coffee()
            elif self.state == "fill":
                self.fill_coffee()
            elif self.state == "take":
                self.take_money()
            elif self.state == "remaining":
                print(f"The coffee machine has")
                print(f"{self.water} ml of water")
                print(f"{self.milk} ml of milk")
                print(f"{self.beans} g of coffee beans")
                print(f"{self.cups} disposable cups")
                print(f"${self.money} of money\n")


test = CoffeeMachine()
test.main()
