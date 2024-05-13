import sqlite3
import pandas as pd

def main():
    # 読み込みOR新規作成
    con = sqlite3.connect("data.db")
    cur = con.cursor()

    make_table(cur, con)
    execute_sql(con)

    cur.execute("DROP TABEL students")
    con.commit()
    con.close()

def sql_result(sql_text, con):
    print(f"「{sql_text}」")
    df = pd.read_sql_query(sql_text, con)
    print(df)

def make_table(cur,con):

    cur.execute("CREATE TABLE students(id, japanese, english, math, year)")

    students_df = pd.real_csv("../01_python_sqlite/students.csv")
    students_df.to_sql("students", con, if_exists="append",index=None)

    sql_result("SeLECT * FROM students", con)

def execute_sql(con):