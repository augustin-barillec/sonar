import math


def dotproduct(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))


def length(v):
    return math.sqrt(dotproduct(v, v))


def angle_rad(v1, v2):
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


pi = math.pi


def angle_deg(v1, v2):
    return angle_rad(v1, v2)*180/pi


def distance(m1, m2):
    v = [b-a for a, b in zip(m1, m2)]
    return length(v)


def line_shift(m1, m2, m):
    x1, y1 = m1
    x2, y2 = m2
    x, y = m
    return (x-x1)*(-(y2-y1)) + (y-y1)*(x2-x1)


def first_long_block(l, value, window_length):
    current_block_length = 0
    i = 0
    while i < len(l) and current_block_length < window_length:
        if l[i] == value:
            current_block_length += 1
        else:
            current_block_length = 0
        i += 1
    if current_block_length == window_length:
        j = i
        while j < len(l) and l[j] == value:
            j += 1
        return i-current_block_length, j-1
    else:
        return None


def last_long_block(l, value, window_length):
    current_block_length = 0
    i = len(l)-1
    while i >= 0 and current_block_length < window_length:
        if l[i] == value:
            current_block_length += 1
        else:
            current_block_length = 0
        i -= 1
    if current_block_length == window_length:
        j = i
        while j >= 0 and l[j] == value:
            j -= 1
        return j+1, i+current_block_length
    else:
        return None


def index_closest(zis, z):
    dists = [abs(z-zi) for zi in zis]
    return dists.index(min(dists))


def index_furthest(zis, z):
    dists = [abs(z-zi) for zi in zis]
    return dists.index(max(dists))
