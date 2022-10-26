# main.py
import package

qr_code = package.QrCodeGenerator.generateQrCode("https://jardinage.lemonde.fr/images/dossiers/2017-09/castor-113620.jpg")
qr_code.img.save('generated_qr_code.png')
print(qr_code.url)
