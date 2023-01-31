import qrcode as qr

link = input("Enter Your URL : ")
img = qr.make(link)
img.save("YourQr.png")