def orientation(p, q, r):
    value = (q[1] - p[1])*(r[0]-q[0])-(q[0]-p[0])*(r[1]-q[1])
    if value == 0:
        return 0
    
    if value>0:
        return 1
    
    if value<0:
        return 2
        
def find_convex_hull(points):
    convex_hull = []
    p = points[0]
    q = points[1]
    convex_hull.append(p)

    for r in points[2:]:
        if orientation(p, q, r) == 1:
            q = r
        else:
            convex_hull.append(q)
            p = q
            q = r

    convex_hull.append(q)

    return convex_hull


def find_convex_hull_better_vers(points):
    convex_hull = []
    p = points[0]
    q = points[1]
    convex_hull.append(p)

    for r in points[2:]:
        if orientation(p, q, r) == 1:
            q = r
        elif orientation(p, q, r) == 2:
            q = r

    convex_hull.append(q)

    return convex_hull



if __name__ == '__main__':
    points1 = ((0, 3), (0, 0), (0, 1), (3, 0), (3, 3))
    points2 = ((0, 3), (0, 1), (0, 0), (3, 0), (3, 3))
    print(find_convex_hull(points1))
    print(find_convex_hull(points2))

    print(find_convex_hull_better_vers(points1))
    print(find_convex_hull_better_vers(points2))

    points3 = (2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)
    print(find_convex_hull(points3))
    print(find_convex_hull_better_vers(points3))