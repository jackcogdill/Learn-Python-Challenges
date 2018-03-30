from mobs import *
from util import *
from game import game
import commands

prologue = '''Example Game.
Type 'help' for a list of commands.
Type 'quit' to end the game.'''

# Run this code before the game starts
def setup():
    print(prologue)
    name = input('Enter your name: ')
    x, y = game.start
    game.player = Player(x, y, name)
    print()

# This function is called every loop of the game
def update():
    x, y = game.player.coords
    tile = game.grid[y][x]
    title = tile.title.upper()
    print(title)
    print('-' * len(title))
    if not tile.visited: # Print description if first time visiting
        tile.visited = True
        print(tile.desc)

# Parse commands
def parse(prompt='> '): # Can change this prompt from default by using: parse('my_prompt')
    text = input(prompt).strip().lower() # Remove whitespace, lowercase
    if not text:
        return # No input

    words = text.split() # Split by whitespace
    command = words[0]
    args = words[1:]

    try:
        return commands.parse(command, args)
    except InvalidCommandException as e:
        print(e)
        return False

# Main loop
if __name__ == '__main__':
    setup()
    update() # Run once before looping
    while True:
        success = parse()
        print()
        if success: # Only update if parsing succeeded
            update()

