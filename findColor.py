from colormath.color_objects import LabColor, CMYKColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import itertools
from fractions import Fraction
from statistics import mean
from math import sqrt
import csv
colour_dict = {}
with open('CitColours.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    next(csv_reader)
    
    for row in csv_reader:
        colour_dict[row[0]] = row[2]
            
print(colour_dict)

def get_rgb_from_hex(h):
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def mix_two_cmyk_colours(c1, c2, prop1 = 1, prop2 = 1):
    tot = prop1+prop2
    prop1 /= tot
    prop2 /= tot
    return ((prop1*a + prop2*b) for a, b in zip(c1.get_value_tuple(), c2.get_value_tuple()))
def get_color_diff(c1, c2):
    c1 = convert_color(c1, LabColor)
    c2 = convert_color(c2, LabColor)
    return delta_e_cie2000(c1, c2)

def hex_to_cmyk_color(h):
    c = get_rgb_from_hex(h[1:])
    c = sRGBColor(*c)
    c = convert_color(c, CMYKColor)
    return c
my_colors = ['#ffffff', '#9b0e05', '#c00b0c', '#e21516', '#4b205c', '#18ABCC', '#789ebb', '#35998e', '#094345', '#008660', '#36a062', '#003b1d', '#257326', '#57aa2d', '#a89758', '#c6c180', '#8c5144', '#cb7953', '#dbad75', '#4e3433', '#7b7e74', '#9caeae', '#d2e4df', '#aba495', '#d6d5c4', '#010100', '#535659', '#3B5150', '#84C3AA']
target_color = hex_to_cmyk_color('#6c592f')
target_color = convert_color(target_color, LabColor)
current_best_diff = 1000000
current_best_comb = (0, 0)
current_best_ratio = (0, 0)
max_divisions = 6
for c1, c2 in itertools.combinations(my_colors, 2):
    c1cmyk = hex_to_cmyk_color(c1)
    c2cmyk = hex_to_cmyk_color(c2)
    for r in range(1, max_divisions):
        c3 = CMYKColor(*mix_two_cmyk_colours(c1cmyk, c2cmyk, r, max_divisions-r))
        diff = get_color_diff(c3, target_color)
        if diff < current_best_diff:
            current_best_diff = diff
            current_best_comb = (c1, c2)
            current_best_ratio = (r, max_divisions-r)

print(current_best_comb, Fraction(*current_best_ratio).as_integer_ratio())
