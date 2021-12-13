from ST import Table
from helpers import *
from Auto import *
import re
class Scanner:
    def __init__(self, input_file, st_table, pif_table):
        self.input_file=input_file
        self.st_table_file=st_table
        self.pif_table=pif_table
        self.reserved = get_reserved()
        self.ST = Table()
        self.PIF = []
        self.constant_auto = Automata()
        self.identifier_auto = Automata()
        self.constant_auto.read("ConstantAuto")
        self.identifier_auto.read("IdentifierAuto")
    def write_to_files(self):

        with open(self.st_table_file,'w') as f:
            f.write(self.ST.to_string())

        with open(self.pif_table,'w') as f:
            for element in self.PIF:
                f.write("token: ")
                f.write(element[0])
                f.write(" ")
                f.write("pos: ")
                f.write(str(element[1]))
                f.write('\n')

    def scan(self):
        with open(self.input_file,'r') as f:
            program=""
            for line in f:
                program+=line
            reserved = get_reserved()
            for key in reserved:
                program = program.replace(key, " "+key + " ")
            program = program.replace('\n', " ? ")
            program = re.split(" ", program)
            trimmed = []
            for token in program:
                if token != '':
                    trimmed.append(token.strip())
            line_count = 1
            for token in trimmed:
                if not is_full_of_spaces(token):
                    if token != '?':
                        if token in reserved:
                            self.PIF.append([token, -1])

                        elif self.identifier_auto.is_accepted(token):
                            pos=self.ST.add(token)
                            self.PIF.append([token,pos])

                        elif self.constant_auto.is_accepted(token):
                            pos=self.ST.add(token)
                            self.PIF.append(["constant", pos])

                        else:
                            print("Error : cannot resolve token:" + token + " " + "at line " + str(line_count))
                            return
                    else:
                        line_count+=1
            print("Lexically correct")
            self.write_to_files()

