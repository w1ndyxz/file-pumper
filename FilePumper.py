import os

filePath = input("You can move file to console\nPath: ")
_, fileName = os.path.split(filePath)
chooseByte = int(input("1 - BYTE | 2 - KILOBYTE | 3 - MEGABYTE | 4 - GIGABYTE\nChoose: "))
chooseSize = int(input("Size: "))


selectedByte = (lambda x: {1: 1, 2: 1024, 3: 1048576, 4: 1073741824}.get(x, "UNKNOWN"))(chooseByte)
outSize = selectedByte * chooseSize

with open(filePath, 'rb') as src:
    data = src.read()

with open(f"{_}\\PUMP_{fileName}", 'wb') as outf:
    outf.write(data)
    outf.write(b"\x00" * outSize)


input("Created :)")