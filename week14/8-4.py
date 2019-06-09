f = open('water.txt', 'r', encoding='utf-8')

s = f.readlines()

f.close()

f = open('result.txt', 'w', encoding='utf-8')

for line in s:
    line = line.split()
    if line:
        f.write('{} {}\n'.format(line[0], (int(line[-1])-int(line[1]))*1.05))
