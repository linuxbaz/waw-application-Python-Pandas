# from dataDB import DBApiuse
import os.path
import requests
import pandas as pd
from guizero import App, Box, TextBox, Picture, Text,\
 PushButton, ListBox, Drawing, Combo
from match_phones import MergeFind
from dataDB import DBApiuse
import report_run
# dict1 = {'IDs': [[8888888888], [7777777777]], 'phones': ['09127820525', '09185793788']}
#
#
# list_id = dict1.pop("IDs")
# list_phone = dict1.pop("phones")
#
# len = len(list_id)
# list = []
# for i in range(0,len):
#     t = (str(list_id[i][0]), list_phone[i])
#     list.append(t)
# print(list)
#
#
#
#
#
# d1 = DBApiuse(list, "std_id", "parent_phone")
# d1.insertlisttoDB()
#number = '9127820525.0'
#x = number.rstrip(".0")
#print(x)

# c_absent_phone = { "IDs" : [], "phones" : [] }
# dic_absent_phone["IDs"] = [333,444,555]
# dic_absent_phone["IDs"] += [33,44]
# print(dic_absent_phone["IDs"])

########  test get data from DB
d1 = DBApiuse({""}, "std_id", "parent_phone")
dict_db_data = d1.get_data("4311874561")
print(dict_db_data)