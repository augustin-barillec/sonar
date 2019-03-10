from .utils import line_shift
from .coordinate import xy_def, ij_to_xy, xy_to_ij, f_to_xy, xy_to_f


def xy_line(m1_xy, m2_xy):
    if m1_xy == m2_xy:
        raise ValueError('The two points must be distinct')
    res = []
    for x, y in xy_def:
        dl = line_shift(m1_xy, m2_xy, (x, y))
        dr = line_shift(m1_xy, m2_xy, (x+1, y))
        ur = line_shift(m1_xy, m2_xy, (x+1, y+1))
        ul = line_shift(m1_xy, m2_xy, (x, y+1))
        if not ((dl > 0 and dr > 0 and ur > 0 and ul > 0) or (dl < 0 and dr < 0 and ur < 0 and ul < 0)):
            res.append((x, y))
    if m1_xy[0] != m2_xy[0]:
        res = sorted(res, key=lambda m_xy: m_xy[0])
    else:
        res = sorted(res, key=lambda m_xy: m_xy[1])
    return res


def ij_line(m1_ij, m2_ij):
    m1_xy = ij_to_xy(m1_ij[0], m1_ij[1])
    m2_xy = ij_to_xy(m2_ij[0], m2_ij[1])
    return [xy_to_ij(x, y) for x, y in xy_line(m1_xy, m2_xy)]


def f_line(m1_f, m2_f):
    m1_xy = f_to_xy(m1_f)
    m2_xy = f_to_xy(m2_f)
    return [xy_to_f(x, y) for x, y in xy_line(m1_xy, m2_xy)]
