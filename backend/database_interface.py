from sqlite3 import Error
from uuid import uuid4
import sqlite3
from typing import Union

DATABASE_FILE_PATH = "data/schoowl.db"


class DatabaseException(Exception):
    pass


class DB:
    _instance = None

    def __init__(self) -> None:
        if DB._instance != None:
            return DB._instance

        # create database
        try:
            self.connection = sqlite3.connect(DATABASE_FILE_PATH)
            self.cursor = self.connection.cursor()
            DB._instance = self
            # create tables

            self.cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS users (
                        id integer PRIMARY KEY,
                        username text NOT NULL,
                        passwordhash text NOT NULL
                    )
                """
            )

            self.connection.commit()

        except Error as e:
            print(e)

    def insert_user(self, username, passwordhash) -> Union[True, False]:
        
        pass
        
if __name__ == "__main__":
    pass
