# user input
W, H = 160, 120

M00_ij = 80, 118
M01_ij = 80, 93
M02_ij = 80, 81
M03_ij = 80, 73

M10_ij = 135, 118
M11_ij = 117, 93
M12_ij = 108, 81
M13_ij = 102, 73

Mm10_ij = 25, 118
Mm11_ij = 43, 93
Mm12_ij = 52, 81
Mm13_ij = 58, 73

DDELTA = 1
DDISTANCE_CAR_ORIGIN = 1
AANGLE_GROUND_CAMERA = 80

GROUND_COLOR = (152, 157, 161)
BROKEN_LINE_COLOR = (228, 215, 163)
SOLID_LINE_COLOR = (247, 255, 255)


# useful variables
X0 = M10_ij[0] - M00_ij[0]
X1 = M11_ij[0] - M01_ij[0]
X2 = M12_ij[0] - M02_ij[0]
X3 = M13_ij[0] - M03_ij[0]

Y1 = M00_ij[1] - M01_ij[1]
Y2 = M00_ij[1] - M02_ij[1]
Y3 = M00_ij[1] - M03_ij[1]

Xis = [X0, X1, X2, X3]
Yis = [0, Y1, Y2, Y3]

YYis = [k*DDELTA for k in range(4)]

# check cross_ratio_max_on_pic
cross_ratio_max_on_pic = round(Y2*(H-Y1)/(H*(Y2-Y1)), 2)

# if cross_ratio_max_on_pic > 1.95:
#     raise ValueError('cross_ratio_max_on_pic = {}. It must be less than 1.95'.format(cross_ratio_max_on_pic))
