import mysql.connector
import datetime as dt
import storage
from mysql.connector import MySQLConnection, Error


class DBApiuse:
    def __init__(self, dict, fieldName1, fieldName2):
        self.list = list
        self.FildName1 = fieldName1
        self.FildName2 = fieldName2
        self.dict = dict

    def dict_to_sqlData(self):
        #print(self.dict)
        list_id = self.dict.pop("IDs")
        list_phone = self.dict.pop("phones")
        count = 0
        count = len(list_id)
        list = []
        for i in range(0,count):
            t = (str(list_id[i]), str(list_phone[i]).rstrip(".0"))
            list.append(t)
        return list


    def insertlisttoDB(self):
        cnx = storage.connect()
        cursor = cnx.cursor()

        vals = self.dict_to_sqlData()
        print(vals)
        try:
            cursor.executemany(u"INSERT INTO absents_phones(std_id, parent_phone) VALUES (%s, %s)", vals)

            # if cursor.lastrowid:
            #     print('last insert id', cursor.lastrowid)
            # else:
            #     print('last insert id not found')
            cnx.commit()
        except Error as error:
            print("error = ")

        finally:
            cursor.close()
            cnx.close()

    def get_data(self,std_id):
        dict = {}
        cnx = storage.connect()
        cursor = cnx.cursor()
        #count of absent
        sql = "SELECT count(parent_phone) FROM absents_phones where std_id = %s"
        id = (std_id, )
        cursor.execute(sql, id)
        myresult = cursor.fetchall()
        dict["count"] = myresult[0]
        #report of absent
        sql = "SELECT * FROM absents_phones where std_id = %s"
        id = (std_id, )
        cursor.execute(sql, id)
        myresult = cursor.fetchall()
        dict["data"] = myresult
        return dict
