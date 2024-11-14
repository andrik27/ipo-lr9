def isCorrectRect(point1,point2):
    flag = False
    if(point1[0] < point2[0] and point1[1] < point2[1]):
                flag = True
    return print(flag)


spis1 = []
spis2 = []
pointX1 = float(input('Введите x1: '))
spis1.append(pointX1)
pointY1 = float(input('Введите y1: '))
spis1.append(pointY1)

pointX2 = float(input('Введите x2 : '))
spis2.append(pointX2)
pointY2 = float(input('Введите y2 : '))
spis2.append(pointY2)

spis1 = tuple(spis1)
spis2 = tuple(spis2)

isCorrectRect(spis1, spis2)