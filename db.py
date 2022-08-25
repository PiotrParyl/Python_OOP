from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#connect wieth data base 
engine = create_engine('sqlite:///sqlalchemy.sglite', echo=True)    
#mange tabeles

base = declarative_base()

class player_info (base):

    __tablename__ = 'Player_table'

    player_id = Column(Integer, primary_key=True)
    name = Column(String)
    str = Column(Integer)
    mgp = Column(Integer)
    gold = Column(Integer)
    items = Column(String)
    friends = Column(String)
    hp = Column(Integer)
    fate = Column(Integer)
    abilities = Column(String)

    def __init__(self,name,str,mgp,gold,items,friends,hp,fate,abilities):
        self.name = name
        self.str = str
        self.mgp = mgp
        self.gold = gold
        self.items = items
        self.friends = friends
        self.hp = hp
        self.fate = fate
        self.abilities = abilities
    
base.metadata.create_all(engine)

    
