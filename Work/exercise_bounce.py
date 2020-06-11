
#! /usr/bin/python3

'''
Bounce a ball
'''

bounce = 0
height = 100


while bounce < 10:
    height = round((height *  3/5), 2)
    bounce += 1
    print(bounce, ":", height)

