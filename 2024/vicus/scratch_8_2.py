directions =[(1,1),(1,-1), (-1,1),(-1,-1), (0,0)]
score = 0
for (x,y), key in dic.items():
    if key =='A':
        test = ''.join([dic.get((x+dx,y+dy), 'L') for dx,dy in directions])
        if test.count('A')==1 and test.count('M')==2 and test.count('S')==2:
            if dic[(x+1,y+1)] != dic[(x-1,y-1)]:
                score += 1

print(f'answer to part 2 is {score}')