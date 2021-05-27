from app import app, db
import sys

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    db.create_all()
    app.run()