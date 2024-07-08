class Position:
    
    def __init__(self):
        self.POSITION_MAP = {
            "P": 1,
            "C": 2,
            "1B": 3,
            "2B": 4,
            "3B": 5,
            "SS": 6,
            "LF": 7,
            "CF": 8,
            "RF": 9
            }



    def convert_position_to_num(self, position):
        if position != None:
            return self.POSITION_MAP[position]
