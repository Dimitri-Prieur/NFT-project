import qrcode

class QrCodeGenerator:

    @classmethod
    def generateQrCode(cls, url: str):
        #Creating an instance of qrcode
        qr = qrcode.QRCode(
                version = 1,
                box_size = 10,
                border = 5,
            )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        return Response(url = url, img = img)

class Response:
    def __init__(self, url, img):
        self.url = url
        self.img = img


