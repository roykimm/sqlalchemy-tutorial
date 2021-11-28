from main import User, Session, engine

users = [
    {
        "username": "roy",
        "email": "roy@gmail.com"
    },
    {
        "username": "daldog",
        "email": "daldog@gmail.com"
    },
    {
        "username": "ej",
        "email": "ej@gmail.com"
    },
    {
        "username": "ej2",
        "email": "ej2@gmail.com"
    }

]

local_session = Session(bind=engine)

# new_user = User(username="roykimm", email="roykimm@gmail.com")


# local_session.add(new_user)
# local_session.commit()

for x in users:
    new_user = User(username=x["username"], email=x["email"])
    local_session.add(new_user)
    local_session.commit()

    print(f"added {x['username']}")
