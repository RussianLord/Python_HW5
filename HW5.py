# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# with open ('Python_HW5/file.txt', 'r',encoding='utf-8') as F:
#     S = F.read()
#     listS = list(map(str, S.split()))
#     print(listS)
#     newList = []
#     for i in range(len(listS)):
#         if 'а' in listS[i] or 'б' in listS[i] or 'в' in listS[i]:
#             i += 1
#         else:
#             newList.append(listS[i])
#     print(newList)

# 2. Создайте программу для игры в ""Крестики-нолики"".

zone1 = ['-','-','-']
zone2 = ['-','-','-']
zone3 = ['-','-','-']
print(zone1,zone2,zone3,sep='\n')
R = 9
def kr(R):
    for i in range(R-9, R):
        X = int(input('Введите номер ячейки... '))
        if i % 2 == 0 :
            S = 'X'
        else:
            S = 'O'
        if 0 < X < 4:
            if X == 1 and zone1[0] == '-':       
                zone1[0] = S
            elif X == 2 and zone1[1] == '-':
                zone1[1] = S
            elif X == 3 and zone1[2] == '-':
                zone1[2] = S
            else:
                print('Занято, ввидете другое число...')
                return kr(R+1)
        elif 3 < X <7:
            if X == 4 and zone2[0] == '-':       
                zone2[0] = S
            elif X == 5 and zone2[1] == '-':
                zone2[1] = S
            elif X == 6 and zone2[2] == '-':
                zone2[2] = S
            else:
                print('Занято, ввидете другое число...')
                return kr(R)
        elif 6 < X < 10:
            if X == 7 and zone3[0] == '-':       
                zone3[0] = S
            elif X == 8 and zone3[1] == '-':
                zone3[1] = S
            elif X == 9 and zone3[2] == '-':
                zone3[2] = S
            else:
                print('Занято, ввидете другое число...')
                return kr(R)
    
        print(zone1,zone2,zone3, sep='\n')
kr(R)
# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Mode = int(input('Нажми 1, чтобы выбрать сжатие, нажми 2, чтобвы выбрать восстановление... '))
# with open('Python_HW5/sjat.txt', 'r', encoding='utf-8') as R:
#     M = R.read()
# def Sjat(N):  
#         K = 0
#         strN = ""
#         for i in range(K, len(M)):
#             if M[K] != M[i]:
#                 strN += ((f'{i-K} {M[i-1]},'))
#                 K = i
#         strN += ((f'{i-K+1} {M[i-1]}'))
#         print(strN)
#         with open('Python_HW5/recovery.txt', 'w', encoding='utf-8') as W:
#             P = W.write(strN) 
           


# with open('Python_HW5/recovery.txt', 'r', encoding='utf-8') as R:
#     N = R.read().split(',')
# def Recov(N):
#     with open('Python_HW5/sjat.txt', 'w', encoding='utf-8') as W:
#         P = W.write('')
#     strN = ""
#     for i in range(len(N)): 
#         T = N[i].split()
#         number = int(T[0])
#         for j in range(number):
#             strN = T[1]
#             with open('Python_HW5/sjat.txt', 'a', encoding='utf-8') as W:
#                 P = W.write(strN)
#             print(strN, end='')
    
# if Mode == 1:
#     Sjat(M)
# else:
#     Recov(N)
