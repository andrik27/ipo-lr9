class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    return rect[0][0] < rect[1][0] and rect[0][1] < rect[1][1]

def isCollisionRect(rects):
    rect1, rect2 = rects

    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")

    # Проверяем пересечение прямоугольников
    if rect1[0][0] > rect2[1][0] or rect2[0][0] > rect1[1][0]:
        return False
    if rect1[0][1] > rect2[1][1] or rect2[0][1] > rect1[1][1]:
        return False
    return True

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

# Объединяем прямоугольники в список списков
rects = [rect1, rect2]
rects = tuple(rects)
# Проверка пересечения прямоугольников
try:
    result = isCollisionRect(rects)
    print(f"Пересекаются ли прямоугольники? {result}")
except RectCorrectError as e:
    print(e)
