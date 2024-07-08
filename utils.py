positions = {
    "C":  2,
    "1B": 3,
    "2B": 4, 
    "SS": 6,
    "3B": 5,
    "LF": 7,
    "CF": 8,
    "RF": 9,
    "DH": 10,
    "UT": 11,
    "OF": 12
}

def convertPositionToEnum(position):
    if position: 
        cleaned_position = position.upper()
        if cleaned_position in positions:
            return positions[cleaned_position]
    else: 
        return 0

