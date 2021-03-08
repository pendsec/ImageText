import time

from MySQLdb import _mysql

while True:
    try:
        db = _mysql.connect(host="db", user="root", passwd="imagetext", db="imagetext_prod")
        break
    except BaseException:
        time.sleep(1)
        continue
