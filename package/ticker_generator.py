from package.qr_code_generator import QrCodeGenerator
from PIL import Image, ImageDraw, ImageFont #Import PIL functions

class TicketGenerator:

    def __init__(self, message, url):
        self.message = message # Little message
        self.url = url # Qr code image

    def generateTicket(self):

        #Creating an instance of qrcode
        qr_code = QrCodeGenerator.generateQrCode(self.url).img
        qr_code = qr_code.resize((360, 360))

        background = Image.open('./Images/template/background.png', 'r').convert('RGB') #Opens Template Image
        background.paste(qr_code, (100,238))

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(background)

        # Add Text to an image
        I1.text((28, 36), self.message, fill=(255, 0, 0))


        return background
