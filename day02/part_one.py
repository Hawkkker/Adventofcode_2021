import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def move(submarine, direction, value):
    if direction == 'forward':
        submarine['horizontal'] += value
        submarine['depth'] += value * submarine['aim']
    if direction == 'down':
        submarine['aim'] += value
    elif direction == 'up':
        submarine['aim'] -= value
    return submarine

total = 0
with open(dir_path + '/' + 'input.txt') as f:
    submarine = {'horizontal': 0, 'depth': 0, 'aim': 0}
    for line in f:
        info = line.split()
        direction = info[0]
        value = int(info[1])
        submarine = move(submarine, direction, value)
print(submarine)
print(submarine['horizontal']*submarine['depth'])