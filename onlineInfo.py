import sqlite3
import time
from getInfo import get_status

con = sqlite3.connect("vk_site/db.sqlite3")

cur = con.cursor()

statuses = {}

while True:
    data = cur.execute('SELECT link, id FROM mainpage_listofusersmodel')
    for el in data:
        id = el[0][15:]
        if id[:2] == 'id':
            id = id[2:]
        statuses[str(el[1])] = get_status(current_status=statuses[str(el[1])] if str(el[1]) in statuses else False,
                                          link_id=str(el[1]), id=id)

    cur.fetchall()
    time.sleep(1)

cur.close()
