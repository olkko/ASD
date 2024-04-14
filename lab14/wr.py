class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"


def orientation(p1: Point, p2: Point, p3: Point) -> float:
    w = (p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)
    if w == 0:
        return 1  # współliniowe
    elif w < 0:
        return 2  # lewoskrętne
    else:
        return 3  # prawoskrętne


def find_leftmost(points):
    leftmost = points[0]
    for i in range(len(points)):
        if points[i].x < leftmost.x:
            leftmost = points[i]
        elif points[i].x == leftmost.x:
            if points[i].y < leftmost.y:
                leftmost = points[i]
    return leftmost


def convex_hull(points):
    start = find_leftmost(points)
    hull = []
    current_point = start
    while True:
        if current_point not in hull:
            hull.append(current_point)
        for i in range(len(points)):
            if points[i] == current_point:
                if i == len(points) - 1:
                    i = -1
                next_point = points[i + 1]
        for i in range(len(points)):
            candidate = points[i]
            if orientation(current_point, next_point, candidate) == 3:
                next_point = candidate
        current_point = next_point
        if current_point == start:
            break
    return hull


def convex_hull2(points):
    start = find_leftmost(points)
    hull = []
    current_point = start
    while True:
        if current_point not in hull:
            hull.append(current_point)
        for i in range(len(points)):
            if points[i] == current_point:
                if i == len(points) - 1:
                    i = -1
                next_point = points[i + 1]
        for i in range(len(points)):
            candidate = points[i]
            if orientation(current_point, candidate, next_point) == 1:
                if current_point.x < next_point.x < candidate.x:
                    next_point = candidate
                elif current_point.x == next_point.x == candidate.x and current_point.y < next_point.y < candidate.y:
                    next_point = candidate
                elif candidate.x < next_point.x < current_point.x:
                    next_point = candidate
                elif candidate.x == next_point.x == current_point.x and candidate.y < next_point.y < current_point.y:
                    next_point = candidate
            elif orientation(current_point, candidate, next_point) == 2:
                next_point = candidate
        current_point = next_point
        if current_point == start:
            break
    return hull


def main():
    points1 = [Point(0, 3), Point(0, 0), Point(0, 1), Point(3, 0), Point(3, 3)]
    points2 = [Point(0, 3), Point(0, 1), Point(0, 0), Point(3, 0), Point(3, 3)]
    points3 = [Point(2, 2), Point(4, 3), Point(5, 4), Point(0, 3), Point(
        0, 2), Point(0, 0), Point(2, 1), Point(2, 0), Point(4, 0)]

    hull1 = convex_hull(points3)
    hull2 = convex_hull2(points3)

    print("Wypukła otoczka (metoda 1):", end=" ")
    for point in hull1:
        print(point, end=" ")
    print()

    print("Wypukła otoczka (metoda 2):", end=" ")
    for point in hull2:
        print(point, end=" ")
    print()


if __name__ == '__main__':
    main()
