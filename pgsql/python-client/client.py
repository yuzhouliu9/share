import psycopg2
import time
import multiprocessing

def single_conn(id):
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="suppliers",
        user="postgres",
        password="abc123")

    print('Database connection established, id: ' + str(id))

    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)

    time.sleep(10)
    conn.close
    print('Database connection closed')

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    ans = pool.map(single_conn, range(0,5))
    pool.close()
