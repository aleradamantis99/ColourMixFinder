# ColourMixFinder
This tool finds the closest mix from the colours you own to a target colour. To use this, you just need to write a list of available hex codes in the list called 'my_colors', and change 'target_color' to the color you want to obtain. After you run this code, you will get the best colors to mix, and the proportion.

## Installation
Just run ``pip -r requirements.txt``, or install ``colormath`` library in some way.

## Usage

The variables you might want to change are:
- ``my_colors``: Here you need to specify the colors you want. You can specify the hex code of the color (eg. '#6c592f'), or the name of the colour if you have the right csv file for that brand (Citadel Colour CSV file is provided, so you can use those). Keep in mind that if you use the name instead of the code the result will show the name too, which might be more convenient.
- ``target_color``: This is the color you want to obtain. Again, you can use either a name or a hex code.
- ``max_colors``: The maximum number of colors you want to be tested in a single mix. For example, with the default value 3, you will get the bext that requires 3 or less paints.
- ``max_divisions``: This specifies the granularity of the mixes. The default (6) should be fine as far as you don't want max_colors to be >= 6. For 6, the proportions tested with 3 colors are: (1, 1, 4), (1, 2, 3), (1, 3, 2), (1, 4, 1), (2, 1, 3), (2, 2, 2), (2, 3, 1), (3, 1, 2), (3, 2, 1), (4, 1, 1). While if you go up to 10: (1, 1, 8), (1, 2, 7), (1, 3, 6), (1, 4, 5), (1, 5, 4), (1, 6, 3), (1, 7, 2), (1, 8, 1), (2, 1, 7), (2, 2, 6), (2, 3, 5), (2, 4, 4), (2, 5, 3), (2, 6, 2), (2, 7, 1), (3, 1, 6), (3, 2, 5), (3, 3, 4), (3, 4, 3), (3, 5, 2), (3, 6, 1), (4, 1, 5), (4, 2, 4), (4, 3, 3), (4, 4, 2), (4, 5, 1), (5, 1, 4), (5, 2, 3), (5, 3, 2), (5, 4, 1), (6, 1, 3), (6, 2, 2), (6, 3, 1), (7, 1, 2), (7, 2, 1), (8, 1, 1). This increases computing time and can lead to some hard-to-get-right proportions in real life, like (7, 2, 1)
