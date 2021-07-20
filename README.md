# ColourMixFinder
This tool finds the closest (pairwise) mix from the colours you own to a target colour. To use this, you just need to write a list of available hex codes in the array called 'my_colors', and change 'target_color' to the color you want to obtain. After you run this code, you will get the two best colors to mix, and the proportion (with a maximum dilution of 1/6) of each.

## Usage

The variables you might want to change are:
- ``my_colors``: Here you need to specify the colors you want. You can specify the hex code of the color (eg. '#6c592f'), or the name of the colour if you have the right csv file for that brand (Citadel Colour CSV file is provided, so you can use those). Keep in mind that if you use the name instead of the code the result will show the name too, which might be more convenient.
- ``target_color``: This is the color you want to obtain. Again, you can use either a name or a hex code.
- ``max_colors``: The maximum number of colors you want to be tested in a single mix. For example, with the default value 3, you will get the bext that requires 3 or less paints.
- ``max_divisions``: This specifies the granularity of the mixes. The default (6) should be fine as far as you don't want max_colors to be >= 6.
