import json
import os


adjectives = [
    "Mysterious", "Purple", "Sunny", "Electric", "Midnight", "Frosty",
    "Crimson", "Silver", "Ocean", "Golden", "Azure", "Lucky", "Emerald",
    "Velvet", "Neon", "Fuzzy", "Whispering", "Dancing", "Galactic",
    "Wild", "Stealthy", "Moonlit", "Rapid", "Enchanted", "Electric",
    "Dreamy", "Shooting", "Crimson", "Silver", "Jade", "Aqua", "Mystic",
    "Cosmic", "Amber", "Whimsical", "Ruby", "Night", "Sapphire", "Fading",
    "Dusk", "Hidden", "Misty", "Burning", "Obsidian", "Starlight",
    "Silent", "Galaxy", "Velvet", "Lunar", "Jovial", "Marble", "Aquamarine",
    "Copper", "Moonlit", "Whispering", "Scarlet", "Silver", "Crimson",
    "Jade", "Sapphire", "Flickering", "Dancing", "Neon", "Electric", "Golden",
    "Lively", "Amber", "Whimsical", "Ruby", "Nighttime", "Sapphire", "Frosty",
    "Daring", "Hidden", "Misty", "Blazing", "Obsidian", "Starlit", "Silent",
    "Galactic", "Velvet", "Lunar", "Jovial", "Marble", "Aquamarine", "Copper",
    "Opalescent", "Cerulean", "Glimmering", "Enigmatic", "Violet", "Sun-kissed",
    "Dynamic", "Twinkling", "Frozen", "Gilded", "Turquoise", "Fortunate",
    "Enchanting", "Plush", "Radiant", "Zephyr", "Wandering", "Celestial",
    "Untamed", "Nimble", "Stellar", "Accelerating", "Whimsy", "Amethyst",
    "Nocturnal", "Cobalt", "Waning", "Eclipsed", "Concealed", "Phantasmal",
    "Blissful", "Sanguine", "Verdant", "Lustrous", "Flaming", "Onyx",
    "Astral", "Suspended", "Galvanized", "Vermilion", "Iridescent",
    "Cerulean", "Jubilant", "Rosy", "Moonbeam", "Ethereal", "Lively",
    "Ivory", "Luminescent", "Wistful", "Crimson", "Cadmium", "Luminous",
    "Sable", "Lavender", "Sparkling", "Emergent", "Whirling", "Silken",
    "Incandescent", "Resplendent", "Spectral", "Topaz", "Turbulent",
    "Sapphire", "Vibrant", "Dusky", "Fleeting", "Flourishing", "Molten",
    "Ornate", "Serene", "Galaxy-spanning", "Moonlit", "Fervent", "Jasper",
    "Quicksilver", "Nebulous", "Vivid", "Ephemeral", "Flickering", "Azure",
    "Halcyon", "Coppery", "Shimmering", "Lustrous", "Sapphire", "Gossamer",
    "Celestial", "Amber", "Enigmatic", "Smoldering", "Velvet", "Cosmic",
    "Cerulean", "Jubilant", "Rosy", "Moonbeam"
]

nouns = [
    "Gopher", "Tulip", "Skies", "Jaguar", "Raven", "Breeze", "Comet", "Arrow",
    "Dreamer", "Sphinx", "Wave", "Charm", "Enigma", "Dragon", "Knight", "Panda",
    "Willow", "Firefly", "Ninja", "Cheetah", "Shadow", "Mermaid", "Phoenix",
    "Oak", "Pixel", "Dusk", "Snail", "Star", "Sparrow", "Stallion", "Jester",
    "Whisper", "Lotus", "Falcon", "Wanderer", "Ripple", "Sky", "Leopard",
    "Marauder", "Whale", "Stardust", "Lioness", "Crescent", "Gazelle", "Shimmer",
    "Flame", "Dawn", "Nebula", "Embrace", "Gust", "Lynx", "Arcade", "Wisp",
    "Ripple", "Nomad", "Sky", "Fawn", "Dusk", "Hawk", "Maze", "Brook", "Oasis",
    "Sorcerer", "Swan", "Gazer", "Voyager", "Lily", "Journey", "Mystic",
    "Aura", "Charm", "Minstrel", "Wind", "Solstice", "Scepter", "Crown",
    "Jadeite", "Starlight", "Firefly", "Dolphin", "Nightingale", "Eclipse",
    "Glade", "Labyrinth", "Archer", "Sable", "Tempest", "Galaxy", "Seer",
    "Serenade", "Moonbeam", "Wraith", "Zephyr", "Coral", "Echo", "Cascade", 
    "Onyx", "Rune", "Blaze", "Lagoon", "Bison", "Evergreen", "Viper", "Twilight",
    "Tiger", "Muse", "Jade", "Rain", "Horizon", "Sapphire", "Pegasus", "Bamboo",
    "Jewel", "Whirlwind", "Willow",
    "Gazelle", "Wisp", "Quasar", "Aurora", "Frost", "Harmony", "Glimmer",
    "Heron", "Cobra", "Abyss", "Mirage", "Oracle", "Blossom", "Neptune",
    "Kestrel", "Ember", "Rhapsody", "Majesty", "Nectar", "Amber", "Mystique",
    "Wildfire", "Panther", "Brook", "Lyric", "Everest", "Fable", "Rustle",
    "Pebble", "Monarch", "Nimbus", "Lavender", "Halcyon", "Petal", "Wanderlust",
    "Glimpse", "Opal", "Inferno", "Breeze", "Reverie", "Lark", "Gazelle",
    "Eagle", "Scepter", "Wraith", "Lilac", "Celestial", "Thunder", "Silhouette",
    "Velvet", "Wanderer", "Calypso", "Vortex", "Zodiac", "Thorn", "Whisper",
    "Moonstone", "Zenith", "Voyage", "Astral", "Ethereal", "Quill", "Breeze",
    "Jasmine", "Lagoon", "Mercury", "Auburn", "Shade", "Nymph", "Frost", "Falcon",
    "Sparrow", "Cascade", "Serenity", "Raven", "Talisman", "Grove", "Stardust",
    "Jupiter", "Drizzle", "Wisp", "Zephyr", "Azalea", "Reverie", "Nebula",
    "Halcyon", "Nightingale", "Eclipse", "Sapphire", "Solace", "Cypress", "Aurelia",
    "Luminous", "Quasar", "Majestic", "Sylph", "Marigold", "Aurora", "Verdant",
    "Sage", "Amethyst", "Harmony", "Celeste", "Whirlpool", "Phantom", "Rune",
    "Sable", "Tempest", "Galaxy", "Seer", "Serenade", "Moonbeam", "Wraith",
    "Zephyr", "Coral", "Echo", "Cascade", "Onyx", "Rune", "Blaze", "Lagoon",
    "Bison", "Evergreen", "Viper", "Twilight", "Tiger", "Muse", "Jade", "Rain",
    "Horizon", "Sapphire", "Pegasus", "Bamboo", "Jewel", "Whirlwind", "Willow",
    "Gazelle", "Wisp", "Quasar", "Aurora", "Frost", "Harmony", "Glimmer",
    "Heron", "Cobra", "Abyss", "Mirage", "Oracle", "Blossom", "Neptune",
    "Kestrel", "Ember", "Rhapsody", "Majesty", "Nectar", "Amber", "Mystique",
    "Wildfire", "Panther", "Brook", "Lyric", "Everest", "Fable", "Rustle",
    "Pebble", "Monarch", "Nimbus", "Lavender", "Halcyon", "Petal", "Wanderlust",
    "Glimpse", "Opal", "Inferno", "Breeze", "Reverie", "Lark", "Gazelle",
    "Eagle", "Scepter", "Wraith", "Lilac", "Celestial", "Thunder", "Silhouette",
    "Velvet", "Wanderer", "Calypso", "Vortex", "Zodiac", "Thorn", "Whisper",
    "Moonstone", "Zenith", "Voyage", "Astral", "Ethereal", "Quill", "Breeze",
    "Jasmine", "Lagoon", "Mercury", "Auburn", "Shade", "Nymph", "Frost", "Falcon",
    "Cascade", "Serenity", "Raven", "Talisman", "Grove", "Stardust", "Jupiter",
    "Drizzle", "Wisp", "Zephyr", "Azalea", "Reverie", "Nebula", "Halcyon",
    "Nightingale", "Eclipse", "Sapphire", "Solace", "Cypress", "Aurelia",
    "Luminous", "Quasar", "Majestic", "Sylph", "Marigold", "Aurora", "Verdant",
    "Sage", "Amethyst", "Harmony", "Celeste", "Whirlpool", "Phantom", "Rune"
]

def generate_random_usernames():
    return_data = []
    for adjective in list(set(adjectives)) :
        for noun in list(set(nouns)) :
            return_data.append(f"{adjective}{noun}")
    return return_data

usernames = generate_random_usernames()
path = f'{os.path.dirname(__file__)}/usernames.json'
with open(path, 'w') as file:
    json.dump(usernames, file, indent=4)