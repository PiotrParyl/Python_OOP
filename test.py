import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db.engine)
session = Session()




new_player = db.player_info('elf',3,4,2,'pusto','pusto',3,2,'Fajny łuk')
session.delete()
session.commit()


for x in session.query(db.player_info).all():
    print(x.name)