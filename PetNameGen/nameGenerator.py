import tkinter as tk
from tkinter import ttk, messagebox
import random


# Expanded NameDatabase class stores pet names categorized by type, gender, and themes
class NameDatabase:
    def __init__(self):
        # Significantly expanded database of names categorized by type and gender
        self.names = {
            'dog': {
                'male': ['Max', 'Buddy', 'Charlie', 'Rocky', 'Jake', 'Toby', 'Duke', 'Bear', 'Cooper', 'Zeus',
                         'Finn', 'Murphy', 'Apollo', 'Dexter', 'Sam', 'Buster', 'Rusty', 'Rex', 'Diesel', 'Thor',
                         'Ace', 'Bruno', 'Chase', 'Jackson', 'Gunner', 'Maverick', 'Harley', 'Baxter', 'Bentley',
                         'Beau', 'Jax', 'Ranger', 'Simba', 'Ollie', 'Milo', 'Riley', 'Scout', 'Louie', 'Frankie',
                         'Winston', 'Samson', 'Ozzy', 'Rocco', 'Hank', 'King', 'Tank', 'Archie', 'Ziggy', 'Boomer',
                         'Blue', 'Bruce', 'Brody', 'Shadow', 'Griffin'],
                'female': ['Bella', 'Lucy', 'Daisy', 'Molly', 'Lola', 'Sadie', 'Zoe', 'Rosie', 'Maggie', 'Ruby',
                           'Nala', 'Ginger', 'Harley', 'Sasha', 'Chloe', 'Stella', 'Roxy', 'Lulu', 'Gracie', 'Pepper',
                           'Penny', 'Dixie', 'Coco', 'Ellie', 'Maya', 'Millie', 'Winnie', 'Honey', 'Sophie', 'Bailey',
                           'Olive', 'Hazel', 'Piper', 'Izzy', 'Annie', 'Kona', 'Dolly', 'Phoebe', 'Lexi', 'Zelda',
                           'Lilly', 'Willow', 'Ella', 'Nova', 'Trixie', 'Raven', 'Maddie', 'Sassy', 'Princess',
                           'Sugar', 'Bonnie', 'Lady'],
                'gender-neutral': ['Bailey', 'Riley', 'Coco', 'Shadow', 'Scout', 'Bandit', 'Blue', 'Lucky',
                                   'Marley', 'Dakota', 'Teddy', 'Whiskey', 'Sunny', 'Nova', 'Smokey', 'Echo',
                                   'Storm', 'Sandy', 'Pepper', 'Raven', 'Frost', 'River', 'Sage', 'Aspen', 'Sky',
                                   'Blaze', 'Ash', 'Sunny', 'Harley', 'Parker', 'Jinx', 'Fido', 'Oakley', 'Moose',
                                   'Hopper', 'Biscuit', 'Spot', 'Dusty', 'Radar', 'Clover', 'Freckles', 'Mocha',
                                   'Mittens', 'Snowball', 'Snickers', 'Cinnamon', 'Twilight', 'Tiger', 'Indie']
            },
            'cat': {
                'male': ['Oliver', 'Leo', 'Milo', 'Simba', 'Jasper', 'Felix', 'Oscar', 'George', 'Jack', 'Sam',
                         'Toby', 'Harry', 'Max', 'Finn', 'Benny', 'Gizmo', 'Louie', 'Salem', 'Tiger', 'Shadow',
                         'Theo', 'Sebastian', 'Archie', 'Jinx', 'Zeus', 'Thor', 'Rufus', 'Rocky', 'Ziggy',
                         'Apollo', 'Tom', 'Bandit', 'Buster', 'Casper', 'Tigger', 'Freddie', 'Hunter', 'Charlie',
                         'Simba', 'Maverick', 'Romeo', 'Chester', 'Winston', 'Oreo', 'Merlin', 'Whiskers', 'Rusty',
                         'Elvis', 'Figaro', 'Smokey', 'Clyde', 'Sunny', 'Fluffy'],
                'female': ['Luna', 'Chloe', 'Lily', 'Sophie', 'Cleo', 'Nala', 'Misty', 'Zara', 'Ruby', 'Daisy',
                           'Mimi', 'Sassy', 'Trixie', 'Poppy', 'Willow', 'Pepper', 'Olive', 'Hazel', 'Molly', 'Juno',
                           'Mittens', 'Pearl', 'Rosie', 'Zoe', 'Fluffy', 'Ella', 'Fiona', 'Nina', 'Honey', 'Dolly',
                           'Lacey', 'Tinkerbell', 'Penny', 'Duchess', 'Muffin', 'Snowball', 'Whiskers', 'Princess',
                           'Kiki', 'Angel', 'Sasha', 'Lulu', 'Baby', 'Storm', 'Jasmine', 'Phoebe', 'Sweetie',
                           'Lady', 'Sugar', 'Bella', 'Cupcake'],
                'gender-neutral': ['Smokey', 'Shadow', 'Oreo', 'Charlie', 'Tigger', 'Whiskers', 'Midnight', 'Ash',
                                   'Stormy', 'Blue', 'Phoenix', 'Fuzz', 'Dusty', 'Kit', 'Patches', 'Buttons',
                                   'Teddy', 'Cloud', 'Marble', 'Pumpkin', 'Tiger', 'Muffin', 'Pepper', 'Sunny',
                                   'Chester', 'Boo', 'Jinx', 'Misty', 'Snowy', 'Sky', 'Fuzzy', 'Misty', 'Mochi',
                                   'Storm', 'Socks', 'Tiger', 'Snickers', 'Taco', 'Cinder', 'Mango', 'Spot',
                                   'Zorro', 'Cloudy', 'Ziggy', 'Silver', 'Twinkle', 'Thunder', 'Onyx', 'Spooky']
            },
            'bird': {
                'male': ['Kiwi', 'Buddy', 'Skye', 'Chico', 'Rio', 'Jazz', 'Ozzy', 'Rocky', 'Pico', 'Sunny',
                         'Cody', 'Sammy', 'Chirpy', 'Buzz', 'Zephyr', 'Axel', 'Cosmo', 'Flick', 'Gizmo', 'Cloud',
                         'Harvey', 'Benny', 'Charlie', 'Dexter', 'Echo', 'Finn', 'Gizmo', 'Harley', 'Indy', 'Joey',
                         'Kenny', 'Lenny', 'Milo', 'Nico', 'Paco', 'Rico', 'Scout', 'Turbo', 'Vinnie', 'Willie',
                         'Zazu', 'Pip', 'Rocket', 'Fritz', 'Skipper', 'Dobby', 'Flame', 'Zippy', 'Ringo', 'Koko',
                         'Sky'],
                'female': ['Tweety', 'Sunny', 'Angel', 'Peach', 'Lola', 'Cleo', 'Bella', 'Daisy', 'Sky', 'Rosie',
                           'Penny', 'Ruby', 'Lulu', 'Blossom', 'Honey', 'Jewel', 'Mango', 'Piper', 'Fluffy', 'Coco',
                           'Olive', 'Feather', 'Saffron', 'Kiara', 'Bonnie', 'Juno', 'Violet', 'Clementine', 'Sandy',
                           'Cricket', 'Ivy', 'Pearl', 'Polly', 'Rainbow', 'Tiki', 'Hazel', 'Peanut', 'Princess',
                           'Sugar', 'Snowflake', 'Stella', 'Pumpkin', 'Skittles', 'Lily', 'Misty', 'Serena',
                           'Autumn', 'Peaches', 'Nina', 'Sophie', 'Ember'],
                'gender-neutral': ['Rio', 'Sky', 'Sunny', 'Coco', 'Flame', 'Cloud', 'Echo', 'Jazz', 'Chirp',
                                   'Tweetie', 'Ziggy', 'Blaze', 'Feather', 'Skittles', 'Zephyr', 'Twinkle',
                                   'Blue', 'Phoenix', 'Storm', 'Aspen', 'Skyler', 'Buttercup', 'Sandy', 'Pip',
                                   'Sparrow', 'Cloudy', 'Rusty', 'Stormy', 'Shadow', 'Bubbles', 'Snowy', 'Mango',
                                   'Banjo', 'Jet', 'Cinnamon', 'Nibbles', 'Freckles', 'Coco', 'Rocket', 'Sunny',
                                   'Sprinkles', 'Tango', 'Popcorn', 'Pebble', 'Indigo', 'Echo', 'Wings', 'Gizmo']
            }
        }

        # Additional expanded database of names categorized by theme
        self.themed_names = {
            'nature': ['Willow', 'River', 'Sky', 'Leaf', 'Luna', 'Storm', 'Rain', 'Aspen', 'Dawn', 'Blaze',
                       'Ocean', 'Maple', 'Cedar', 'Forrest', 'Coral', 'Sierra', 'Breeze', 'Fern', 'Ivy', 'Flame',
                       'Meadow', 'Sunny', 'Pine', 'Dew', 'Shadow', 'Rose', 'Breeze', 'Brook', 'Sage', 'Fern',
                       'Lake', 'Violet', 'Birch', 'Boulder', 'Daisy', 'Fawn', 'Flora', 'Juniper', 'Moss', 'Pebble',
                       'Ember', 'Autumn', 'Frost', 'Ivy', 'Petal', 'Sunny', 'Thorn', 'Zephyr', 'Clover', 'Sequoia',
                       'Poppy', 'Star', 'Tiger', 'Fern', 'Echo'],
            'mythology': ['Zeus', 'Athena', 'Thor', 'Loki', 'Apollo', 'Hera', 'Hermes', 'Freya', 'Hades',
                          'Artemis', 'Persephone', 'Ares', 'Odin', 'Poseidon', 'Hercules', 'Juno', 'Anubis',
                          'Isis', 'Ra', 'Sif', 'Atlas', 'Demeter', 'Eros', 'Fenrir', 'Gaia', 'Helios', 'Janus',
                          'Medusa', 'Nike', 'Nyx', 'Orion', 'Selene', 'Venus', 'Vulcan', 'Hermes', 'Dionysus',
                          'Triton', 'Hebe', 'Juno', 'Achilles', 'Circe', 'Bacchus', 'Tyr', 'Heimdall', 'Fenrir',
                          'Balder', 'Ceres', 'Cerberus', 'Chiron', 'Phoenix'],
            'food': ['Cookie', 'Peanut', 'Muffin', 'Pumpkin', 'Pepper', 'Oreo', 'Sugar', 'Mocha', 'Pickles',
                     'Brownie', 'Cinnamon', 'Nacho', 'Cupcake', 'Biscuit', 'Nutmeg', 'Mango', 'Honey',
                     'Waffles', 'Cocoa', 'Jellybean', 'Marshmallow', 'Taco', 'Peaches', 'Pudding', 'Cheddar',
                     'Ginger', 'Maple', 'Toffee', 'Popcorn', 'S’mores', 'Lemon', 'Brie', 'Basil', 'Coconut',
                     'Butterscotch', 'Blueberry', 'Raisin', 'Chili', 'Churro', 'Caramel', 'Apple', 'Dumpling',
                     'Tuna', 'Mint', 'Sushi', 'Toffee', 'Vanilla', 'Cheese', 'Spice', 'Pretzel', 'Crumbs'],
            'space': ['Nova', 'Comet', 'Orbit', 'Star', 'Nebula', 'Galaxy', 'Astro', 'Luna', 'Mars',
                      'Venus', 'Jupiter', 'Mercury', 'Stellar', 'Apollo', 'Rocket', 'Cosmo', 'Meteor',
                      'Zodiac', 'Aurora', 'Orion', 'Andromeda', 'Pluto', 'Stardust', 'Quasar', 'Nebula',
                      'Sirius', 'Polaris', 'Titan', 'Europa', 'Sol', 'Io', 'Halley', 'Vega', 'Pulsar',
                      'Celeste', 'Ganymede', 'Cassiopeia', 'Draco', 'Scorpius', 'Rigel', 'Phoenix', 'Equinox',
                      'Eclipse', 'Hyperion', 'Nebula', 'Triton', 'Atlas', 'Aries', 'Orbit', 'Phaeton',
                      'Asteroid Destroyer']
        }

    def get_names_by_type_and_gender(self, pet_type, gender):
        """Returns names filtered by pet type and gender"""
        return self.names.get(pet_type, {}).get(gender, [])

    def get_names_by_theme(self, theme):
        """Returns names filtered by theme"""
        return self.themed_names.get(theme, [])

    def get_random_name(self, pet_type=None, gender=None, theme=None):
        """Returns a random name filtered by pet type, gender, and theme if provided"""
        names = []

        # Filter by theme if provided (themes ignore gender)
        if theme:
            names = self.get_names_by_theme(theme)

        # If no theme, filter by pet type and gender
        elif pet_type and gender:
            names = self.get_names_by_type_and_gender(pet_type, gender)
        elif pet_type:
            names = sum(self.get_names_by_type(pet_type).values(), [])
        else:
            # If no filters provided, get all names
            names = sum([sum(gender_names.values(), []) for gender_names in self.names.values()], [])

        return random.choice(names) if names else None


# NameGenerator class handles the name generation logic
class NameGenerator:
    def __init__(self, name_database):
        self.name_database = name_database

    def generate_name(self, pet_type=None, gender=None, theme=None):
        """Generates a random name with optional filters for pet type, gender, and theme"""
        return self.name_database.get_random_name(pet_type, gender, theme)


# Main GUI Application using tkinter
class PetNameGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Name Generator")

        # Set a fun background color
        self.root.configure(bg="#f0f9ff")

        # Initialize the database and generator
        self.name_db = NameDatabase()  # NameDatabase with sample names
        self.name_gen = NameGenerator(self.name_db)  # NameGenerator to generate names

        # Labels for the dropdowns
        ttk.Label(root, text="Pet Type:", background="#f0f9ff").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(root, text="Gender:", background="#f0f9ff").grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(root, text="Theme:", background="#f0f9ff").grid(row=3, column=0, padx=10, pady=10)

        # Dropdowns for Pet Type, Gender, and Theme
        self.pet_type = tk.StringVar()
        self.gender = tk.StringVar()
        self.theme = tk.StringVar()

        self.pet_type_combo = ttk.Combobox(root, textvariable=self.pet_type)
        self.pet_type_combo['values'] = ['dog', 'cat', 'bird', 'Any']
        self.pet_type_combo.grid(row=1, column=1, padx=10, pady=10)
        self.pet_type_combo.current(0)

        self.gender_combo = ttk.Combobox(root, textvariable=self.gender)
        self.gender_combo['values'] = ['male', 'female', 'gender-neutral', 'Any']
        self.gender_combo.grid(row=2, column=1, padx=10, pady=10)
        self.gender_combo.current(0)

        self.theme_combo = ttk.Combobox(root, textvariable=self.theme)
        self.theme_combo['values'] = ['nature', 'mythology', 'food', 'space', 'None']
        self.theme_combo.grid(row=3, column=1, padx=10, pady=10)
        self.theme_combo.current(4)  # Set default to 'None'

        # Generate button with a fun style
        self.generate_button = ttk.Button(root, text="Generate Name", command=self.generate_name, style="Fun.TButton")
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Label for displaying the generated name with custom font
        self.result_label = ttk.Label(root, text="", font=("Comic Sans MS", 16), background="#f0f9ff",
                                      foreground="#ff4500")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Create a style for the button to make it more fun
        style = ttk.Style()
        style.configure("Fun.TButton", font=("Comic Sans MS", 14), foreground="#000", background="#ffdab9")


    def generate_name(self):
        """Handles generating and displaying a random pet name"""
        pet_type = self.pet_type.get().lower() if self.pet_type.get() != 'Any' else None
        gender = self.gender.get().lower() if self.gender.get() != 'Any' else None
        theme = self.theme.get().lower() if self.theme.get() != 'None' else None

        # Generate the name based on the selected filters
        random_name = self.name_gen.generate_name(pet_type, gender, theme)

        if random_name:
            self.result_label.config(text=f"Generated Pet Name: {random_name}")
        else:
            messagebox.showerror("Error", "No names available for the selected filters")


# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PetNameGeneratorApp(root)
    root.mainloop()
