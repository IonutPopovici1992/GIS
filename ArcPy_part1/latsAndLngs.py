llF = open('latsAndLngs.csv', 'r')

for line in llF:
    words = line.split(',')
    print(words[0])
    print(words[1])
    print(words[2])

llF.close()
