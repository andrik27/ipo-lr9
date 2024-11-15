from collision.isCorrectRect import isCorrectRect, RectCorrectError 
from collision.isCollisionRect import isCollisionRect
from collision.intersectionAreaRect import intersectionAreaRect


def main():
    while True:
        number = int(input("Выберите: 1 - isCorrectRect, 2 - isCollisionRect, 3 - intersectionAreaRect, 5 - Выход: "))
        
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
                isCorrectRect((spis1, spis2))
                print("Прямоугольник корректный")
            except RectCorrectError as e:
                print(e)
        
        elif number == 2:
            print("Введите координаты первого прямоугольника:")
            rect1 = input_coordinates()
            print("Введите координаты второго прямоугольника:")
            rect2 = input_coordinates()
            rects = [rect1, rect2]
            rects = tuple(rects)
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
        
        elif number == 5:
            print("Выход")
            break
        else:
            print(f"Вы ввели {number}. Чтобы продолжить, введите корректное число.")
main()
