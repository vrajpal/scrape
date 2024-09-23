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

# the headers for the batting table in Baseball Ref, remove player as its method for grabbing name is inconsistent 
batting = {"age", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", 
           "CS", "BB", "SO", "batting_avg", "onbase_perc", "slugging_perc", "onbase_plus_slugging", 
           "onbase_plus_slugging_plus", "TB", "GIDP", "HBP", "SH", "SF", "IBB"}



def convertPositionToEnum(position):
    if position: 
        cleaned_position = position.upper()
        if cleaned_position in positions:
            return positions[cleaned_position]
    else: 
        return 0

