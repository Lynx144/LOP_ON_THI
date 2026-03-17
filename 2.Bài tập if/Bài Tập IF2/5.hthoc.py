k=int(input())
tg= 7
min =k*45
if k>1:
    min+=10
if k>2:
    min+=5
if k>3:
    min+=10
if k>4:
    min+=5
print(f'{int(tg+min//60)} {int(min%60)}')
