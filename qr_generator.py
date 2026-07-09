import qrcode

data = input("Enter text or URL")

qr = qrcode.make(data)

file_name = input("Enter file name(without .png):")

qr.save(file_name + ".png")
print(f"QR Code Saved as {file_name}.png")
