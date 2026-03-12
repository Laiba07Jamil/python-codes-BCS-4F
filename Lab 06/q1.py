import random

def fun(x):
  return (-x**2 + 6*x)

max_x = 6
min_x = 0

x = random.randint(min_x , max_x)
print("Initial value of x:" , x)
print("f(x): ",fun(x))

while True:

    current_value = fun(x)

    left = x - 1
    right = x + 1

    left_value = float('-inf')
    right_value = float('-inf')

    if left >= min_x:
        left_value = fun(left)

    if right <= max_x:
        right_value = fun(right)

    if left_value > current_value:
        x = left
        print("Move to x =", x, "f(x) =", fun(x))

    elif right_value > current_value:
        x = right
        print("Move to x =", x, "f(x) =", fun(x))

    else:
        print("No better neighbour exists")
        print("Final optimal x =", x)
        print("Final f(x) =", fun(x))
        break