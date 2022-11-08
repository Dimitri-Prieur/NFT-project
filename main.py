# main.py
import package

url = "https://google.fr"

amaztemp = package.TicketGenerator(
    message = 'Hello, world!',
    url = url,
)

img = amaztemp.generateTicket()
img.show()
