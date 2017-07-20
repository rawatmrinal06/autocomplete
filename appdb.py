import MySQLdb
import constants


def __get_connection():
    # Open database connection
    try:
        db = MySQLdb.connect(constants.IP, constants.USERNAME, constants.PASSWORD, constants.DATABASE)
        return db
    except MySQLdb.MySQLError:
        print("Can't connect to mysql server")


def __close_connection(db):
    # Disconnect from mysql server
    if db:
        db.close()


def _get_items(sql):
    db = __get_connection()
    di = []
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        if results:
            for row in results:
                d = {}
                for idx, field in enumerate([i[0] for i in cursor.description]):
                    d.update({field: row[idx]})
                di.append(d)
            return di
    except MySQLdb.Error:
        print "Error: unable to fetch data"
    finally:
        __close_connection(db)


def get_title_by_partial_keyword(keyword):
    sql = "SELECT {0} FROM {1} where {2} like '%{3}%'".format(constants.FIELD_NAME, constants.TABLE_NAME,
                                                                constants.FIELD_NAME, keyword)
    titles = _get_items(sql)
    if titles:
        return [title.get('title') for title in titles]
    else:
        return []
