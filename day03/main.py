import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def most(list, model, i):
    compare = ''
    zero = 0
    one = 0
    for nb in list:
        if nb[i] == '0':
            zero += 1
        elif nb[i] == '1':
            one += 1
    if zero > one:
        if model == 0:
            compare = '0'
        else:
            compare = '1'
    elif zero == one:
        if model == 0:
            compare = '1'
        else:
            compare = '0'
    else:
        if model == 0:
            compare = '1'
        else:
            compare = '0'
    return (compare)

def recur(list, model, bits, index):
    new = []
    compare = ''
    if index >= len(bits[0]):
        return (list[0])
    for report in list:
        compare = most(list, model, index)
        if report[index] == compare:
            new.append(report)
    if not new:
        return (list[0])
    return recur(new, model, bits, index + 1)

total = 0
with open(dir_path + '/' + 'input.txt') as f:
    bits = []
    for line in f:
        bit = []
        bits.append(str(line).rstrip("\n"))
    gamma = ''
    epsilon = ''
    for i in range(len(bits[0])):
        zero = 0
        one = 0
        for report in bits:
            if report[i] == '0':
                zero += 1
            elif report[i] == '1':
                one += 1
        if zero > one:
            gamma += '0'
            epsilon += '1'
        elif zero == one:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '1'
            epsilon += '0'
    gamma_list = []
    epsilon_list = []
    for idx, report in enumerate(bits):
        if report[0] == gamma[0]:
            gamma_list.append(bits[idx])
        else:
            epsilon_list.append(bits[idx])
    gamma = recur(gamma_list, 0, bits, 1)
    epsilon = recur(epsilon_list, 1, bits, 1)
    # print(int(gamma, 2), int(epsilon, 2))
    print(int(gamma, 2) * int(epsilon, 2))