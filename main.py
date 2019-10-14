import magic


file = u'Книга'
# file_magic = magic.Magic(magic_file="D:\Distr\Python\Projects\EnglishEasyCheckBot\env\Scripts")
print(magic.from_file(file, mime=True))
