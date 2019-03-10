from .utils import index_closest, index_furthest
from .input import W, H, M00_ij, Xis, Yis, YYis, DDELTA

ij_def = set()
for i1 in range(W):
    for j1 in range(H):
        ij_def.add((i1, j1))


def ij_to_f(i, j):
    return j * W + i


def f_to_ij(f):
    q = f // W
    r = f - q * W
    return r, q


f_def = {ij_to_f(i, j) for i, j in ij_def}


i0, j0 = M00_ij


def ij_to_xy(i, j):
    return i - i0, -j + j0


def xy_to_ij(x, y):
    return x + i0, -y + j0


xy_def = {ij_to_xy(i, j) for i, j in ij_def}


def f_to_xy(f):
    i, j = f_to_ij(f)
    return ij_to_xy(i, j)


def xy_to_f(x, y):
    i, j = xy_to_ij(x, y)
    return ij_to_f(i, j)


def _cross_ratio(z0, z1, z2, z3):
    return (z2-z0)*(z3-z1)*1/(z3-z0)*1/(z2-z1)


def _zz(z0, z1, z2, z, zz0, zz1, zz2):
    cr = _cross_ratio(z0, z1, z2, z)
    return (zz1*zz2-zz1*zz0-cr*zz0*zz2+cr*zz0*zz1)/(zz2-zz0-cr*zz2+cr*zz1)


def _zz_from_3_furthest(zis, z, zzis):
    zis = zis[:]
    zzis = zzis[:]
    while len(zis) > 3:
        ie = index_closest(zis, z)
        zis.pop(ie)
        zzis.pop(ie)
    z0, z1, z2 = zis
    zz0, zz1, zz2 = zzis
    return _zz(z0, z1, z2, z, zz0, zz1, zz2)


def _yy(y):
    return _zz_from_3_furthest(Yis, y, YYis)


def _xx(x, y):
    index_origin = index_furthest(Yis, y)
    indexes = [0, 1, 2, 3]
    indexes.pop(index_origin)
    index_inter = min(indexes)

    delta_horizontal_inter = Xis[index_inter]
    xis_inter = [k * delta_horizontal_inter for k in range(-2, 3)]

    y_origin = Yis[index_origin]
    y_inter = Yis[index_inter]
    x_inter = (y_inter-y_origin)*x / (y-y_origin)

    xxis_inter = [k * DDELTA for k in range(-2, 3)]

    xx_inter = _zz_from_3_furthest(xis_inter, x_inter, xxis_inter)

    yy = _yy(y)

    return (yy - index_origin * DDELTA) * xx_inter / (DDELTA * (index_inter - index_origin))


_xy_to_xxyy_dict = {}
for x1, y1 in xy_def:
    _xy_to_xxyy_dict[(x1, y1)] = _xx(x1, y1), _yy(y1)


def xy_to_xxyy(x, y):
    return _xy_to_xxyy_dict[(x, y)]


_ij_to_xxyy_dict = {}
for i1, j1 in ij_def:
    x1, y1 = ij_to_xy(i1, j1)
    _ij_to_xxyy_dict[(i1, j1)] = xy_to_xxyy(x1, y1)


def ij_to_xxyy(i, j):
    return _ij_to_xxyy_dict[(i, j)]


_f_to_xxyy_dict = {}
for f1 in f_def:
    x1, y1 = f_to_xy(f1)
    _f_to_xxyy_dict[f1] = xy_to_xxyy(x1, y1)


def f_to_xxyy(f):
    return _f_to_xxyy_dict[f]
