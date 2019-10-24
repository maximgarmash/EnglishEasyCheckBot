filename = 'english-module.txt'

eng_dict = {}
with open(filename, 'r', encoding='utf-8') as file:
    for line in file.read().splitlines():
        eng_dict[line.split('\t')[0]] = line.split('\t')[1]
print(eng_dict)




# import fleep
    # info = fleep.get(f.read(128))
#
# print(info.type)
# print(info.extension)
# print(info).mime)
#
# print(info.type_matches("raster-image"))
# print(info.extension_matches("gif"))
# print(info.mime_matches("image/png"))