import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://www.youtube.com/channel/UCCE5GkKcYhjBjNPaUO_mRyA"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("mahout.svg", scale=8)
