import sys
import logging
import psycopg2
# config.py with db info and creds
import config


def db_start():
    logging.info("Connecting to DB")
    con = None

    try:
        con = psycopg2.connect(database=config.DB_NAME,
                               user=config.DB_USER,
                               host=config.DB_HOST,
                               password=config.DB_PASS)
        return con
    except psycopg2.DatabaseError as e:

        if con:
            con.rollback()

        logging.error('Error %s' % e)
        sys.exit(1)


if __name__ == '__main__':
    logging.basicConfig(
        filename="log.log",
        level=logging.INFO,
        format='%(asctime)s [%(name)10s] [%(levelname)s] %(message)s')
    logging.info("Starting program")
    with open('game_data.sql', 'r') as f:
        q = f.read()

    con = db_start()
    cursor = con.cursor()
    cursor.execute(q)
    records = cursor.fetchall()
