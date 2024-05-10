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

def sql_result(sql_text,cpm):
    # 引数のsql_textを表示
    print(f"「{sql_text}」")
    # pd.read_sql_query()でSQLの結果をDataFrameに変換
    df = pd.read_sql_query(sql_text, con)
    # 結果を表示
    print(df)

# make_table()関数の作成
def make_table(cur,con):
    #SQLテキストのCREATE TABLEでテーブルを作成
    cur.execute("CREATE TABLE students(id, japanese, english,math,year)")

    # データ追加
    # pd.read_csv()でCSVファイルを読み込み
    students_df = pd.read_csv("students.csv")
    # to_sql()でDataFrameをテーブルに追加(if_exists="append"で存在する場合は追加)
    students_df.to_sql("students", con, )
    # sql_result()関数を実行(引数はSELECT * FROM studentsでstudentsテーブルの全データを持ってくる。)
    sql_result("SELECT * FROM students", con)

    # cur.execute()でテーブルを削除
    cur.exexute("DROP TABLE students")

# if __name__ == "__main__"でmain()関数を実行
if __name__ == "__main__":
    main()