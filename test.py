input_data = open("input.txt", "r")
lines = [x.strip() for x in input_data.readlines()]
m = 0
pairs = {}
for line in lines:
    itemList = line.split(':')
    if len(itemList) == 0:
        break
    elif len(itemList) == 1:
        m = int(itemList[0])
    else:
        pairs[int(itemList[0])] = itemList[1]

found = False
for key,item in sorted(pairs.items()):
    if m % key == 0:
        found = True
        print(item)

if not found:
    print(m)
