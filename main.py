import fleep


file_pdf = 'Книга'
file_jpg = 'photo_jpg'
file_mp3 = 'single_mp3'
file_png = 'logo_png'
file_json = 'answer_json'
with open(file_jpg, 'rb') as f:
    info = fleep.get(f.read(128))

print(info.type)
print(info.extension)
print(info.mime)

print(info.type_matches("raster-image"))
print(info.extension_matches("gif"))
print(info.mime_matches("image/png"))