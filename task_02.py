#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converting C to K tempreature"""

import decimal

ABSOLUTE_DIFFERENCE =  273.15

def fahrenheit_to_celsius(degrees):
    convert = float((degrees - 32) * 5 / 9)
    return convert


def celsius_to_kelvin(degrees):
    convertK = float(degrees + ABSOLUTE_DIFFERENCE)
    return convertK


