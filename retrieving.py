from main import User, Session, engine

local_session = Session(bind=engine)

# returns all objects
# users = local_session.query(User).all()[:3]
# for user in users:
#     print(user.username)


# query for one object
roykimm = local_session.query(User).filter(User.username == "roykimm").first()
print(roykimm)
