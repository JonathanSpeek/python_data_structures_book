# A standard science experiment is to drop a ball and see how high it bounces.
# Once the “bounciness” of the ball has been determined, the ratio gives a
# bounciness index. For example, if a ball dropped from a height of 10 feet bounces 6
# feet high, the index is 0.6 and the total distance traveled by the ball is 16 feet after
# one bounce. If the ball were to continue bouncing, the distance after two bounces
# would be 10 ft + 6 ft + 6 ft + 3.6 ft = 25.6 ft. Note that distance traveled for each
# successive bounce is the distance to the floor plus 0.6 of that distance as the ball
# comes back up. Write a program that lets the user enter the initial height of the
# ball and the number of times the ball is allowed to continue bouncing. Output
# should be the total distance traveled by the ball.

drop_height = int(input('What height did you drop the ball: '))
number_bounces = int(input('How many times is the ball allowed to continue bouncing: '))

# giving it a bounciness index of 0.6 as it was not specified in instructions...


def bounce(height):
    return round(height * 0.6, 2)


def distance(height, bounces):
    total = height
    last_height = 0
    for _bounce in range(bounces):
        height = bounce(height)
        last_height = height
        total += height * 2
    total_distance = round(total - last_height, 2)
    print('The total distance travelled by the ball is {td}ft.'.format(td=total_distance))

distance(drop_height, number_bounces)
