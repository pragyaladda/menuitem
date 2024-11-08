from pyqrcode import QRCode

# Define the URL to encode
url = "https://rishabhjadia.github.io/pmenuitem/"

# Create the QRCode object for the URL as text
qr = QRCode(url)

# Save the QR code as a PNG image
qr.png('menu_qr.png', scale=8)  # Adjust scale for desired size

print("QR code generated successfully! Saved as menu_qr.png")