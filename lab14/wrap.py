import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_leftmost_point(points):
    leftmost = points[0]
    for point in points:
        if point.x < leftmost.x or (point.x == leftmost.x and point.y < leftmost.y):
            leftmost = point
    return leftmost

def is_left_turn(p, q, r):
    return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x) > 0

def is_collinear(p, q, r):
    return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x) == 0

def is_between(p, q, r):
    if not is_collinear(p, q, r):
        return False
    if p.x != q.x:
        return p.x <= r.x <= q.x or q.x <= r.x <= p.x
    else:
        return p.y <= r.y <= q.y or q.y <= r.y <= p.y

def distance(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def find_farthest_collinear_point(p, q, points):
    farthest_point = q
    for point in points:
        if is_collinear(p, q, point) and point != q:
            if distance(p, point) > distance(p, farthest_point):
                farthest_point = point
    return farthest_point

def compute_convex_hull_v1(points):
    p = find_leftmost_point(points)
    hull = [p]
    q = None
    while q != hull[0]:
        if q is None:
            q = points[(points.index(p) + 1) % len(points)]
        r = points[(points.index(q) + 1) % len(points)]
        if is_left_turn(p, q, r):
            hull.append(q)
            p = q
            q = r
        elif is_collinear(p, q, r) and is_between(p, q, r):
            q = r
        else:
            q = find_farthest_collinear_point(p, q, points)
    return hull

def compute_convex_hull_v2(points):
    p = find_leftmost_point(points)
    hull = [p]
    q = None
    while q != hull[0]:
        if q is None:
            q = points[(points.index(p) + 1) % len(points)]
        r = points[(points.index(q) + 1) % len(points)]
        if is_left_turn(p, q, r):
            hull.append(q)
            p = q
            q = r
        elif is_collinear(p, q, r) and is_between(p, q, r):
            q = find_farthest_collinear_point(p, q, points)
        else:
            q = r
    return hull

def print_points(points):
    for point in points:
        print(f"({point.x}, {point.y})", end=" ")
    print()

# Test Case 1
points1 = [Point(0, 3), Point(0, 0), Point(0, 1), Point(3, 0), Point(3, 3)]
convex_hull1_v1 = compute_convex_hull_v1(points1)
print("Convex Hull (Version 1):")
print_points(convex_hull1_v1)

convex_hull1_v2 = compute_convex_hull_v2(points1)
print("Convex Hull (Version 2):")
print_points(convex_hull1_v2)

# Test Case 2
points2 = [Point(0, 3), Point(0, 1), Point(0, 0), Point(3, 0), Point(3, 3)]
convex_hull2_v1 = compute_convex_hull_v1(points2)
print("Convex Hull (Version 1):")
print_points(convex_hull2_v1)

convex_hull2_v2 = compute_convex_hull_v2(points2)
print("Convex Hull (Version 2):")
print_points(convex_hull2_v2)

# Test Case 3
points3 = [Point(2, 2), Point(4, 3), Point(5, 4), Point(0, 3), Point(0, 2), Point(0, 0), Point(2, 1), Point(2, 0), Point(4, 0)]
convex_hull3_v1 = compute_convex_hull_v1(points3)
print("Convex Hull (Version 1):")
print_points(convex_hull3_v1)

convex_hull3_v2 = compute_convex_hull_v2(points3)
print("Convex Hull (Version 2):")
print_points(convex_hull3_v2)
