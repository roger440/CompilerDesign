import numpy as np
class Node:
    def __init__(self, key=None, position=None):
        self.key = key
        self.position = position
        self.next = None

class Table:
    def __init__(self):
        self.chain_count=10
        self.next_available_position=0
        self.chains = []
        for i in range(0,self.chain_count,1):
            self.chains.append(Node())

    def get_hash_value(self, identifier):
        s = 0
        for character in identifier:
            s+= ord(character)
        return s % self.chain_count

    def get(self, token):
        slot = self.get_hash_value(token)
        parser = self.chains[slot]
        while parser:
            if parser.key == token:
                return parser.position
            parser = parser.next

        return "not in symbol table"

        #if not found, create one
        added=Node(token, self.next_available_position)
        self.next_available_position+=1

        parser = self.chains[slot]
        while parser.next:
            if parser.key == token:
                return parser.position
            parser = parser.next

        parser.next = added
        return added.position

    def add(self,token):
        slot = self.get_hash_value(token)
        parser = self.chains[slot]

        while parser:
            if parser.key == token:
                return "already in symbol table"
            parser = parser.next

        added=Node(token, self.next_available_position)
        self.next_available_position+=1

        parser = self.chains[slot]
        while parser.next:
            if parser.key == token:
                return parser.position
            parser = parser.next
        parser.next = added

t = Table()
t.add("aa")
t.add("bb")
print(t.get("bb"))





