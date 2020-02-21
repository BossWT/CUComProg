import math


def distance1(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


def distance2(p1, p2):
    dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return dist


def distance3(c1, c2):
    overlap = False
    dist = math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)
    if (dist <= c1[2] + c2[2]):
        overlap = True
    return dist, overlap


def perimeter(points):
    oldx = points[0][0]
    originx = points[0][0]
    oldy = points[0][1]
    originy = points[0][1]
    per = 0
    for i in range(1, len(points)):
        dist = math.sqrt((points[i][0] - oldx) ** 2 + (points[i][1] - oldy) ** 2)
        per += dist
        oldx = points[i][0]
        oldy = points[i][1]
    dist = math.sqrt((points[len(points) - 1][0] - originx) ** 2 + (points[len(points) - 1][1] - originy) ** 2)
    per += dist
    return per


exec(input().strip())
