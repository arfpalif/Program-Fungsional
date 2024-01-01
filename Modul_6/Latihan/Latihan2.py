from PIL import Image, ImageDraw, ImageFont, ImageFilter

gambarku = Image.open("C:\\Users\\HP\\Pictures\\Foto instacom\\_DSC0635.jpg")
overlay = Image.open("C:\\Users\\HP\\Documents\\Documents PC\\UMM_Logo.png")

gambarBW = gambarku.convert("L")

teks_layer = Image.new("L", gambarku.size, 255)  
teks_draw = ImageDraw.Draw(teks_layer)

font = ImageFont.truetype("arial.ttf", 100)
text = "Alif Raihan Firman P - 202110370311254"
bbox = teks_draw.textbbox((0, 0), text, font)

text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2

teks_draw.text((text_x, text_y), text, font=font, fill=0) 

teks_layer = teks_layer.rotate(30, resample=Image.BICUBIC, expand=True)
teks_layer = teks_layer.filter(ImageFilter.BLUR)

gambarBW.paste(teks_layer, (0, 0), teks_layer)

gambarBW.save("C:\\Users\\HP\\Pictures\\Foto instacom\\CobaBaru.jpg")

gambarBW.show()
