
# This is the color tester. Running this script in whichever terminal or console
# you are running your code in will yield a large table containing all of the
# codes for the different color options of background, foreground, and style.
# If you would like to change the color, remember that the format is:

# print('\033[1;32;40m' + 'some text here' + '\033[0m')

# where the leading '\033[' dicates a new format, with style '1' and color '32',
# on a background '40'. The final '\033[0m' resets the formatting to default.
# if default background is preferred, then the above line of code would look like:

# print('\033[1;32m' + 'some text here' + '\033[0m')

# Good luck with any experimenting that you do!!

###############################################################################

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(10):              # has options 0 - 9
        for fg in range(30,38):          # only has options 30 - 37
            s1 = ''
            for bg in range(40,48):      # only has options 40 - 47
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\033[%sm %s \033[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()
