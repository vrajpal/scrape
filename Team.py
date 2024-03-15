class Team:

    def __init__(self, franchise_name, location) -> None:
        self.franchise_name = franchise_name
        self.location = location

    def print_team(self):
        print(self.location + " " + self.franchise_name)
        
