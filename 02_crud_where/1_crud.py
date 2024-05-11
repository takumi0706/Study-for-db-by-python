import sqlite3
import pandas as pd

def main():
    # sqlite3.connect()でDBファイルを読み込む
    con = sqlite3.connect("data.db")
    # con.cursor()でカーソルを取得
    cur = con.cursor()

    # make_table()関数を実行
    make_table(cur, con)
    # crud()関数を実行
    crud(cur, con)

    # DROP TABLEでテーブルを削除
    cur.execute("DROP TABLE students")
    # con.commit()でコミット
    con.commit()
    # con.close()でDBとの接続を閉じる
    con.close()

def sql_result(sql_text, con):
    # 引数のsql_textを表示
    print(f"「{sql_text}」")
    # pd.read_sql_query()でSQLの結果をDataFrameに変換
    df = pd.read_sql_query(sql_text, con)
    # 結果を表示
    print(df)

# make_table()関数の作成
def make_table(cur, con):
    #SQLテキストのCREATE TABLEでテーブルを作成
    cur.execute("CREATE TABLE IF NOT EXISTS students(id, japanese, english, math, year)")

    # データ追加
    # pd.read_csv()でCSVファイルを読み込み
    students_df = pd.read_csv("../01_python_sqlite/students.csv")
    # to_sql()でDataFrameをテーブルに追加(if_exists="append"で存在する場合は追加)
    students_df.to_sql("students", con, if_exists = "append", index = None)
    # sql_result()関数を実行(引数はSELECT * FROM studentsでstudentsテーブルの全データを持ってくる。)
    sql_result("SELECT * FROM students", con)


# crud()関数の作成
def crud(cur,con):
    print("-----------------------------")
    print("CREATE")
    print(f"「INSERT INTO students VALUES(10, 75, 75, 75,'M2')」")

    # INSERT INTOでデータを追加
    cur.execute(f"INSERT INTO students VALUES(10, 75, 75, 75, 'M2')")

    print("-----------------------------")
    print("READ")
    sql_result("SELECT * FROM students",con)

    print("-----------------------------")
    print("UPDATE")
    print("「UPDATE students SET japanese = 90 WHERE id =1」")
    cur.execute("UPDATE students SET japanese = 90 WHERE id = 1")

    print("-----------------------------")
    print("DELETE")
    print("「DELETE FROM students WHERE id = 3」")
    cur.execute("DELETE FROM students WHERE id = 3")

    print("-----------------------------")
    sql_result("SELECT * FROM students ",con)

# if __name__ == "__main__"でmain()関数を実行
if __name__ == "__main__":
    main()