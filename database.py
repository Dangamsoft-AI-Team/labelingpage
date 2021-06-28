import pymysql


def banji_conn():
    conn = pymysql.connect(
        host='dev.thegam.io',
        user='banji',
        port=13306,
        password='dangam2021@!',
        db='banji',
        charset='utf8mb4'
    )
    return conn

conn = banji_conn()
# cr = conn.cursor()
# sql_sentence = """
# SELECT * FROM Labeling_image;
# """
# cr.execute(sql_sentence)
# rows = cr.fetchall()
# print(rows)

