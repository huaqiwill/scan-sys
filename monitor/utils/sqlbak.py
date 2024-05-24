"""
数据备份和恢复模块
"""

import datetime
import os
import pymysql
import mysql.connector
import pandas as pd


def backup_database(host, user, password, database, backup_path):
    try:
        # 连接到数据库
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, connection)
            df.to_csv(f"{backup_path}/{table_name}.csv", index=False)
            print(f"Table {table_name} backed up successfully.")
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def restore_database(host, user, password, database, backup_path):
    try:
        # 连接到数据库
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        cursor = connection.cursor()

        for file in os.listdir(backup_path):
            if file.endswith(".csv"):
                table_name = file.split(".")[0]
                file_path = os.path.join(backup_path, file)
                df = pd.read_csv(file_path)

                # 删除表中的所有数据
                cursor.execute(f"DELETE FROM {table_name}")

                # 恢复数据
                for index, row in df.iterrows():
                    placeholders = ", ".join(["%s"] * len(row))
                    columns = ", ".join(row.index)
                    sql = (
                        f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                    )
                    cursor.execute(sql, tuple(row))
                connection.commit()
                print(f"Table {table_name} restored successfully.")
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


import mysql.connector


def backup_database_to_sql_file(host, user, password, database, backup_file_path):
    try:
        # 连接到数据库
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        with open(backup_file_path, "w", encoding="utf-8") as backup_file:
            for table in tables:
                table_name = table[0]

                # 获取表创建语句
                cursor.execute(f"SHOW CREATE TABLE {table_name}")
                create_table_stmt = cursor.fetchone()[1]
                backup_file.write(f"{create_table_stmt};\n\n")

                # 获取表数据
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                # 写入插入语句
                for row in rows:
                    values = []
                    for value in row:
                        if value is not None:
                            value = str(value).replace("'", "\\'")
                            values.append(value)
                        else:
                            value = "NULL"
                            values.append(value)

                    values_str = ", ".join(values)
                    backup_file.write(
                        f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values_str});\n"
                    )
                backup_file.write("\n\n")

                print(f"Table {table_name} backed up successfully.")
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


import mysql.connector


def restore_database_from_sql_file(host, user, password, database, backup_file_path):
    try:
        # 连接到数据库
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        cursor = connection.cursor()

        with open(backup_file_path, "r", encoding="utf-8") as backup_file:
            sql_statements = backup_file.read().split(";")
            for statement in sql_statements:
                if statement.strip():
                    cursor.execute(statement)
                    connection.commit()

        print("Database restored successfully from SQL file.")
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def backup():
    backup_database_to_sql_file(
        "localhost", "root", "123456", "auth_system", "./backup.sql"
    )


def restore():
    restore_database_from_sql_file(
        "localhost", "root", "123456", "auth_system2", "./backup.sql"
    )
