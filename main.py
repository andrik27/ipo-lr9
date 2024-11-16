from collision.isCorrectRect import isCorrectRect
from collision.isCollisionRect import isCollisionRect
from collision.intersectionAreaRect import intersectionAreaRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect, RectCorrectError

def input_coordinates():
    pointX1 = float(input('Введите координаты левого нижнего угла по иксу: '))
    pointY1 = float(input('Введите координаты левого нижнего угла по игрику: '))
    pointX2 = float(input('Введите координаты правого верхнего угла по иксу: '))
    pointY2 = float(input('Введите координаты правого верхнего угла по игрику: '))
    
    return [(pointX1, pointY1), (pointX2, pointY2)]

def main():
    while True:
        number = int(input("Выберите: 1 - isCorrectRect, 2 - isCollisionRect, 3 - intersectionAreaRect, 4 - intersectionAreaMultiRect, 5 - Выход: "))
        
        if number == 1:
            spis1 = []
            spis2 = []
            pointX1 = float(input('Введите x1: '))
            spis1.append(pointX1)
            pointY1 = float(input('Введите y1: '))
            spis1.append(pointY1)
            pointX2 = float(input('Введите x2: '))
            spis2.append(pointX2)
            pointY2 = float(input('Введите y2: '))
            spis2.append(pointY2)
            spis1 = tuple(spis1)
            spis2 = tuple(spis2)
            try:
                if isCorrectRect((spis1, spis2)):
                    print("Прямоугольник корректный")
                else:
                    print("Прямоугольник некорректный")
            except RectCorrectError as e:
                print(e)
        
        elif number == 2:
            print("Введите координаты первого прямоугольника:")
            rect1 = input_coordinates()
            print("Введите координаты второго прямоугольника:")
            rect2 = input_coordinates()
            rects = [rect1, rect2]
            try:
                result = isCollisionRect(rects)
                print(f"Пересекаются ли прямоугольники? {result}")
            except RectCorrectError as e:
                print(e)
        
        elif number == 3:
            print("Введите координаты первого прямоугольника:")
            rect1 = input_coordinates()
            print("Введите координаты второго прямоугольника:")
            rect2 = input_coordinates()
            try:
                area = intersectionAreaRect(rect1, rect2)
                print(f"Площадь пересечения: {area}")
            except RectCorrectError as e:
                print(e)

        elif number == 4:
            rects = []
            n = int(input("Введите количество прямоугольников: "))
            for i in range(n):
                print(f"Введите координаты прямоугольника {i + 1}:")
                rects.append(input_coordinates())
            try:
                total_area = intersectionAreaMultiRect(rects)
                print(f"Общая площадь пересечения: {total_area}")
            except RectCorrectError as e:
                print(e)
        
        elif number == 5:
            print("Выход")
            break
        else:
            print(f"Вы ввели {number}. Чтобы продолжить, введите корректное число.")

main()
