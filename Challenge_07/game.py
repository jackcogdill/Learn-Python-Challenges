class Tile:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.visited = False

# Map of tiles
T = {
    'forest': Tile('Dark Forest', 'Eerie howls echo from the shadows. You bravely walk into the forest.'),
    'meadow': Tile('Central Meadow',
        'Slowly peeking open your eyelids, you awaken to find yourself in the middle of a green field. The moon shines directly above you.'),
}

# Use to store game variables
class game:
    # Storing as [y][x]
    grid = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,T['meadow'],T['forest'],0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    start = (2, 2)

