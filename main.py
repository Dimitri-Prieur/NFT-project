# main.py
import package

url = "https://jardinage.lemonde.fr/images/dossiers/2017-09/castor-113620.jpg"

# Get qr code
qr_code = package.QrCodeGenerator.generateQrCode(url)

# Save and print output
qr_code.img.save('generated_qr_code.png')
print(qr_code.url)
