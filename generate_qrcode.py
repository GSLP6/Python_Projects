import qrcode
#QRCode - Generate QRCODE
#VERSION - Determines size of the QRCODE, and range is from 1 to 40
#Box_size - Each box size in the qrcode grid(pixels)
#border = border around the QRCODE


qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
#data -  define the data that you want to encode in the QRCODE.
#qr.add_data(data) -  this method adds the specified data
#qr.make(fit=True) - it generates the qrcode and fit the entire data within the qrcode


data = "www.linkedin.com/in/sai-lakshmi-prasanna-ghantasala-b75699167"
qr.add_data(data)
qr.make(fit=True)


#qr.make_image - this method creates image of the QRCODE
#fill="black" specifies the color of the QR code itself (the squares), which is set to black.
#back_color="white" specifies the background color of the QR code image, which is set to white.
img = qr.make_image(fill="black", back_color="white")
# Generate and save the QR code image
img.save("test.png")
