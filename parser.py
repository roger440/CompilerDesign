from main import Grammar


class Parser:
    def __init__(self) -> None:
        self.G = Grammar()
        self.firstSet = {i: [] for i in self.G.nonterminals}
        self.followSet = {i: [] for i in self.G.nonterminals}

    def computeFirst(self):
        changed = True
        while changed:
            changed = False

            for production in self.G.productions:
                for rhs in production.RHS:
                    if rhs[0] in self.G.alphabet and rhs[0] not in self.firstSet[production.LHS]:
                        self.firstSet[production.LHS].append(rhs[0])
                        changed = True

    def follow(self):
        pass

    def parse(self):
        pass


p = Parser()

p.computeFirst()

print(p.firstSet)