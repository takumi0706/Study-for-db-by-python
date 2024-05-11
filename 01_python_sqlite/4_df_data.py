import sqlite3
import pandas as pd

def main():
    # ファイル読み込み
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    # SQL命令関数
    sql_execute(cur,con)
    # SQLを実行しファイルにアクセス
    con.commit()
    # ファイルをクローズ
    con.close()

#     SQLの中身をデータフレームとして表示させる関数
def sql_result(sql_text,con):
    # SQL文表示
    print(f"「{sql_text}」")
    #    データフレーム変換
    df = pd.read_sql_query(sql_text, con)
    # 結果表示
    print(df)

#    この関数にSQL文を書き込み
def sql_execute(cur,con):
    # TABLE作成SQL命令文
    cur.execute("CREATE TABLE students(id, japanese,english, math, year)")

    # データ追加
    # studenst.csvを読み込み
    students_df = pd.read_csv("students.csv")
    # to_sql()でDataFrameをテーブルに追加(if_exists="append"で存在する場合は追加)
    students_df.to_sql("students", con, if_exists="append", index = None)
    # sql_result()関数を実行
    sql_result("SELECT * FROM students", con)

    # cur.execute()でテーブルを削除
    cur.execute("DROP TABLE students")

if __name__ == "__main__":
    main()