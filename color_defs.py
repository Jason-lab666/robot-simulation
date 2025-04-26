#Color_defs.py
#Color constants
COLOR_YELLOW = 1
COLOR_CYAN = 2
COLOR_GREEN = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_WHITE = 6

COLOR_NAME_MAP = {
    COLOR_YELLOW: 'Yellow',
    COLOR_CYAN: 'Cyan',
    COLOR_GREEN: 'Green',
    COLOR_BLUE: 'Blue',
    COLOR_MAGENTA: 'Magenta',
    COLOR_WHITE: 'White'
}

COLOR_CHAR_MAP = {
    COLOR_YELLOW: 'Y',
    COLOR_CYAN: 'C',
    COLOR_GREEN: 'G',
    COLOR_BLUE: 'B',
    COLOR_MAGENTA: 'M',
    COLOR_WHITE: 'W'
}

def get_color_name(code):
    return COLOR_NAME_MAP.get(code, 'Unknown')

def get_color_char(code):
    return COLOR_CHAR_MAP.get(code, '?')

COLOR_MAP = {
    'name': COLOR_NAME_MAP,
    'char': COLOR_CHAR_MAP
}