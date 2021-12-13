class Transition:
    def __init__(self, first, second, cost):
        self.first=first
        self.second=second
        self.cost=cost

class Automata:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.finalStates = []
        self.initialState = 'p'

    def read(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

            #states
            states = lines[0].split(',')
            for i in range(0,len(states)-1,1):
                self.states.append(states[i])

            #alphabet
            alphabet = lines[1].split(',')
            for i in range(0,len(alphabet)-1,1):
                self.alphabet.append(alphabet[i])

            self.initialState = lines[2][0]

            #transitions
            transitions = lines[3].split(";")
            for transition in transitions:
                first = transition[0]
                cost = ""
                index = 2
                while transition[index] != ' ':
                    cost+=transition[index]
                    index+=1

                if cost == "0..9":
                    cost = "0123456789"

                elif cost == "a..z":
                    cost = "qwertyuiopasdfghjklzxcvbnm"

                elif cost == "A..Z":
                    cost = "QWERTYUIOPASDFGHJKLZXCVBNM"

                elif cost == "1..9":
                    cost = "123456789"

                second = ""

                index += 4
                second = transition[index]
                t = Transition(first, second, cost)
                self.transitions.append(t)

            #final states
            states = lines[4].split(',')
            for state in states:
                self.finalStates.append(state)

    def is_accepted(self, sequence):
        current_state = self.initialState
        for letter in sequence:
            ok = False
            for transition in self.transitions:
                if letter in transition.cost and transition.first == current_state:
                    ok = True
                    current_state = transition.second
            if not ok:
                return False
        return current_state in self.finalStates