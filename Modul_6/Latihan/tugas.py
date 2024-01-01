from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

gambarku = Image.open("C:\\Users\\HP\\Pictures\\Foto instacom\\UMM.jpg")
overlay = Image.open("C:\\Users\\HP\\Documents\\Documents PC\\UMM_Logo.png")

gambarku = gambarku.resize(
    (int(gambarku.width * 1), int(gambarku.height * 1)))

gambarBW = gambarku.convert("L")  

gambarBW = gambarBW.rotate(
    30, resample=Image.BICUBIC, expand=True)
gambarBW = gambarBW.filter(
    ImageFilter.GaussianBlur(radius=2))

overlay = overlay.resize((int(overlay.width * 0.3), int(overlay.height * 0.3)))

teks_overlay_layer = Image.new("RGBA", gambarku.size, (255, 255, 255, 0))
teks_overlay_draw = ImageDraw.Draw(teks_overlay_layer)

overlay_x = (gambarku.width - overlay.width) // 2
overlay_y = (gambarku.height - overlay.height) // 2


enhancer = ImageEnhance.Brightness(overlay)
overlay = enhancer.enhance(5)  

enhancer = ImageEnhance.Contrast(overlay)
overlay = enhancer.enhance(4)

teks_overlay_layer.paste(overlay, (overlay_x, overlay_y), overlay)

font_size = 24  
font = ImageFont.truetype("arial.ttf", font_size)
text = "Informatika Joss"
bbox_text = teks_overlay_draw.textbbox((0, 0), text, font)

text_width = bbox_text[2] - bbox_text[0]
text_height = bbox_text[3] - bbox_text[1]
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height + overlay.height + text_height) // 2

teks_overlay_draw.text((text_x, text_y), text, font=font, fill=(
    255, 255, 255, 255))    

gambarBW.paste(teks_overlay_layer, teks_overlay_layer)

gambarBW.save(
    "C:\\Users\\HP\\Pictures\\Foto instacom\\tugas_praktikum_enam.jpg")

gambarBW.show()
