from package.qr_code_generator import QrCodeGenerator
from PIL import Image, ImageDraw, ImageFont #Import PIL functions
from datetime import datetime

class TicketGenerator:

    def __init__(self, message: str, url: str, title: str, subtitle: str, date: datetime, picture: str):
        self.message = message # Little message
        self.url = url # Qr code image
        self.title = str(title).upper()
        self.subtitle = str(subtitle).upper()
        self.picture = picture

        test = datetime.strptime(date, '%d/%m/%Y %H:%M:%S')
        self.day = test.strftime('%b %d %Y')
        self.hour = test.strftime('%I:%M%p')

    def generateTicket(self):

        #Creating an instance of qrcode
        qr_code = QrCodeGenerator.generateQrCode(self.url).img
        qr_code = qr_code.resize((360, 360))

        # Background image
        background = Image.open('./ressources/template/background.png', 'r').convert('RGB') #Opens Template Image
        
        # At the end, this picture should be load randomly :
        special_picture = Image.open(self.picture,'r').convert('RGB')
        special_picture = special_picture.resize((630, 630))

        # Add pictures on the background 
        background.paste(qr_code, (100, 238))
        background.paste(special_picture, (1947, 120))


        # Il faudra mettre une limite de caractère maximale

        def addNewDraw(text, width, heigth, fontsize, fontcolor, fontwidth:int = 1):
            draw = ImageDraw.Draw(background)
            myFont = ImageFont.truetype("./ressources/courrier_new.ttf", fontsize)
            w, h = draw.textsize(text, font = myFont)
            draw.text((width - (w/2), heigth - (h/2)), text, font= myFont, stroke_width=fontwidth, fill=fontcolor)

        # Display title
        blue_color = (30, 61, 89)
        orange_color = (255, 193, 59)
        addNewDraw(self.title, 1220, 320, 120, blue_color, 3)
       
        # Display subtitle
        addNewDraw(self.subtitle, 1220, 500, 90, blue_color, 3)
        
        # Display day
        addNewDraw(self.day, 280, 190, 50, orange_color, 1)
        
        # Display day
        addNewDraw(self.hour, 280, 635, 50, orange_color, 1)

        # Display no refund
        text = "No refund / No exchange"
        addNewDraw(text, 815, 815, 38, (245, 240, 225))

        return background
