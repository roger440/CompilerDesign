import re


# a list of all reserved keywords

def get_reserved():
    reserved = []
    with open('specifications/tokens.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip(' ')
            reserved.append(line.strip('\n'))
    return reserved


def is_string(x):
    pattern = '^"[a-zA-Z0-9 ]+"$'
    if re.search(pattern, x):
        return True
    return False


def is_number(x):
    pattern = '^[-]?[1-9][0-9]*$'
    if re.search(pattern, x):
        return True
    return False


def is_identifier(x):
    pattern = '^[a-zA-Z][a-zA-Z_0-9]*$'
    if re.search(pattern, x):
        return True
    return False

def is_zero(x):
    return x == 0 or x == '0'

def is_constant(x):
    if is_number(x) or is_string(x) or is_zero(x):
        return True
    return False

def is_full_of_spaces(x):
    for char in x:
        if char != ' ':
            return False
    return True
