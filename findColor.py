from colormath.color_objects import LabColor, CMYKColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import itertools
from fractions import Fraction
from statistics import mean
from math import sqrt, gcd
import csv
from functools import reduce


colour_dict = {}
with open('CitColours.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    next(csv_reader)
    
    for row in csv_reader:
        colour_dict[row[0]] = row[2]

def simplify(array):
    return [int(e/reduce(gcd, array)) for e in array]

def __get_proportions(max_divisions, max_colors, depth, final_proportions, previous_proportions):
    depth += 1
    current_proportion = previous_proportions + (1, )
    while sum(current_proportion) < max_divisions:
        print(current_proportion)
        added_proportion = tuple(current_proportion + ((max_divisions-sum(current_proportion)), ))
        final_proportions[depth].append(added_proportion)
        if max_colors > depth:
            __get_proportions(max_divisions, max_colors, depth, final_proportions, current_proportion)
        current_proportion = current_proportion[:-1] + ((current_proportion[-1]+1), )
        
def get_proportions(max_divisions, max_colors):
    depth = 2
    final_proportions = {i: [] for i in range(2, max_colors+1)}
    for i in range(1,max_divisions):
        final_proportions[2].append((i,max_divisions-i))
        if max_colors > depth:
            __get_proportions(max_divisions, max_colors, depth, final_proportions, (i, ))
    return final_proportions
def get_hex_from_name(c):
    return c if c[0] == '#' else colour_dict[c]
def get_rgb_from_hex(h):
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def mix_cmyk_colours(colors, prop):
    tot = sum(prop)
    prop = tuple(p/tot for p in prop)
    s = []
    for comp in zip(*(c.get_value_tuple() for c in colors)):
        s.append(0)
        for col, p in zip(comp, prop):
            s[-1] += p*col
    return s
def get_color_diff(c1, c2):
    c1 = convert_color(c1, LabColor)
    c2 = convert_color(c2, LabColor)
    return delta_e_cie2000(c1, c2)

def hex_to_cmyk_color(h):
    c = get_rgb_from_hex(h[1:])
    c = sRGBColor(*c)
    c = convert_color(c, CMYKColor)
    return c
# my_colors = ['#ffffff', '#9b0e05', '#c00b0c', '#e21516', '#4b205c', '#18ABCC', '#789ebb', '#35998e', '#094345', '#008660', '#36a062', '#003b1d', '#257326', '#57aa2d', '#a89758', '#c6c180', '#8c5144', '#cb7953', '#dbad75', '#4e3433', '#7b7e74', '#9caeae', '#d2e4df', '#aba495', '#d6d5c4', '#010100', '#535659', '#3B5150', '#84C3AA']
my_colors = ['#ffffff', 'Abaddon Black', 'Bugmans Glow', 'Caliban Green', 'Celestra Grey', 'Incubi Darkness', 'Mephiston Red', 'Rakarth Flesh', 'Rhinox Hide', 'Thousand Sons Blue', 'Zandri Dust', 'Dark Reaper', 'Cadian Fleshtone', 'Dawnstone', 'Eshin Grey', 'Evil Sunz Scarlet', 'Kabalite Green', 'Kislev Flesh', 'Moot Green', 'Pallid Wych Flesh', 'Ulthuan Grey', 'Warpstone Glow', 'Wild Rider Red', 'Dawnstone', 'Xereus Purple', 'Gauss Blaster Green']

max_divisions = 6
max_colors = 3

target_color = hex_to_cmyk_color('#f7d095')
#target_color = hex_to_cmyk_color(colour_dict['Xereus Purple'])

target_color = convert_color(target_color, LabColor)
current_best_diff = 1000000
current_best_comb = (0, 0)
current_best_ratio = (0, 0)
chosen_mix = 0

proportions = get_proportions(max_divisions, max_colors)
print(proportions)
for p in proportions.keys():
    for colors in itertools.combinations(my_colors, p):
        colorscmyk = (tuple(hex_to_cmyk_color(get_hex_from_name(c)) for c in colors))
        for r in proportions[p]:
            c3 = CMYKColor(*mix_cmyk_colours(colorscmyk, r))
            diff = get_color_diff(c3, target_color)
            if diff < current_best_diff:
                current_best_diff = diff
                current_best_comb = (colors)
                current_best_ratio = r
                chosen_mix = c3

for c1 in my_colors:
    c1cmyk = hex_to_cmyk_color(get_hex_from_name(c1))
    diff = get_color_diff(c1cmyk, target_color)
    if diff < current_best_diff:
        current_best_diff = diff
        current_best_comb = (c1)
        current_best_ratio = (1, )
#Fraction(*current_best_ratio).as_integer_ratio()
print(current_best_comb, simplify(current_best_ratio), "With diff: ", current_best_diff)
