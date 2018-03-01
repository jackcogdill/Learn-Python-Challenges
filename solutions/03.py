# Challenge:
# Print a diamond based on the user's input. The number should specify the height of the top half. It should work for any number.
# E.g., if the user inputs 2, it should print:  If the user inputs 3, it should print:
#   *                                              *
#  ***                                            ***
#   *                                            *****
#                                                 ***
#                                                  *
# Good luck! (^_^)
# Note: Do not print anything inside `input()`; the way the check script checks your output, it must only output the diamond.

n = int(input())

stars = 1
spaces = n - 1
for i in range(n):
    print(' ' * spaces + '*' * stars)
    stars += 2
    spaces -= 1

stars -= 4
spaces += 2
for i in range(n - 1):
    print(' ' * spaces + '*' * stars)
    stars -= 2
    spaces += 1

