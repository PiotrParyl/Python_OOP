from models import Player, items
import db 
from sqlalchemy.orm import sessionmaker
import game_defs

Session = sessionmaker(bind=db.engine)
session = Session()


players_list = []







if __name__=="__main__":
    game_defs.item_menu()