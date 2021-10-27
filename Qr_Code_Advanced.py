import qrcode
qr = qrcode.QRCode(
    version = 10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(" Hi This Is Test QRCode ")
qr.make(fit=True)

img = qr.make_image(fill_color="blue",back_color="black")
img.save("Anand_Advanced.png")