print('This is triangle <a>')
def triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

height = int(input("Enter the height of the triangle: "))
triangle(height)



print('This is triangle <b>')
def left_triangle(heightb):
    for i in range(1, heightb + 1):
        print(' ' *(heightb - i) + '*' * i)

heightb = int(input("Enter the height of the triangle: "))
left_triangle(heightb)


print('This is triangle <c>')

def down_pyramid(heightc):
    for i in range(heightc, 0, -1):
        print(' ' * (heightc - i) + '*' * (2 * i - 1))

heightc = int(input("Enter the height of the triangle: "))
down_pyramid(heightc)



print('This is triangle <d>')

def pyramid(heightd):
    for i in range(heightd):
        print(' ' * (heightd - i - 1) + '*' * (2 * i + 1))

heightd = int(input("Enter the height of the triangle: "))
pyramid(heightd)


print('This is triangle <e>')


def two_pyramids(heighte):
    for i in range(heighte, 0, -1):
        print(' ' * (heighte - i), end='')
        print('*' * (2 * i - 1))

    for i in range(2, heighte + 1):
        print(' ' * (heighte - i), end='')
        print('*' * (2 * i - 1))

heighte = int(input("Enter the height of the triangle: "))
two_pyramids(heighte)



print('This is triangle <f>')

def sideways_pyramids(heightf):
    for i in range(1, heightf + 1):
        print('*' * i, end='')
        print(' ' * (2 * (heightf - i)), end='')
        print('*' * i)
    
    for i in range(heightf - 1, 0, -1):
        print('*' * i, end='')
        print(' ' * (2 * (heightf - i)), end='')
        print('*' * i)

heightf = int(input("Enter the height of the triangle: "))
sideways_pyramids(heightf)




print('This is triangle <g>')

def sideway_pyramid_left(heightg):
    for i in range(1, heightg + 1):
        print('*' * i)
    
    for i in range(heightg - 1, 0, -1):
        print('*' * i)

heightg = int(input("Enter the height of the triangle: "))
sideway_pyramid_left(heightg)




print('This is triangle <h>')

def sideway_pyramid_right(heighth):
    for i in range(1, heighth + 1):
        print(' ' * (heighth - i), end='')
        print('*' * i)
    
    for i in range(heighth - 1, 0, -1):
        print(' ' * (heighth - i), end='')
        print('*' * i)

heighth = int(input("Enter the height of the triangle: "))
sideway_pyramid_right(heighth)





print('This is triangle <i>')
def down_triangle(heighti):
    for i in range(heighti, 0, -1):
        print('*' * i)

heighti = int(input("Enter the height of the triangle: "))
down_triangle(heighti)





print('This is triangle <j>')
def last_triangle(heightj):
    for i in range(1, heightj + 1):
        print(' ' *(heightj - i) + '*' * i)

heightj = int(input("Enter the height of the triangle: "))
last_triangle(heightj)



