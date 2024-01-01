import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageDraw, ImageFont

img = mpimg.imread('C:\\Users\\HP\\Pictures\\Foto instacom\\_DSC0635.jpg')
ima = Image.open('C:\\Users\\HP\\Pictures\\Foto instacom\\_DSC0635.jpg')
ima.save('C:\\Users\\HP\\Pictures\\Foto instacom\\_DSC0635Baru.jpg')

plt.imshow(ima)
plt.axis('off')
plt.show()
