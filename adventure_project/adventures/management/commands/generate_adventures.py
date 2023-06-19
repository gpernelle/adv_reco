from django.core.management.base import BaseCommand
from adventures.models import Adventure
from faker import Faker
from faker.providers import BaseProvider
import random


# Our custom provider inherits from the BaseProvider
class CategoryProvider(BaseProvider):
    def adventure_category(self):
        categories = [
            "Mountain Climbing",
            "White-Water Rafting",
            "Desert Exploration",
            "Deep Sea Diving",
            "Hot Air Ballooning",
            "Forest Hiking",
            "Underwater Exploration",
            "Jungle Trekking",
            "Ancient Ruins Exploration",
            "Tundra Exploration"
        ]

        # Return a random category
        return random.choice(categories)


# Our custom provider inherits from the BaseProvider
class AdventureProvider(BaseProvider):
    def location_coordinates(self, city):
        # Generate random coordinates within a reasonable range for latitude and longitude
        random.seed(hash(city))
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        return latitude, longitude


    def adventure_description(self, category):
        # Map each category to a list of descriptions
        descriptions = {
            "Mountain Climbing": [
                "Embark on a thrilling climb to the peak of the highest mountain.",
                "Experience the challenge and reward of mountain climbing.",
                "Navigate rocky terrain and reach new heights with this mountain climbing adventure."
            ],
            "White-Water Rafting": [
                "Feel the rush of white-water rafting in fast flowing rivers.",
                "Navigate through thrilling rapids in this white-water rafting adventure.",
                "Experience the exhilaration of battling the river's currents."
            ],
            "Desert Exploration": [
                "Explore the stunning beauty and vast expanses of the desert.",
                "Experience the unique ecosystem and tranquil solitude of desert exploration.",
                "Navigate sandy dunes and discover desert flora and fauna in this adventure."
            ],
            "Deep Sea Diving": [
                "Immerse yourself in the underwater world, exploring the beauty of the deep sea.",
                "Dive beneath the waves and encounter unique marine life.",
                "Experience the serenity of the underwater world in this deep sea diving adventure."
            ],
            "Hot Air Ballooning": [
                "Soar through the sky and enjoy breathtaking views in this hot air ballooning adventure.",
                "Experience the thrill of floating high above the ground and witness the panoramic beauty.",
                "Embark on a serene journey above the clouds in a hot air balloon."
            ],
            "Forest Hiking": [
                "Journey through the tranquil forest and breathe in the fresh air.",
                "Experience the serene beauty of the forest as you hike through its trails.",
                "Embark on a relaxing hike and connect with nature in this forest adventure."
            ],
            "Underwater Exploration": [
                "Dive deep beneath the waves and witness the colorful world of coral reefs.",
                "Experience the mesmerizing beauty of underwater life.",
                "Uncover the hidden secrets of the sea in this underwater exploration adventure."
            ],
            "Jungle Trekking": [
                "Navigate through the lush greenery and exotic wildlife of the jungle.",
                "Experience the thrilling adventure of trekking in the heart of the jungle.",
                "Embark on an exciting trek through the dense jungle and discover its secrets."
            ],
            "Ancient Ruins Exploration": [
                "Uncover the secrets of the past in this ancient ruins exploration adventure.",
                "Experience the thrill of discovering hidden treasures in the ancient ruins.",
                "Step into the past and learn about ancient civilizations in this exploration adventure."
            ],
            "Tundra Exploration": [
                "Venture into the freezing tundra and witness the beauty of the icy wilderness.",
                "Experience the serene solitude of the tundra in this exploration adventure.",
                "Embark on a chilly journey and discover the unique ecosystem of the tundra."
            ]
        }

        # Return a random description for the given category
        return random.choice(descriptions[category])


# Add the CategoryProvider to our faker object
faker = Faker()
faker.add_provider(CategoryProvider)
faker.add_provider(AdventureProvider)


class Command(BaseCommand):
    help = 'Generate random adventures'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of adventures to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for _ in range(total):
            category = faker.adventure_category()
            location = faker.city()
            latitude, longitude = faker.location_coordinates(location)
            Adventure.objects.create(name=f"{category} in {location}",
                                     description=faker.adventure_description(category),
                                     category=category,
                                     location=location,
                                     latitude=latitude,
                                     longitude=longitude,
                                     kids=random.getrandbits(1),
                                     adrenalin=random.randint(0, 10),
                                     promoted=random.getrandbits(1)
                                     )

        self.stdout.write(self.style.SUCCESS(f'{total} adventures were created successfully.'))
