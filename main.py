# main.py
import package

url = "https://google.fr"

amaztemp = package.TicketGenerator(
    message = 'Hello, world!',
    url = url,
    title = "This is the title",
    subtitle = "This is the subtitle",
)

img = amaztemp.generateTicket()
img.show()

# # new_image.save("images/merged_image.jpg","PNG")
# new_image.show()