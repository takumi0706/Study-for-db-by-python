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

    