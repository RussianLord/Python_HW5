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


N = 'AAADDDDDAABBBCC'
Mode = int(input('Нажми 1, чтобы выбрать сжатие, нажми 2, чтобвы выбрать восстановление... '))

def Sjat(N):
    K = 0
    listN = []
    for i in range(K, len(N)):
        if N[K] != N[i]:
            listN.append((i-K, N[i-1]))
            K = i
    listN.append((i-K+1, N[i-1]))
    print(listN)

    # change = int(input('Восстановить файл?...Да - 1... '))
    # if change == 1:
    #     Recov(N)

Sjat(N)

# def Recov(N):


# if Mode == 1:
#     Sjat(N)
# else:
#     Recov(N)
