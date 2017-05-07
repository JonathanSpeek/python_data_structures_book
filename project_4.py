# The German mathematician Gottfried Leibniz developed the following method
# to approximate the value of π:
# π/4 = 1 – 1/3 + 1/5 – 1/7 + ...
# Write a program that allows the user to specify the number of iterations used in
# this approximation and displays the resulting value.

iterations = int(input('How many iterations of the pi approximation would you like to use: '))


def estimate_pi(terms):
    result = 0.0
    sign = 1.0
    for n in range(terms):
        result += sign / (2.0 * n + 1.0)
        sign = -sign
    pi_est = 4 * result
    print('The approximation of pi is {pi_est}'.format(pi_est=pi_est))

estimate_pi(iterations)
