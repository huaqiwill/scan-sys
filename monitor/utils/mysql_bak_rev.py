import datetime
import os
import pymysql


def backup():
    # 数据库连接信息
    db_host = "localhost"
    db_user = "root"
    db_password = "123456"
    db_name = "tp_admin"

    # 备份文件保存路径
    backup_path = "D:/Data/Desktop/"
    backup_file = os.path.join(
        backup_path, f'{db_name}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.sql'
    )

    # 连接数据库
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()

    # 执行备份命令
    dump_command = (
        f"mysqldump -u {db_user} -p{db_password} --databases {db_name} > {backup_file}"
    )
    os.system(dump_command)

    # 关闭数据库连接
    cursor.close()
    connection.close()

    print(f"数据库 {db_name} 已成功备份到 {backup_file}")


def recover():
    # 数据库连接信息
    db_host = "localhost"
    db_user = "your_username"
    db_password = "your_password"
    db_name = "your_database_name"

    # 备份文件路径
    backup_file = "/path/to/your/backup/file.sql"

    # 连接数据库
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password)
    cursor = connection.cursor()

    # 创建数据库（如果不存在）
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name};"
    cursor.execute(create_db_query)

    # 选择数据库
    use_db_query = f"USE {db_name};"
    cursor.execute(use_db_query)

    # 读取备份文件内容并执行
    with open(backup_file, "r") as file:
        for line in file:
            # 跳过注释和空行
            if line.startswith("--") or line.strip() == "":
                continue
            cursor.execute(line)

    # 提交事务
    connection.commit()

    # 关闭数据库连接
    cursor.close()
    connection.close()

    print(f"数据库 {db_name} 已成功从 {backup_file} 恢复")
