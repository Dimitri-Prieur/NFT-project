from .qr_code_generator import QrCodeGenerator
from PIL import Image, ImageDraw, ImageFont #Import PIL functions
from datetime import datetime
import json

class TicketGenerator:

    def __init__(self, id: str, url: str, price: float, picture: str, title: str, subtitle: str, date: datetime, seat: str = None, location: str = None):
        """Initializing ticket

        Args:
            id (str): ticket id
            url (str): ticket QR Code url
            price (float): ticket price
            picture (str): ticket picture
            
            title (str): event title
            subtitle (str): event subtitle
            date (datetime): event date. Format -> dd/mm/yy hh:mm:ss
            
            seat (str, optional): seat number. Defaults to None.
            location (str, optional): event location. Defaults to None.
        """
        
        # Ticket
        self.id = id
        self.url = url # qr code url
        self.price = price
        self.picture = picture # picture
        self.seat = seat
        
        # Event
        self.title = str(title).upper() # main title
        self.subtitle = str(subtitle).upper() # sub title
        self.location = location

        formatted_date = datetime.strptime(date, '%d/%m/%Y %H:%M:%S')
        self.day = formatted_date.strftime('%b %d %Y')
        self.hour = formatted_date.strftime('%I:%M%p')
        self.date = date # date
        
    
    def generate_picture(self):
        """generate ticket

        Returns:
            image at png format
        """
        # Creating an instance of qrcode
        qr_code = QrCodeGenerator.generateQrCode(self.url).img
        qr_code = qr_code.resize((360, 360))

        # Background image
        background = Image.open('./ressources/template/background.png', 'r').convert('RGB') #Opens Template Image
        
        # Special picture
        special_picture = Image.open(self.picture,'r').convert('RGB')
        special_picture = special_picture.resize((630, 630))

        # Add special picture on the background 
        background.paste(qr_code, (100, 238))
        background.paste(special_picture, (1947, 120))

        def addNewDraw(text: str, x_pos: str, y_pos: str, fontsize: str, fontcolor: tuple, fontwidth: int = 1):
            """Add text on the picture

            Args:
                text (str): the text added on the picutre
                x_pos (str): text x position
                y_pos (str): text y position
                fontsize (str): text fontsize
                fontcolor (tuple): text fontcolor (r, g, b)
                fontwidth (int, optional): text fontwidth. Defaults to 1.
            """
            draw = ImageDraw.Draw(background)
            myFont = ImageFont.truetype("./ressources/courrier_new.ttf", fontsize)
            w, h = draw.textsize(text, font = myFont)
            draw.text((x_pos - (w/2), y_pos - (h/2)), text, font= myFont, stroke_width=fontwidth, fill=fontcolor)

        # Initialize color
        blue_color = (30, 61, 89)
        orange_color = (255, 193, 59)
        
        # Display title
        addNewDraw(self.title, 1220, 320, 120, blue_color, 3)
       
        # Display subtitle
        addNewDraw(self.subtitle, 1220, 500, 90, blue_color, 3)
        
        # Display day
        addNewDraw(self.day, 280, 190, 50, orange_color, 1)
        
        # Display hour
        addNewDraw(self.hour, 280, 635, 50, orange_color, 1)

        # Display no refund
        _text = "No refund / No exchange"
        addNewDraw(_text, 815, 815, 38, (245, 240, 225))
        
        return background


    # Create JSON
    def generate_json(self):       
        data = {}
        data['event_date'] = self.date
        data['event_location'] = self.location
        data['event_title'] = self.title.lower()
        data['event_subtitle'] = self.subtitle.lower()
        
        data['ticket_seat'] = self.seat
        data['ticket_price'] = self.price
        data['ticket_id'] = self.id
        
        return json.dumps(data)