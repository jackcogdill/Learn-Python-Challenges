#    *
#   ***
#  *****
# *******

size = int(input())

stars = 1
spaces = size - 1
for i in range(size):
    print(' ' * spaces + '*' * stars)
    stars += 2
    spaces -= 1

