import qrcode

class QrCodeGenerator:

    # Link for website
    url = "https://jardinage.lemonde.fr/images/dossiers/2017-09/castor-113620.jpg"

    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version = 1,
            box_size = 10,
            border = 5,
        )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    @classmethod
    def get_qr_code_picture(cls):
        return Generate(url = cls.url, img = cls.img)

class Generate:
    def __init__(self, url, img):
        self.url = url
        self.img = img

test = QrCodeGenerator.get_qr_code_picture()
print(test.url)
print(test.img)