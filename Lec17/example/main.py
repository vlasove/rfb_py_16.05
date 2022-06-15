from app import run
from app import server as srv
from app import database as db


if __name__ == "__main__":
    srv.run()
    db.run()
    run()