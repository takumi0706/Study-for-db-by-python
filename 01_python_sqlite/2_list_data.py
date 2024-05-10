import sqlite3
import pandas as pd

def main():
    #ファイル読み込み
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    #SQL命令関数
    sql_execute(cur,con)

    #SQLを実行しファイルにアクセス
    con.commit()
    #ファイルをクローズ
    con.close()

#     SQLの中身をデータフレームとして表示させる関数
def sql_result(sql_text,con):
    # SQL文表示
    print(f"「{sql_text}」")
#     データフレーム変換
    df = pd.read_sql_query(sql_text,con)
    print(df)
#     この関数にSQL文を書き込み
def sql_execute(cur, con):
    # TABLE作成SQL命令文
    cur.execute("CREATE TABLE students(id, japanese,english,math)")

    # データ追加SQL命令文
    #先にデータのリストを作成
    students_list = [(0, 50, 30, 20), (1, 30, 40, 60), (2, 60, 70, 20)]
    #テーブルにデータリストの追加
    cur.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students_list)
    # データの追加
    sql_result("SELECT * FROM students", con)
    # テーブル削除
    cur.execute("DROP TABLE students")

if __name__ == "__main__":
    main()