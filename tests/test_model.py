from PIL import Image
from sonar.model import angle_reco

im = Image.open('calibration.jpg')
print(angle_reco(im))
