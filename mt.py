import os.path
import requests
import pandas as pd
from guizero import App, Box, TextBox, Picture, Text,\
 PushButton, ListBox, Drawing, Combo
from match_phones import MergeFind
from dataDB import DBApiuse
import report_run

Msg_file_not_found =0
Msg_file_empty = 0
cf = -1


def get_folder(): # and_rename_xlsx_files simple
   global absent_path
   absent_path = frm1.select_folder()
   files = os.listdir(absent_path)
   global cf


   for index, file in enumerate(files):
      cf += 1
      os.rename(os.path.join(absent_path, file), os.path.join(absent_path, ''.join([str(index), '.xlsx'])))




#create object from MergFind class and call methods
def fn_test():
    print(absent_path)
    m_f = MergeFind(cf, absent_path)
    m_f.Merge_files()
    lbl2 = Text(frm1,text="+ ok : ادغام فایل موفق +",font = 'B Titr', size = '11', color = "green")
    #get a Dictionary of IDs and phones
    global dic_absent_phone
    dic_absent_phone = m_f.fn_compare_and_extract_phones()

def fn_DB():
    #DB : insert to Absents Table
    d1 = DBApiuse(dic_absent_phone, "std_id", "parent_phone")
    d1.insertlisttoDB()


def fn_send():
    #Sending
    global str_SMS
    phones = []
    phone_str = 0
    [phones.append(x) for x in dic_absent_phone["phones"] if x not in phones]
    for number in phones:
        phone_str = str(number).rstrip(".0")
        payload = {'Username': 'jaberedu', 'Password' : '65361000', 'From' : '-1', 'To' : '0'+ phone_str, 'Text' : str_SMS}
        r = requests.post('https://www.payam-resan.com/APISend.aspx', params = payload)
        print(r.url)
    str_SMS = ""

def fn_find_month(selected_value):
    pass
def fn_find_count():
    dict = {}
    if (len(std_id_find_textbox.value) != 10):
        frm1.info(" اشتباه شماره دانش آموز", std_id_find_textbox)
    else:
        d1 = DBApiuse({""}, "std_id", "parent_phone")
        dict_db_data = d1.get_data(std_id_find_textbox.value)
        print(dict_db_data)
        report_run.create_report_data(dict_db_data)
        Text(options_box, text= dict_db_data["count"][0])






str_SMS = ""
absent_path = ""
dic_absent_phone = {}
month_list = ["مهر","آبان","آذر","دی","بهمن","اسفند","فروردین","اردیبهشت","خرداد","تیر",]
list_day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

def month_choose(selected_value):
    global str_SMS
    str_SMS += ' ' + selected_value

def day_choose(selected_value):
    global str_SMS
    str_SMS = "هنرستان جابر:با سلام.فرزند شما در روز"
    str_SMS += ' ' + selected_value

def absent_type_choose(selected_value):
    global str_SMS
    str_SMS += ' در ' + selected_value

def fn_build_message():
    global str_SMS
    str_SMS += ' غیبت داشته است. '
    frm1.info("info", str_SMS)

frm1 = App(title=" جابر ابن حیان ",height="430",width = '500')


#-------------Reports
options_box = Box(frm1, height="fill", align="right",border=True)
content_box = Box(frm1, align="top", width="fill", border=True)
Text(options_box, text="گزارش گیری")



#form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)
# Text(options_box, grid=[0,0], text="form", align="right")
# Text(options_box, grid=[0,1], text="label", align="left")
combo_month_find = Combo(options_box, options= month_list,\
                    command = fn_find_month, width = '15')
std_id_find_textbox = TextBox(options_box, grid=[1,1], width="fill")
PushButton(options_box, command=fn_find_count, text="  جستجو  ")


#-------------Main Buttons

Text(frm1, text="عملیات فایل")
PushButton(frm1, command=get_folder, text="مسیر فایلها", width = '12')
PushButton(frm1,command=fn_test, text="     ادغام     ", width = '12')



#SMS_message Set

Text(frm1, text="_____________")
combo_day = Combo(frm1, options = list_day, command = day_choose, width = '7')

combo_month = Combo(frm1, options= month_list,\
                    command = month_choose, width = '7')

list_absent_type = ["کلاس مجازی","کلاس","امتحان"]
combo_absent_type = Combo(frm1, options = list_absent_type, command = absent_type_choose, width = '7')
Text(frm1, text="_____________")
PushButton(frm1, command = fn_build_message, text=" ساخت پیام ", width = '12')
PushButton(frm1,command=fn_send, text=" ارسال پیام ", width = '12')
PushButton(frm1,command=fn_DB, text="ثبت داده ها", width = '12')
#Copy Right
buttons_box = Box(frm1, width="fill", align="bottom", border=True)
lbl2=Text(buttons_box,text="by:Abbas Vakilfard",align = 'bottom',font = 'B Titr', size = '9')
lbl2.text_color = "#222222"
lbl2=Text(buttons_box,text="حق انتشار محفوظ میباشد",align = 'bottom',font = 'B Titr', size = '9')
lbl2.text_color = "#222222"
frm1.display()
