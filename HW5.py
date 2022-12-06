# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

with open ('Python_HW5/file.txt', 'r',encoding='utf-8') as F:
    S = F.read()
    listS = list(map(str, S.split()))
    print(listS)
    newList = []
    for i in range(len(listS)):
        if 'а' in listS[i] or 'б' in listS[i] or 'в' in listS[i]:
            i += 1
        else:
            newList.append(listS[i])
    print(newList)