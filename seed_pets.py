"""Seed file to make sample data for db."""

from models import db, Pet

# Create all tables
db.drop_all()
db.create_all()

PETS = [
    {
        "name": "Fluffy",
        "species": "cat",
        "photo_url": "https://images.ctfassets.net/m5ehn3s5t7ec/wp-image-199550/944c1fee6902ea18636ef182f6d3d599/Fluffy_Siberian_Cat.jpeg",
        "age": 3,
        "notes": "Likes to nap in the sun.",
        "available": True
    },
    {
        "name": "Buddy",
        "species": "dog",
        "photo_url": "https://www.thesprucepets.com/thmb/tcGA_jeqWkO1dU4rw69G3a3pWAw=/2121x0/filters:no_upscale():strip_icc()/GettyImages-926877064-29386c59fee1414a809043123091eb72.jpg",
        "age": 5,
        "notes": "Very friendly and loves to play fetch.",
        "available": True
    },
    {
        "name": "Nibbles",
        "species": "cat",
        "photo_url": "https://images.unsplash.com/photo-1529778873920-4da4926a72c2?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHx8MA%3D%3D",
        "age": 1,
        "notes": "Enjoys running on the wheel.",
        "available": False
    },
    {
        "name": "Spike",
        "species": "dog",
        "photo_url": "https://media-be.chewy.com/wp-content/uploads/2021/06/02102805/Doberman-Pinscher_Featured-Image.jpg",
        "age": 2,
        "notes": "Loves mealworm treats.",
    },
    {
        "name": "Snowball",
        "species": "rabbit",
        "photo_url": "https://cdn.shopify.com/s/files/1/0040/8997/0777/files/Cute_Bunny_7d_1024x1024.jpg?v=1698453869",
        "age": 4,
        "notes": "Enjoys hopping around the garden.",
    },
     {
        "name": "Whiskers",
        "species": "cat",
        "age": 2,
        "notes": "Loves chasing laser pointers.",
        "available": False
    },
    {
        "name": "Rocky",
        "species": "dog",
        "photo_url": "https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_square.jpg",
        "age": 4,
        "notes": "Enjoys long walks and belly rubs.",
    },
    {
        "name": "Gizmo",
        "species": "parrot",
        "photo_url": "https://i.natgeofe.com/n/e3ae5fbf-ddc9-4b18-8c75-81d2daf962c1/3948225.jpg",
        "age": 8,
        "notes": "Can mimic human speech.",
        "available": False
    },
    {
        "name": "Speedy",
        "species": "tortoise",
        "photo_url": "https://vetmed.illinois.edu/wp-content/uploads/2022/01/rftortoise.jpg",
        "age": 10,
        "notes": "Enjoys basking in the sun.",
    },
    {
        "name": "Nemo",
        "species": "goldfish",
        "photo_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSssSnpyk97f3enpZLh6NzCM2_WI6NB0rDe76e9FQLSPw&s",
        "age": 1,
        "notes": "Lives in a spacious aquarium.",
    }
]

for pet_data in PETS:
    pet = Pet(**pet_data)
    db.session.add(pet)

db.session.commit()

