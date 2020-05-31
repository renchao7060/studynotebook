#!/usr/local/env/python
#_*_coding:utf-8_*_

# pymysql API模拟银行转账

import pymysql
import sys

class TransferMoney(object):
    def __init__(self,conn):
        self.conn=conn

    def check_acct_available(self,acc_id):
        cursor=self.conn.cursor()
        try:
            sql="SELECT * FROM account WHERE acctid=%s"%acc_id
            cursor.execute(sql)
            print('check_acct_available:'+sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception("账号%s不存在"%acc_id)
        finally:
            cursor.close()
            
    def has_enough_money(self,accid,money):
        cursor=self.conn.cursor()
        try:
            sql="SELECT * FROM account WHERE acctid=%s AND money >=%s"%(accid,money)
            cursor.execute(sql)
            print('has_enough_money:'+sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception("账号%s没有足够的钱"%accid)
        finally:
            cursor.close()

    def reduce_money(self,accid,money):
        cursor=self.conn.cursor()
        try:
            sql="UPDATE account SET money=money-%s WHERE acctid=%s"%(money,accid)
            cursor.execute(sql)
            print('reduce_money:'+sql)
            if cursor.rowcount!=1:
                raise Exception("账号%s减款失败"%accid)
        finally:
            cursor.close()

    def add_money(self,accid,money):
        cursor=self.conn.cursor()
        try:
            sql="UPDATE account SET money=money+%s WHERE acctid=%s"%(money,accid)
            cursor.execute(sql)
            print('add_money:'+sql)
            if cursor.rowcount!=1:
                raise Exception("账号%s加款失败"%accid)
        finally:
            cursor.close()

    def transfer(self,source_accid,target_accid,money):
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            self.has_enough_money(source_accid,money)
            self.reduce_money(source_accid,money)
            self.add_money(target_accid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

if __name__=='__main__':
    source_accid=sys.argv[1]
    target_accid=sys.argv[2]
    money=sys.argv[3]
    conn=pymysql.connect(host='192.168.99.100',port=3306,user='root',passwd='123456',db='bank' )
    # cursor=conn.cursor()
    # cursor.execute("SELECT VERSION()")
    # rs=cursor.fetchall()
    # print(rs)
    tr_money=TransferMoney(conn)
    try:
        tr_money.transfer(source_accid,target_accid,money)
    except Exception as e:
        print('出现问题：%s'%str(e))
    finally:
        conn.close()

'''
执行结果：
D:\project\workspace>python3 py96.py 1 2 100
check_acct_available:SELECT * FROM account WHERE acctid=1
check_acct_available:SELECT * FROM account WHERE acctid=2
has_enough_money:SELECT * FROM account WHERE acctid=1 AND money >100
reduce_money:UPDATE account SET money=money-100 WHERE acctid=1
add_money:UPDATE account SET money=money+100 WHERE acctid=2
'''