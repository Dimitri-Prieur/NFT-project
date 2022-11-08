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

        # Background image
        background = Image.open('./Images/template/background.png', 'r').convert('RGB') #Opens Template Image
        
        # At the end, this picture should be load randomly :
        special_picture = Image.open('./Images/football/DALL·E 2022-11-08 01.21.01 - A cyberpunk representation of soccer goal.png','r').convert('RGB')
        special_picture = special_picture.resize((630, 630))

        # Add pictures on the background 
        background.paste(qr_code, (100, 238))
        background.paste(special_picture, (1947, 120))



        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(background)

        # Add Text to an image
        I1.text((28, 36), self.message, fill=(255, 0, 0))


        return background
