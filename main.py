# main.py
import package
import os, random, glob

# Picture data
_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
_picture_path = random.choice(glob.glob("ressources/football/*.png"))
_ticket_id = 1

# Create self informations
informations = package.TicketGenerator(
    id = _ticket_id,
    url = _url,
    price = 30.00,
    picture = _picture_path,
    title = "Uefa euro 2024",
    subtitle = "Finale",
    date = "23/08/2022 21:00:00",
    wallet = "0xC841962098B5592A415493992cd7F521347632f7",
    location = "Stade de France",
    seat = '38A',
)

# Generate ticket image
img = informations.generate_picture()

# Generate ticket json data
json_data = informations.generate_json()

# Display ticket image
# img.show()

# Save ticket image
img.save("generated_tickets/picture/" + str(_ticket_id) + ".png","PNG")

# Save ticket json
with open("generated_tickets/json/" + str(_ticket_id) + ".json", 'w') as outfile:
    outfile.write(json_data)
    
print(json_data)