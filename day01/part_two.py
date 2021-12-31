import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def add(dict, line):
    dict['value'] += int(line)
    dict['numbers'] += 1
    return dict

def reset(dict, previous, total):
    if dict['numbers'] > 2:
        if dict['value'] > previous:
            total += 1
        previous = dict['value']
        dict['numbers'] = 0
        dict['value'] = 0
    return dict, previous, total

total = 0
with open(dir_path + '/' + 'input.txt') as f:
    previous = 0
    turn = 0
    A = {'value': 0, 'numbers':0}
    B = {'value': 0, 'numbers':0}
    C = {'value': 0, 'numbers':0}
    for line in f:
        A, previous, total = reset(A, previous, total)
        B, previous, total = reset(B, previous, total)
        C, previous, total = reset(C, previous, total)
        if turn == 0:
            A = add(A, line)
            turn += 1
        elif turn == 1:
            A = add(A, line)
            B = add(B, line)
            turn += 1
        else:
            A = add(A, line)
            B = add(B, line)
            C = add(C, line)
print(total)