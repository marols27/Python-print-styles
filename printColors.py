"""
#DOCSTRING:
This module contains classes and predeffined objects that can help you style text in the console.

The classes are:
	- fontColor: 
		You can use this class to define font colors to use when printing in the console.

	- backgroundColor: 
		You can use this class to define background colors to use when printing in the console.


The predeffined colors are:
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
"""

# # CLASSES:
class fontColor:
	"""
	# DOCSTRING:
	You can use this class to define font colors to use when printing in the console.

	FIELDS:
	- color: 
		The color code for the font.

	METHODS:
	- testPrintColor(string: str) -> None:
		Prints the given string in the defined color.
	
	OVERRODE METHODS:
	- __str__() -> str:
		Returns the color code.
	"""
	def __init__(self, r: int, g: int, b: int) -> None:
		self.color = f"\033[38;2;{r};{g};{b}m"

	def testPrintColor(self, string: str) -> None:
		print(self.color + string + "\033[0m")

	def __str__(self) -> str:
		return self.color
	
	if __name__ == "__main__":
		pass

	#def __add__(self, other):
	#	return self.color + other.color


class backgroundColor:
	"""
	# DOCSTRING:
	You can use this class to define background colors to use when printing in the console.

	FIELDS:
	- color: 
		The color code for the background.

	METHODS:
	- testPrintColor(string: str) -> None:
		Prints the given string in the defined color.
	
	OVERRODE METHODS:
	- __str__() -> str:
		Returns the color code.
	"""
	def __init__(self, r: int, g: int, b: int) -> None:
		self.color = f"\033[48;2;{r};{g};{b}m"

	def testPrintColor(self, string: str) -> None:
		print(self.color + string + "\033[0m")

	def __str__(self) -> str:
		return self.color
	
	if __name__ == "__main__":
		pass

	#def __add__(self, other) -> str:
	#	return self.color + other.color


#class colorStyle: # ?????????
#	def __init__(self, style):
#		self.style = f"\033[{style}m"
#
#	def testPrintStyle(self, string):
#		print(self.style + string + "\033[0m")

def setTerminalStyle(fontColor: fontColor, backgroundColor: backgroundColor) -> None:
	"""
	# DOCSTRING:
	Sets the font color to the given RGB values.

	PARAMETERS:
	- fontColor: fontColor
		The font color to set.
	- backgroundColor: backgroundColor
		The background color to set.

	RETURNS:
	- The color code.
	"""
	print(fontColor.color + backgroundColor.color, end='')


# # PREDEFINED COLORS:
# # FONT COLORS:
DEFAULT_FONT = fontColor(255, 255, 255)
WHITE_FONT = fontColor(255, 255, 255)
LIGHT_WHITE_FONT = fontColor(200, 200, 200)
BLACK_FONT = fontColor(0, 0, 0)
LIGHT_BLACK_FONT = fontColor(50, 50, 50)
RED_FONT = fontColor(255, 0, 0)
LIGHT_RED_FONT = fontColor(200, 0, 0)
GREEN_FONT = fontColor(0, 255, 0)
LIGHT_GREEN_FONT = fontColor(0, 200, 0)
YELLOW_FONT = fontColor(255, 255, 0)
LIGHT_YELLOW_FONT = fontColor(200, 200, 0)
BLUE_FONT = fontColor(0, 0, 255)
LIGHT_BLUE_FONT = fontColor(0, 0, 200)
MAGENTA_FONT = fontColor(255, 0, 255)
LIGHT_MAGENTA_FONT = fontColor(200, 0, 200)
CYAN_FONT = fontColor(0, 255, 255)
LIGHT_CYAN_FONT = fontColor(0, 200, 200)

# # BACKGROUND COLORS:
DEFAULT_BACKGROUND = backgroundColor(0, 0, 0)
WHITE_BACKGROUND = backgroundColor(255, 255, 255)
LIGHT_WHITE_BACKGROUND = backgroundColor(200, 200, 200)
BLACK_BACKGROUND = backgroundColor(0, 0, 0)
LIGHT_BLACK_BACKGROUND = backgroundColor(50, 50, 50)
RED_BACKGROUND = backgroundColor(255, 0, 0)
LIGHT_RED_BACKGROUND = backgroundColor(200, 0, 0)
GREEN_BACKGROUND = backgroundColor(0, 255, 0)
LIGHT_GREEN_BACKGROUND = backgroundColor(0, 200, 0)
YELLOW_BACKGROUND = backgroundColor(255, 255, 0)
LIGHT_YELLOW_BACKGROUND = backgroundColor(200, 200, 0)
BLUE_BACKGROUND = backgroundColor(0, 0, 255)
LIGHT_BLUE_BACKGROUND = backgroundColor(0, 0, 200)
MAGENTA_BACKGROUND = backgroundColor(255, 0, 255)
LIGHT_MAGENTA_BACKGROUND = backgroundColor(200, 0, 200)
CYAN_BACKGROUND = backgroundColor(0, 255, 255)
LIGHT_CYAN_BACKGROUND = backgroundColor(0, 200, 200)

if __name__ == "__main__":
	pass