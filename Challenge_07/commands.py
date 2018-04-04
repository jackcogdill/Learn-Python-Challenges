from util import *
from game import game

def parse(command, args):
    if command in commands:
        function = commands[command]
        return function(args)
    else:
        raise InvalidCommandException('Unknown command: "%s"' % command)

def help(args):
    print('List of commands: [%s]' % ' '.join(commands.keys()))
    print('Try typing "go" with a direction (north, east, south, west).')
    return False # Don't update

def move(args):
    if not args:
        raise InvalidCommandException('No direction specified.')
    direction = args[0]

    x, y = game.player.coords
    if direction == 'north':
        y += 1
    elif direction == 'east':
        x += 1
    elif direction == 'south':
        y -= 1
    elif direction == 'west':
        x -= 1
    else:
        raise InvalidCommandException('Invalid direction.')

    inbounds = 0 <= y < len(game.grid) and 0 <= x < len(game.grid[0])
    if not inbounds or not game.grid[y][x]:
        print('The path this way is blocked.')
        return False
    else:
        game.player.coords = (x, y)
        return True

def quit(args):
    exit(0)

# Every command function must return True/False for success and
# take args, a list of strings.
commands = {
    'go': move,
    'help': help,
    'quit': quit,
}

