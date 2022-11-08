# main.py
import package
import os, random, glob

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
picture_path = random.choice(glob.glob("ressources/football/*.png"))
print(picture_path)

amaztemp = package.TicketGenerator(
    message = 'Hello, world!',
    url = url,
    title = "Uefa euro 2024",
    subtitle = "Finale",
    date = "23/08/2022 21:00:00",
    picture = picture_path,
)

img = amaztemp.generateTicket()
img.show()

# img.save("ressources/TEST.png","PNG")
# new_image.show()