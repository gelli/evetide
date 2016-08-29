import database


def main():
    session = database.session()
    for feed in session.query(database.Feed):
        print feed
