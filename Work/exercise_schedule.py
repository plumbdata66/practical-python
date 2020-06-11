#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:54:14 2020

@author: playstation
"""
import urllib.request
u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=1479&route=22")
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall(".//pt"):
    print(pt.text)
    

