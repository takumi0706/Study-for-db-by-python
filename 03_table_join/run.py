import sqlite3
import datetime
import pandas as pd

def main():
    # sqlite3.connect()でDBファイルを読み込むOR新規作成
    con = sqlite3.connect("data.db")
    # con.cursor()でカーソルを取得
    cur = con.cursor()

    make_table(cur, con)
    join_table(con)

    cur.execute("DROP TABLE user_table")
    cur.execute("DROP TABLE item_table")
    cur.execute("DROP TABLE buy_table")

    con.commit()
    con.close()

def sql_result(sql_text, con):
    print(f"「{sql_text}」")
    # pd.read_sql_query()でSQLの結果をDataFrameに変換
    df = pd.read_sql_query(sql_text, con)

    # 結果を表示
    if column_flg:
        print(df.columns)
    print(df)

def make_table(cur, con):
    print("-----------------------------")
    print("user_table")

    cur.execute("""
                CREATE TABLE IF NOT EXISTS user_table(
                user_id INTEGER PRIMARY KEY,
                user_name TEXT UNIQUE NOT NULL)
                """)

    users_list = [(0,"Ichiro"),(1,"Jiro"),(2,"Saburo"),(3,"Shiro")]
    cur.executemany(f"INSERT INTO user_table VALUES(?,?)", users_list)
    sql_result("SELECT FROM user_tabel", con)

    print("-----------------------------")
    print("item_table")

    cur.execute("""
                CREATE TABLE IF NOT EXISTS item_table(
                item_id INTEGER PRIMARY KEY,
                item_name TEXT UNIQUE NOT NULL,
                item_price INTEGER CHECK( item_price >= 0),
                description TEXT DEFAULT 'No description'
                )
                """)

    items_list = [(0,"apple",100,"Delicious"),
                  (1,"banana",80,"Sweet"),
                  (2,"orange",120,"Juicy")]

    for id, name, price, description in items_list:
        if not description:
            cur.execute(f"""
                        INSERT INTO item_table(item_id, item_name, item_price)
                        VALUES({id},'{name}',{price})
                        """)
        else:
            cur.execute(f"""
                        INSERT INTO item_table(item_id, item_name, item_price, description)
                        VALUES ({id},'{name}',{price},'{description}')
                        """)
        sql_result("SELECT * FROM item_table", con)

    print("-----------------------------")
    print("buy_table")

    cur.execute("""
                CREATE TABEL buy_table(
                buy_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                item_id INTEGER,
                Created_time TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES user_table(user_id),
                FOREIGN KEY(item_id) REFERENCES item_table(item_id)
                )
                """)

    buy_list = [(0,0,1,str(datetime.datetime.now())),
                (1,1,2,str(datetime.datetime.now())),
                (2,1,1,str(datetime.datetime.now())),
                (3,5,1,str(datetime.datetime.now()))]

    cur.executemay(f"INSERT INTO buy_table VALUES (?,?,?,?)", buy_list)
    sql_result("SELECT * FROM buy_table", con)

def join_table(con):
    print("-----------------------------")
    print("(INNER) JOIN table")

    sql_result = """
                SELECT *
                FROM buy_table
                JOIN user_table
                ON buy_table.user_id = user_table.user_id
                """

    sql_result(sql_text, con)

    print("-----------------------------")
    print("LEFT (OUTER) JOIN table")

    sql_text = """
    SELECT *
    FROM buy_table
    LEFT JOIN user_table
    ON buy_table.user_id = user_table.user_id
    """

    sql_result(sql_text, con)

    print("-----------------------------")
    print("RIGHT (OUTER) JOIN table")

    sql_text = """
    SELECT * 
    FROM buy_table
    RIGHT JOIN user_table
    ON buy_table.user_id = user_table.user_id
    """
    sql_result(sql_text, con)

    print("-----------------------------")
    print("FULL (OUTER) JOIN table")

    sql_text = """
    SELECT *
    FROM buy_table
    FULL JOIN user_table
    ON buy_table.user_id = user_table.user_id
    """
    sql_result(sql_text, con)

if __name__ == "__main__":
    main()
