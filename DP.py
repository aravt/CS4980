x = input('Please type in the first DNA String:')
y = input('Please type in the second DNA String:')

x = str(x)
y = str(y)

xLen = len(x)
yLen = len(y)

l = [[[0 for _ in range(2)] for _ in range(yLen + 1)] for _ in range(xLen + 1)]

for i in range(xLen + 1):
    for j in range(yLen + 1):
        if i == 0:
            l[i][j][0] = -1 * j
        elif j == 0:
            l[i][j][0] = -1 * i
        else:
            north = l[i - 1][j][0] - 1
            west = l[i][j - 1][0] - 1
            if x[i - 1] == y[j - 1]:
                northWest = l[i - 1][j - 1][0] + 0
            else:
                northWest = l[i - 1][j - 1][0] - 1
            maxNum = max(north, west, northWest)
            if maxNum == north:
                l[i][j][0] = north
                l[i][j][1] = 'n'
            elif maxNum == west:
                l[i][j][0] = west
                l[i][j][1] = 'w'
            else:
                l[i][j][0] = northWest
                l[i][j][1] = 'nw'


word1 = ''
word2 = ''

i = xLen
j = yLen
while i != 0 and j != 0:
    if l[i][j][1] == 'w':
        word1 = '_' + word1
        word2 = y[j - 1] + word2
        j = j - 1
    elif l[i][j][1] == 'n':
        word2 = '_' + word2
        word1 = x[i - 1] + word1
        i = i - 1
    else:
        word1 = x[i - 1] + word1
        word2 = y[j - 1] + word2
        i = i - 1
        j = j - 1

print(l[xLen][yLen][0])
print(word1)
print(word2)
