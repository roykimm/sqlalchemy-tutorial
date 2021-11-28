from main import Session, engine, User

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(
    User.username == 'roykimm').first()

user_to_update.username = "roykimmnim"
user_to_update.email = "roykimmnim@gmail.com"

local_session.commit()
