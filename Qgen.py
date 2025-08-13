from qrcode import QRCode

qr = QRCode(border=10, box_size=100)

qr.add_data("www.google.com")
qr.make(fit=True)
img = qr.make_image()
img.show()