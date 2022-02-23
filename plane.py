def place_pass(pos, side, num, row):
    row = list(row)
    place_letter = {0: 'A', 1: 'B', 2: 'C', 4: 'D', 5: 'E', 6: 'F'}
    places = []
    if side == 'left' and pos == 'aisle':
        for i in range(2, 3 - num - 1, -1):
            row[i] = 'X'
            places.append(i)
    elif side == 'left' and pos == 'window':
        for i in range(num):
            row[i] = 'X'
            places.append(i)
    if side == 'right' and pos == 'aisle':
        for i in range(4, 4 + num):
            row[i] = 'X'
            places.append(i)
    elif side == 'right' and pos == 'window':
        for i in range(6, 6 - num, -1):
            row[i] = 'X'
            places.append(i)
    places.sort()
    for i in range(len(places)):
        places[i] = place_letter[places[i]]
    return ''.join(row), places


def cleaner(table):
    for i in range(len(table)):
        table[i] = table[i].replace('X', '#')
    return table


n = int(input())

plane_map = []

for i in range(n):
    plane_map.append(input())

m = int(input())
place_let = []

for i in range(m):
    num, side, pos = input().split()
    num = int(num)
    side_let = side
    num_flag = False
    pos_flag = False
    place_let = []
    for j in range(n):
        side = side_let
        if side == 'left':
            side = plane_map[j][:-4]
        else:
            side = plane_map[j][-3:]
        num_flag = False
        pos_flag = False
        if '.' * num in side:
            num_flag = True
            if pos == 'aisle' and side_let == 'left' and side[2] == '.':
                pos_flag = True
                plane_map[j], place_let = place_pass('aisle', 'left', num, plane_map[j])
                break
            elif pos == 'aisle' and side_let == 'right' and side[0] == '.':
                pos_flag = True
                plane_map[j], place_let = place_pass('aisle', 'right', num, plane_map[j])
                break
            elif pos == 'window' and side_let == 'left' and side[0] == '.':
                pos_flag = True
                plane_map[j], place_let = place_pass('window', 'left', num, plane_map[j])
                break
            elif pos == 'window' and side_let == 'right' and side[2] == '.':
                pos_flag = True
                plane_map[j], place_let = place_pass('window', 'right', num, plane_map[j])
                break

    if num_flag and pos_flag:
        for i in range(len(place_let)):
            place_let[i] = str(j + 1) + place_let[i]
        new_place = ' '.join(place_let)
        print("Passengers can take seats: " + new_place)
        for k in range(n):
            print(plane_map[k])
        plane_map = cleaner(plane_map)
    else:
        print('Cannot fulfill passengers requirements')
