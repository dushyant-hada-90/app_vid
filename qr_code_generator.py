import qrcode

laptop_ip = "10.93.16.202"  # Replace with your laptop's IP
port = 8000
url = f"http://{laptop_ip}:{port}/"

qr = qrcode.make(url)
qr.save("qr_code.png")
print("✅ QR Code saved as qr_code.png")
