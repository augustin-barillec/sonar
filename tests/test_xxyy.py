from PIL import Image
from sonar.utils import *
from sonar.input import *
from sonar.coordinate import *
from sonar.line import *

im = Image.open("calibration.jpg")
px = im.load()

ij_line1 = ij_line(M00_ij, M10_ij)
ij_line2 = ij_line(M11_ij, Mm13_ij)
ij_line3 = ij_line(Mm12_ij, Mm10_ij)

for i, j in ij_line1:
    px[i, j] = (255, 0, 0)
for i, j in ij_line2:
    px[i, j] = (0, 255, 0)
for i, j in ij_line3:
    px[i, j] = (0, 0, 255)

center_xxyy = xy_to_xxyy(0, 0)

for x, y in xy_def:
    m_xxyy = xy_to_xxyy(x, y)
    if 1 < distance(center_xxyy, m_xxyy) < 2:
        i, j = xy_to_ij(x, y)
        px[i, j] = (0, 0, 0)

for f in f_def:
    m_xxyy = f_to_xxyy(f)
    if 4 < distance(center_xxyy, m_xxyy) < 5:
        i, j = f_to_ij(f)
        px[i, j] = (0, 0, 0)

im.show()
