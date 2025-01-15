# MIT License
# 
# Copyright (c) 2025 Martin Repvik Olsbø
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
#DOCSTRING:
Version: 1.1
Author: Martin Repvik Olsbø
Date: 2024-08-03
This powerfull module contains classes and predeffined objects that can help you style text in the console.

The classes are:
- fontColor: 
	You can use this class to define font colors to use when printing in the console.

- backgroundColor: 
	You can use this class to define background colors to use when printing in the console.

- fontStyle:
	You can use this class to define a font style to use when printing in the console.

		
The functions are:
- setTerminalStyle(fontStyle: str = None, fontColor: fontColor = None, backgroundColor: backgroundColor = None) -> None:
	Set the font style, font color and background color to use when printing in the console.
	The none values will not be changed.
	If the fontStyle specified is RESET_ALL or "\033[0m", and the fontColor and backgroundColor are None, the terminal will be reset to default.
"""

# # DEFAULTS:
RESET_ALL = "\033[0m"

# # CLASSES:
class fontColor:
	"""
	# DOCSTRING:
	You can use this class to define font colors to use when printing in the console.

	CONSTANTS:
	- RESET_ALL
		Resets all styles to default. (superior to the DEFAULT one)
	- DEFAULT:
		The default color.
	- WHITE:
		The color white.
	- LIGHT_WHITE:
		A lighter shade of white.
	- BLACK:
		The color black.
	- LIGHT_BLACK:
		A lighter shade of black.
	- RED:
		The color red.
	- LIGHT_RED:
		A lighter shade of red.
	- GREEN:
		The color green.
	- LIGHT_GREEN:
		A lighter shade of green.
	- YELLOW:
		The color yellow.
	- LIGHT_YELLOW:
		A lighter shade of yellow.
	- BLUE:
		The color blue.
	- LIGHT_BLUE:
		A lighter shade of blue.
	- MAGENTA:
		The color magenta.
	- LIGHT_MAGENTA:
		A lighter shade of magenta.
	- CYAN:
		The color cyan.
	- LIGHT_CYAN:
		A lighter shade of cyan.

	FIELDS:
	- color: 
		The color code for the font.

	METHODS:
	- testPrintColor(string: str) -> None:
		Prints the given string in the defined color.
	
	OVERRODE METHODS:
	- __str__() -> str:
		Returns the color code.
	
	# EXAMPLE:
	```
	red = fontColor(255, 0, 0)
	red.testPrintColor("This text is red!")
	print(red + "This text is also red!")
	print(fontColor(0, 0, 255) + "this one is blue!")
	print(fontColor.MAGENTA + "And this one is magenta!" + fontColor.DEFAULT) # This will reset the font color to default.
	print("But this is normal!")
	```
	"""
	DEFAULT = f"\033[38;2;{204};{204};{204}m"
	RESET_ALL = RESET_ALL
	WHITE = f"\033[38;2;{200};{200};{200}m"
	LIGHT_WHITE = f"\033[38;2;{255};{255};{255}m"
	BLACK = f"\033[38;2;{0};{0};{0}m"
	LIGHT_BLACK = f"\033[38;2;{50};{50};{50}m"
	RED = f"\033[38;2;{255};{0};{0}m"
	LIGHT_RED = f"\033[38;2;{200};{0};{0}m"
	GREEN = f"\033[38;2;{0};{255};{0}m"
	LIGHT_GREEN = f"\033[38;2;{0};{200};{0}m"
	YELLOW = f"\033[38;2;{255};{255};{0}m"
	LIGHT_YELLOW = f"\033[38;2;{200};{200};{0}m"
	BLUE = f"\033[38;2;{0};{0};{255}m"
	LIGHT_BLUE = f"\033[38;2;{0};{0};{200}m"
	MAGENTA = f"\033[38;2;{255};{0};{255}m"
	LIGHT_MAGENTA = f"\033[38;2;{200};{0};{200}m"
	CYAN = f"\033[38;2;{0};{255};{255}m"
	LIGHT_CYAN = f"\033[38;2;{0};{200};{200}m"
	
	def __init__(self, r: int, g: int, b: int) -> None:
		self.color = f"\033[38;2;{r};{g};{b}m"

	def testPrintColor(self, string: str) -> None:
		print(self.color + string + RESET_ALL)

	def __str__(self) -> str:
		return self.color

	def __add__(self, other):
		if isinstance(other, str):
			return self.color + other
		elif isinstance(other, fontColor):
			return self.color + other.color
		else:
			return NotImplemented
		
	def __radd__(self, other):
		if isinstance(other, str):
			return other + self.color
		else:
			return NotImplemented
	
	if __name__ == "__main__":
		pass



class backgroundColor:
	"""
	# DOCSTRING:
	You can use this class to define background colors to use when printing in the console.

	CONSTANTS:
	- RESET_ALL
		Resets all styles to default. (superior to the DEFAULT one)
	- DEFAULT:
		The default color.
	- WHITE:
		The color white.
	- LIGHT_WHITE:
		A lighter shade of white.
	- BLACK:
		The color black.
	- LIGHT_BLACK:
		A lighter shade of black.
	- RED:
		The color red.
	- LIGHT_RED:
		A lighter shade of red.
	- GREEN:
		The color green.
	- LIGHT_GREEN:
		A lighter shade of green.
	- YELLOW:
		The color yellow.
	- LIGHT_YELLOW:
		A lighter shade of yellow.
	- BLUE:
		The color blue.
	- LIGHT_BLUE:
		A lighter shade of blue.
	- MAGENTA:
		The color magenta.
	- LIGHT_MAGENTA:
		A lighter shade of magenta.
	- CYAN:
		The color cyan.
	- LIGHT_CYAN:
		A lighter shade of cyan.

	FIELDS:
	- color: 
		The color code for the background.

	METHODS:
	- testPrintColor(string: str) -> None:
		Prints the given string in the defined color.
	
	OVERRODE METHODS:
	- __str__() -> str:
		Returns the color code.

	# EXAMPLE:
	```
	red = backgroundColor(255, 0, 0)
	red.testPrintColor("This text has a red background!")
	print(red + "This text also has a red background!" + backgroundColor.DEFAULT) # This will reset the background color to default, for some reason i could not figure out it had to be here aswell as on the next one.
	print(backgroundColor(0, 0, 255) + "This one has a blue one!" + backgroundColor.DEFAULT)
	print(backgroundColor.MAGENTA + "And this one is magenta!" + backgroundColor.DEFAULT)
	print("But this is not!")
	```
	"""
	
	RESET_ALL = RESET_ALL
	DEFAULT = f"\033[48;2;{12};{12};{12}m"
	WHITE = f"\033[48;2;{200};{200};{200}m"
	LIGHT_WHITE = f"\033[48;2;{255};{255};{255}m"
	BLACK = f"\033[48;2;{0};{0};{0}m"
	LIGHT_BLACK = f"\033[48;2;{50};{50};{50}m"
	RED = f"\033[48;2;{255};{0};{0}m"
	LIGHT_RED = f"\033[48;2;{200};{0};{0}m"
	GREEN = f"\033[48;2;{0};{255};{0}m"
	LIGHT_GREEN = f"\033[48;2;{0};{200};{0}m"
	YELLOW = f"\033[48;2;{255};{255};{0}m"
	LIGHT_YELLOW = f"\033[48;2;{200};{200};{0}m"
	BLUE = f"\033[48;2;{0};{0};{255}m"
	LIGHT_BLUE = f"\033[48;2;{0};{0};{200}m"
	MAGENTA = f"\033[48;2;{255};{0};{255}m"
	LIGHT_MAGENTA = f"\033[48;2;{200};{0};{200}m"
	CYAN = f"\033[48;2;{0};{255};{255}m"
	LIGHT_CYAN = f"\033[48;2;{0};{200};{200}m"

	def __init__(self, r: int, g: int, b: int) -> None:
		self.color = f"\033[48;2;{r};{g};{b}m"

	def testPrintColor(self, string: str) -> None:
		print(self.color + string + RESET_ALL)

	def __str__(self) -> str:
		return self.color

	def __add__(self, other) -> str:
		if isinstance(other, str):
			return self.color + other
		elif isinstance(other, backgroundColor):
			return self.color + other.color
		else:
			return NotImplemented
		
	def __radd__(self, other):
		if isinstance(other, str):
			return other + self.color
		else:
			return NotImplemented
	
	if __name__ == "__main__":
		pass



class fontStyles:
	"""
	# DOCSTRING:
	You can use this class to define font styles to use when printing in the console.
	
	NOTE:\n
	Not all styles are supported by all terminals\n
	and some styles may not work as intended.\n
	I did not test all styles on all terminals, so you may have to test it yourself.

	CONSTANTS:
	- BRIGT:
		Font is brigter.
	- DIM:
		Font is dim.
	- UNDERLINED:
		Font is underlined.
	- BLINK:
		Font is blinking.
	- REVERSE:
		Font is reversed.
	- HIDDEN:
		Font is hidden.
	- STRIKE_THROUGH:
		Font has a strike through.
	- DOUBLE_UNDERLINED:
		Font is double underlined.

	# EXAMPLE:
	```
	styler = fontStyle()
	print(styler.UNDERLINED + "This text has an underline!" + RESET_ALL)
	```
	"""

	BRIGT = "\033[1m"
	DIM = "\033[2m"
	UNDERLINED = "\033[4m"
	BLINK = "\033[5m"
	REVERSE = "\033[7m"
	HIDDEN = "\033[8m"
	STRIKE_THROUGH = "\033[9m"
	DOUBLE_UNDERLINED = "\033[21m"

	def __init__(self) -> None:
		pass
	
	if __name__ == "__main__":
		pass


# # FUNCTIONS:
def setTerminalStyle(fontStyle: str = None, fontColor: fontColor = None, backgroundColor: backgroundColor = None) -> None:
	"""
	# DOCSTRING:
	Sets the font color to the given RGB values.

	PARAMETERS:
	- fontStyle: str = None:
		The font style to use.
	- fontColor: fontColor = None:
		The font color to use.
	- backgroundColor: backgroundColor = None:
		The background color to use.

	# EXAMPLE:
	```
	red = fontColor(255, 0, 0)
	blue = backgroundColor(0, 0, 255)
	redStyle = colorStyle(red, blue)
	setTerminalStyle(redStyle)
	print("This text is red and has a blue background! And is bad for your eyes!")
	```
	"""
	if fontStyle is None:
		fontStyle = ""
	if fontColor is None:
		fontColor = ""
	if backgroundColor is None:
		backgroundColor = ""
	print(fontStyle + "" if fontColor == None else fontColor.color + "" if backgroundColor == None else backgroundColor.color, end='')

def resetTerminalStyle() -> None:
	"""
	# DOCSTRING:
	Resets the terminal style to default.
	"""
	print(RESET_ALL)



if __name__ == "__main__":
	pass
