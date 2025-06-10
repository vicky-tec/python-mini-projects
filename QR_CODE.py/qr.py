import qrcode 
from PIL import Image, ImageDraw, ImageFont

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10, border=4,)
qr.add_data("https://vicky-tec.github.io/TRAVALLY_/")
qr.make(fit=True)
img=qr.make_image(fill_color="purple", back_color="Aqua")
img.save("TRAVALY_.png")


#------BASIC------------------
# img = qr.make("Link!")
# img.save(".png")
