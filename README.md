# Python-print-styles
Welcome to the Python Print Style library!
This is just a simple but powerfull python library to help you color and style your font while using the console.
Using this library you can:
- Set the font style
- Set the font color
- Set the font background color

The library is as is, so unless there are any major changes that should be done, it will remain as it is.

## classes:
- fontColor:
    - Constructor: __init__(r, g, b)
    - testPrintColor(string)
        Prints a specified test string using your font color.
- backgroundColor:
    - Constructor: __init__(r, g, b)
    - testPrintColor(string)
        Prints a specified test string using your background color.

## Functions:
- setTerminalStyle(style, fontColor, backgroundColor):
    Sets the terminal style, font and background colors to the specified ones.

## Predeffined values:
- DEFAULT_FONT
- WHITE_FONT
- LIGHT_WHITE_FONT
- BLACK_FONT
- LIGHT_BLACK_FONT
- RED_FONT
- LIGHT_RED_FONT
- GREEN_FONT
- LIGHT_GREEN_FONT
- YELLOW_FONT
- LIGHT_YELLOW_FONT
- BLUE_FONT
- LIGHT_BLUE_FONT
- MAGENTA_FONT
- LIGHT_MAGENTA_FONT
- CYAN_FONT
- LIGHT_CYAN_FONT

- DEFAULT_BACKGROUND
- WHITE_BACKGROUND
- LIGHT_WHITE_BACKGROUND
- BLACK_BACKGROUND
- LIGHT_BLACK_BACKGROUND
- RED_BACKGROUND
- LIGHT_RED_BACKGROUND
- GREEN_BACKGROUND
- LIGHT_GREEN_BACKGROUND
- YELLOW_BACKGROUND
- LIGHT_YELLOW_BACKGROUND
- BLUE_BACKGROUND
- LIGHT_BLUE_BACKGROUND
- MAGENTA_BACKGROUND
- LIGHT_MAGENTA_BACKGROUND
- CYAN_BACKGROUND
- LIGHT_CYAN_BACKGROUND

- BRIGT_STYLE
- DIM_STYLE
- UNDERLINED_STYLE
- BLINK_STYLE
- REVERSE_STYLE
- HIDDEN_STYLE
- STRIKE_THROUGH_STYLE
- DOUBLE_UNDELINED_STYLE

- RESET_ALL

## How to use:
If you wish to use this library, you will have to download or copy this file, and put it in your project folder.
Then to use the package you simply import the package like any other like so:
```import printStyles```

To use any of the colors, or styles, you deffine them by using the preset values or define new colors using the colors objects.
Then to apply the colors or styles you simply just print them, or you can use the predeffined function in the library setTerminalStyle().

For example:
1. We want the console to have a cyan font with a grey background (rgb = 12, 12, 12), using the BLINK_STYLE:
```
print(BLINK_STYLE + str(CYAN_FONT) + str(backgroundColor(12, 12, 12)), end="")
```
This will set the style of your console window to the one you wanted.

2. We want to print "Hello World!" with a blue font:
```
print(str(BLUE_FONT) + "Hello World!" + RESET_ALL)
```

NOTE: RESET_ALL does not just reset the style to default, but also the font and background colors.
NOTE: If not reset or changed, the color and style in the console wil remain the same, 
      eaven after your program has exited, so if you do not want your console window to keep a red fonted, 
      blue backgrounded and blinking, remember to add the RESET_ALL to the end of your strings before exiting the program,
      or do ```print(RESET_ALL, end="")``` in stead.

## Separate Examples:
### Font styles:
To specify any font style, use the preset styles from the package.
To apply them just append them to the front of any string that you want to use them on like so:
```
style = BLINK_STYLE
yourString = "Your string"
yourStyledString = style + yourString
print(yourStyledString)
```
Here is a list of the predeffined styles:
- BRIGT_STYLE
- DIM_STYLE
- UNDERLINED_STYLE
- BLINK_STYLE
- REVERSE_STYLE
- HIDDEN_STYLE
- STRIKE_THROUGH_STYLE
- DOUBLE_UNDELINED_STYLE

### Font colors:
To specify any font color, you can do so either by using the predefined fontColors, 
or by specifying your own by using rgb values ranging from 0 to 255.
Use a predeffined font color:
```
yourFontColor = CYAN_FONT
yourString = "Your string"
yourColoredString = yourFontColor + yourString
print(yourColoredStrings)
```

Use your own deffined color using rgb values:
```
yourFontColor = fontColor(r = 45, g = 150, b = 60)
yourString = "Your string"
yourColoredString = yourFontColor + yourString
print(yourColoredString)
```

Here is a list of the predeffined fontColors
- DEFAULT_FONT
- WHITE_FONT
- LIGHT_WHITE_FONT
- BLACK_FONT
- LIGHT_BLACK_FONT
- RED_FONT
- LIGHT_RED_FONT
- GREEN_FONT
- LIGHT_GREEN_FONT
- YELLOW_FONT
- LIGHT_YELLOW_FONT
- BLUE_FONT
- LIGHT_BLUE_FONT
- MAGENTA_FONT
- LIGHT_MAGENTA_FONT
- CYAN_FONT
- LIGHT_CYAN_FONT

## Background colors:
To specify any font color, you can do so either by using the predefined fontColors, 
or by specifying your own by using rgb values ranging from 0 to 255.
Use a predeffined font color:
```
yourBackgroundColor = CYAN_BACKGROUND
yourString = "Your string"
yourColoredString = yourBackgroundColor + yourString
print(yourColoredStrings)
```

Use your own deffined color using rgb values:
```
yourBackgroundColor = backgroundColor(r = 45, g = 150, b = 60)
yourString = "Your string"
yourColoredString = yourBackgroundColor + yourString
print(yourColoredString)
```

Here is a list of the predeffined backgroundColors
- DEFAULT_BACKGROUND
- WHITE_BACKGROUND
- LIGHT_WHITE_BACKGROUND
- BLACK_BACKGROUND
- LIGHT_BLACK_BACKGROUND
- RED_BACKGROUND
- LIGHT_RED_BACKGROUND
- GREEN_BACKGROUND
- LIGHT_GREEN_BACKGROUND
- YELLOW_BACKGROUND
- LIGHT_YELLOW_BACKGROUND
- BLUE_BACKGROUND
- LIGHT_BLUE_BACKGROUND
- MAGENTA_BACKGROUND
- LIGHT_MAGENTA_BACKGROUND
- CYAN_BACKGROUND
- LIGHT_CYAN_BACKGROUND
