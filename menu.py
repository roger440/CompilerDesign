
from Auto import Automata


class menu():
    def __init__(self):
        self.auto = Automata()

    def print_menu(self):
        print("1. Read From file")
        print("2. Display States")
        print("3. Display alphabet")
        print("4. Display transitions")
        print("5. Display final states")
        print("6. Check if pattern is accepted")
    def run(self):
        while True:
            self.print_menu()

            command = int(input())
            if command == 1:
                file = input()
                self.auto.read(file)
            elif command == 2:
                print(self.auto.states)
            elif command == 3:
                print(self.auto.alphabet)
            elif command == 4:
                for transition in self.auto.transitions:
                    print(transition.first,transition.second,transition.cost)
            elif command == 5:
                print(self.auto.finalStates)
            elif command == 6:
                pattern = input()
                print(self.auto.is_accepted(pattern))
            else:
                print("Not accepted command")

m = menu()
m.run()
