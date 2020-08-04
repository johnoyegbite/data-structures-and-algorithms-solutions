# SOLVED!

def convert_to_hex(color):
    """Assumes color is in the range 0 to 255
    Returns the hexadecimal notation
    """
    color_code = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                  7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D',
                  14: 'E', 15: 'F'}
    result = ''
    if color < 16:
        return '0' + color_code[color]
    while color != 0:
        rem = color % 16
        color = color // 16
        result = color_code[rem] + result

    return result


def convert_rgb_to_hex(r, g, b):
    """Assumes r, g and b are in the range 0 to 255
    Returns the hexadecimal notation
    """
    r_hex = convert_to_hex(r)
    g_hex = convert_to_hex(g)
    b_hex = convert_to_hex(b)
    return f'#{r_hex}{g_hex}{b_hex}'


def serialize(hexa):
    valid = []
    for c in hexa:
        if c.isdigit() or c.isalpha():
            valid.append(c)
    return ''.join(valid)
    
def convert_hex_to_rgb(hexa):
    """Assumes hexa is in the form #BF40B4"""
    color_code = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    hexa = serialize(hexa)
    rgb = []
    print(hexa)
    if len(hexa) >= 6:
        j = 0
        s = 0
        for i, c in enumerate(hexa):
            if j == 6:
                break
            if j % 2 == 0:
                s = color_code[c]*16
            else:
                s += color_code[c]
                rgb.append(str(s))
                s = 0
            j += 1
    elif len(hexa) >= 3 and len(hexa) <= 6:
        for i, c in enumerate(hexa):
            if i == 3:
                break
            s = color_code[c]*16
            s += color_code[c]
            rgb.append(str(s))

    return "rgb(" + ", ".join(rgb) + ")"


if __name__ == "__main__":
    r, g, b = 254, 108, 123
    r, g, b = 30, 30, 30
    r, g, b = 70, 70, 70
    r, g, b = 32, 30, 30
    r, g, b = 255, 53, 53
    r, g, b = 191, 64, 180
    # r, g, b = 255, 213, 175
    r, g, b = 255, 172, 54
    r, g, b = 253, 140, 36
    print(convert_rgb_to_hex(r, g, b))
    # print(convert_hex_to_rgb("#BEDFE0"))
