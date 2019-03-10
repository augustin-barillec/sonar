from .utils import angle_deg, distance, last_long_block, index_closest
from .input import SOLID_LINE_COLOR
from .coordinate import xy_to_xxyy, xy_def, xy_to_f, f_to_xxyy
from .line import f_line

line1_yy_wished = 2
line2_yy_wished = 3

y_min = min(m_xy[1] for m_xy in xy_def)
y_max = max(m_xy[1] for m_xy in xy_def)
ys = list(range(y_min, y_max+1))

yys = []
for y in ys:
    xx, yy = xy_to_xxyy(0, y)
    yys.append(yy)

index1 = index_closest(yys, line1_yy_wished)
index2 = index_closest(yys, line2_yy_wished)
y1 = ys[index1]
y2 = ys[index2]

f_line1 = f_line(xy_to_f(0, y1), xy_to_f(1, y1))
f_line2 = f_line(xy_to_f(0, y2), xy_to_f(1, y2))


def angle_reco(im):

    l = im.getdata()

    pixel_line1 = [l[f] for f in f_line1]
    pixel_line2 = [l[f] for f in f_line2]

    mask_line1 = [distance(pixel, SOLID_LINE_COLOR) < 45 for pixel in pixel_line1]
    mask_line2 = [distance(pixel, SOLID_LINE_COLOR) < 45 for pixel in pixel_line2]

    try:
        m1_f = f_line1[last_long_block(mask_line1, True, 4)[0]]
        m2_f = f_line2[last_long_block(mask_line2, True, 4)[0]]
    except TypeError:
        return 0

    m1_xx, m1_yy = f_to_xxyy(m1_f)
    m2_xx, m2_yy = f_to_xxyy(m2_f)

    angle_horizontal_road_deg = angle_deg((1, 0), (m2_xx-m1_xx, m2_yy-m1_yy))
    reco_counterclockwise_deg = angle_horizontal_road_deg - 90
    reco_clockwise_deg = -reco_counterclockwise_deg

    return reco_clockwise_deg
