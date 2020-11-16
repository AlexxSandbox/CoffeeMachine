class Coffee_machine:      
      COFFEE_REСIPE = {'espresso':(250, 0, 16, 1, 4), 'latte':(350, 75, 20, 1, 7), 'cappuccino':(200, 100, 12, 1, 6)}
      def __init__(self):
            self.coffee_menu = []
            for coffee in Coffee_machine.COFFEE_REСIPE:
                  self.coffee_menu.append(coffee)
            self.water = 400
            self.milk = 540
            self.coffee_beans = 120
            self.cups = 9
            self.money = 550

      def remaining(self):
            print(f'\nThe coffee machine has:'
                  f'\n{self.water} of water'
                  f'\n{self.milk} of milk'
                  f'\n{self.coffee_beans} of coffee beans'
                  f'\n{self.cups} of disposal cups'
                  )
            if self.money > 0:
                  print(f'${self.money} of money')
            else:
                  print(f'{self.money} of money')
          
      def buy(self):
            coffee_choice = None
            while coffee_choice not in ('1', '2', '3', 'back'):
                  coffee_choice = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ')
                  if coffee_choice == 'back':
                        pass
                  else:
                        coffee = self.coffee_menu[int(coffee_choice) - 1]
                        self.check_status(coffee)

      def check_status(self, coffee):
            water = self.water - Coffee_machine.COFFEE_REСIPE[coffee][0]
            milk = self.milk - Coffee_machine.COFFEE_REСIPE[coffee][1]
            coffee_beans = self.coffee_beans - Coffee_machine.COFFEE_REСIPE[coffee][2]
            cups = self.cups - Coffee_machine.COFFEE_REСIPE[coffee][3]
            if water < 0:
                  print('\nSorry, not enough water!')
            elif milk < 0:
                  print('\nSorry, not enough milk!')
            elif coffee_beans < 0:
                  print('\nSorry, not enough coffee beans!')
            elif cups < 0:
                  print('\nSorry, not enough coffee beans!')
            else:
                  print('\nI have enough resources, making you a coffee!')
                  self.make_coffee(coffee)

      def make_coffee(self, coffee):            
            self.water -= Coffee_machine.COFFEE_REСIPE[coffee][0]
            self.milk -= Coffee_machine.COFFEE_REСIPE[coffee][1]
            self.coffee_beans -= Coffee_machine.COFFEE_REСIPE[coffee][2]
            self.cups -= Coffee_machine.COFFEE_REСIPE[coffee][3]
            self.money += Coffee_machine.COFFEE_REСIPE[coffee][4]

      def fill(self):      
            add_water = int(input('\nWrite how many ml of water do you want to add:\n> '))
            self.water += add_water
            add_milk = int(input('Write how many ml of milk do you want to add:\n> '))
            self.milk += add_milk
            add_coffee_beans = int(input('Write how many grams of coffee beans do you want to add:\n> '))
            self.coffee_beans += add_coffee_beans
            add_cups = int(input('Write how many disposable cups of coffee do you want to add:\n> '))
            self.cups += add_cups

      def take(self):
            print(f'\nI gave you ${self.money}')
            self.money = 0


def main():
      delonghy = Coffee_machine()
      choice = None
      while choice != 'exit':
            choice = input('Write action (buy, fill, take, remaining, exit):\n> ')
            if choice == 'buy':
                  delonghy.buy()
            elif choice == 'fill':
                  delonghy.fill()
            elif choice == 'take':
                  delonghy.take()
            elif choice == 'remaining':
                  delonghy.remaining()


if __main__ == '__main__':
    main()
