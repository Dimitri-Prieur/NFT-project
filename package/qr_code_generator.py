import qrcode

class QrCodeGenerator:

    @classmethod
    def generateQrCode(cls, url: str):
        #Creating an instance of qrcode
        qr = qrcode.QRCode(
                version = 1,
                box_size = 15,
                border = 0,
            )
        qr.add_data(url)
        qr.make(fit = True)
        img = qr.make_image(
            fill_color = (255, 193, 59),
            back_color=(30, 61, 89)
        )
        return Response(url = url, img = img)

class Response:
    def __init__(self, url, img):
        self.url = url
        self.img = img


