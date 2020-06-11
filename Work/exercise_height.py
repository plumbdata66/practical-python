#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:39:09 2020

@author: playstation
"""

bill_thickness = 0.11 * 0.001 # in meters
sears_height = 442 # height in meters
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills *= 2

print("Number of days: ", day)
print("Number of bills: ", num_bills)
print("Final height: ", num_bills * bill_thickness)

