import pymssql


class GetDatabase:

    def connect(database):
        connect = pymssql.connect(server='172.18.67.205:2433',  # 服务器名或本地IP
                                  user='QA',  # 账户
                                  password='%8q*1QgLSDOyZB@%WcHK',  # 密码
                                  database=database)  # 连接的数据库名
        if connect:
            print("恭喜你，连接成功 !!！")
        else:
            print("连接失败！")
        return connect


if __name__=='__mian__':
    # 连接SFPassport数据库
    connect = GetDatabase.connect('SFPassport')
    connect.close()  # 关闭连接
