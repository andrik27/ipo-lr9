class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    return rect[0][0] < rect[1][0] and rect[0][1] < rect[1][1]

def isCollisionRect(rects):
    rect1, rect2 = rects
    rects = tuple(rects)
    if not isCorrectRect(rect1):
        raise RectCorrectError("Первый прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("Второй прямоугольник некорректный")

    # Проверяем пересечение прямоугольников
    if rect1[0][0] > rect2[1][0] or rect2[0][0] > rect1[1][0]:
        return False
    if rect1[0][1] > rect2[1][1] or rect2[0][1] > rect1[1][1]:
        return False
    return True

def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("Первый прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("Второй прямоугольник некорректный")

    if not isCollisionRect((rect1, rect2)):
        return 0

    x_overlap = max(0, min(rect1[1][0], rect2[1][0]) - max(rect1[0][0], rect2[0][0]))
    y_overlap = max(0, min(rect1[1][1], rect2[1][1]) - max(rect1[0][1], rect2[0][1]))

    return x_overlap * y_overlap

# Функция для ввода координат с клавиатуры
def input_coordinates():
    pointX1 = float(input('Введите координаты левого нижнего угла по иксу: '))
    pointY1 = float(input('Введите координаты левого нижнего угла по игрику: '))
    pointX2 = float(input('Введите координаты правого верхнего угла по иксу: '))
    pointY2 = float(input('Введите координаты правого верхнего угла по игрику: '))
    
    return [(pointX1, pointY1), (pointX2, pointY2)]

# Ввод координат для двух прямоугольников
print("Введите координаты первого прямоугольника:")
rect1 = input_coordinates()
print("Введите координаты второго прямоугольника:")
rect2 = input_coordinates()

# Проверка пересечения прямоугольников и вычисление площади пересечения
try:
    Area = intersectionAreaRect(rect1, rect2)
    print(f"Площадь пересечения: {Area}")
except RectCorrectError as e:
    print(e)
