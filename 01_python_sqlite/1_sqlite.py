import sqlite3
import pandas as pd

def main():

    # sqlite3.connect()でDBファイルを読み込むor新規作成
    con = sqlite3.connect("data.db")
    # con.cursor()でカーソルを取得
    cur = con.cursor()

    # sql_execute()関数を実行
    sql_execute(cur, con)
    # con.commit()でコミット
    con.commit()
    # con.close()でDBとの接続を閉じる
    con.close()

# ここにSQL文が書かれている（大文字がSQL文小文字は変数名）
def sql_execute(cur, con):
    # executeメソッドでSQL文を実行できる
    # CREATE TABLE（テーブルを作成）
    cur.execute("CREATE TABLE students(id, japanese, english, math)")
    # studentsの表にデータを追加
    cur.execute("INSERT INTO students VALUES(0,50,30,20)")
    print("SELECT * FROM stundets")
    # conの中にあるstudentsを取得しデータフレーム変換
    df = pd.read_sql_query("SELECT * FROM students",con)
    print(df)
    # studentsのテーブルを削除
    cur.execute("DROP TABLE students")

if __name__ == "__main__":
    main()