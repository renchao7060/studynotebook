
#python通过 DB API 调用数据库信息


def test_pymysql():
    '''MySQL连接测试'''
    import pymysql
    conn=pymysql.connect(host='192.168.99.100',port=3306,user='root',passwd='123456',db='bank')
    cursor=conn.cursor()
    sql="SELECT * FROM account"
    cursor.execute(sql)
    rs=cursor.fetchall()
    for row in rs:
        print('account_id:%s\tmoney:%s'%(row[0],row[1]))
        
        
def test_pymongo():
    '''MongoDB连接测试'''
    from pymongo import MongoClient
    client=MongoClient('192.168.99.100',27017)
    test_db=client['testdb']
    test_table=test_db['user_info']
    test_table.insert_one({'username':'renchao','password':123456})
    
if __name__=='__main__':
    test_pymysql()

