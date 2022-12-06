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




# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



Mode = int(input('Нажми 1, чтобы выбрать сжатие, нажми 2, чтобвы выбрать восстановление... '))
with open('Python_HW5/sjat.txt', 'r', encoding='utf-8') as R:
    M = R.read()
def Sjat(N):  
        K = 0
        strN = ""
        for i in range(K, len(N)):
            if N[K] != N[i]:
                strN += ((f'{i-K} {N[i-1]},'))
                K = i
        strN += ((f'{i-K+1} {N[i-1]}'))
        print(strN)
        with open('Python_HW5/RECOV.txt', 'w', encoding='utf-8') as W:
            P = W.write(strN) 
           


with open('Python_HW5/RECOV.txt', 'r', encoding='utf-8') as R:
    N = R.read().split(',')
def Recov(N):
    with open('Python_HW5/sjat.txt', 'w', encoding='utf-8') as W:
        P = W.write('')
    strN = ""
    for i in range(len(N)): 
        T = N[i].split()
        number = int(T[0])
        for j in range(number):
            strN = T[1]
            with open('Python_HW5/sjat.txt', 'a', encoding='utf-8') as W:
                P = W.write(strN)
            print(strN, end='')
    


if Mode == 1:
    Sjat(M)
else:
    Recov(N)
