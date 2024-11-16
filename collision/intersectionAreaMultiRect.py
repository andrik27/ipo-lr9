class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    return rect[0][0] < rect[1][0] and rect[0][1] < rect[1][1]

def intersectionArea(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("Некорректный прямоугольник: " + str(rect1))
    if not isCorrectRect(rect2):
        raise RectCorrectError("Некорректный прямоугольник: " + str(rect2))

    x_overlap = max(0, min(rect1[1][0], rect2[1][0]) - max(rect1[0][0], rect2[0][0]))
    y_overlap = max(0, min(rect1[1][1], rect2[1][1]) - max(rect1[0][1], rect2[0][1]))

    return x_overlap * y_overlap

def intersectionAreaMultiRect(rects):
    n = len(rects)
    for rect in rects:
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Некорректный прямоугольник: {rect}")
    
    total_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_area += intersectionArea(rects[i], rects[j])
    
    return total_area
