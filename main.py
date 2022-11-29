# main.py
import package
import os, random, glob

# Picture data
_url = "https://www.google.fr/"
_ticket_id = 10
_picture_path = random.choice(glob.glob("ressources/football/*.png"))

# Create self informations    
informations = package.TicketGenerator(
    id = _ticket_id,
    url = _url,
    price = 89.00,
    picture = _picture_path,
    title = "UEFA Euro 2024",
    subtitle = "FINALE",
    date = "23/08/2024 21:00:00",
    wallet = "0xC841962098B5592A415493992cd7F521347632f7",
    location = "Stade de France, Paris",
    seat = "10D",
)

# Generate ticket image
img = informations.generate_picture()

# Generate ticket json data
json_data = informations.generate_json()

# Display ticket image
# img.show()

# Save ticket image
img.save("generated_tickets/picture/football_" + str(_ticket_id) + ".png","PNG")

# Save ticket json
with open("generated_tickets/json/football_" + str(_ticket_id) + ".json", 'w') as outfile:
    outfile.write(json_data)