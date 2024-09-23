class PlayerController:

    def __init__(self, session) -> None:
        self.session = session
        print("Player Controller")
    
    def db_insert(self, player):
        print(player)
        
        try:
            if player is not None:
                print("in if")
                print(self.session)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"Error occurred: {e}")
    
    def create_player(self, player):
        breakpoint()
        self.session.add(player)
        self.db_insert(player)
        print(player.__tablename__)
