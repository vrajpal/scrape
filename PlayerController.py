class PlayerController:

    def __init__(self, session) -> None:
        self.session = session
        print("Player Controller")
    
    def db_insert(self, player):
        with self.session as session:
            if player != None:
                session.add(player)
                session.commit()
    
    def create_player(self, player):
        self.db_insert(player)
        print(player.__tablename__)