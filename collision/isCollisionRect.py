class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    return rect[0][0] < rect[1][0] and rect[0][1] < rect[1][1]

def isCollisionRect(rects):
    rect1, rect2 = rects
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некорректный")
    # Проверяем пересечение прямоугольников
    if rect1[0][0] > rect2[1][0] or rect2[0][0] > rect1[1][0]:
        return False
    if rect1[0][1] > rect2[1][1] or rect2[0][1] > rect1[1][1]:
        return False
    return True
