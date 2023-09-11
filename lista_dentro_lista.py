linha_1 = [1,2,3]
linha_2 = [4,5,6]
linha_3 = [7,8,9]
tabuleiro = [linha_1,linha_2,linha_3]

#print(tabuleiro)

for x,y,z, in tabuleiro:
    print('-','-','-',sep='+')
    print(x,y,z,sep='|')

check = int(input("digita 0"))

if check in tabuleiro[0]:
    print('ver')
else:
    print('fls')
    