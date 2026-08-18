import qrcode

data = input("ENTER TEXT TO LINK :")
img = qrcode.make(data)

img.save("img.png")
img.show()

print("QRCODE GENERATED...")