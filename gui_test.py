from guizero import App, Text, Combo, PushButton

str = "هنرستان جابر:با سلام.فرزند شما در روز"

def month_choose(selected_value):
    global str
    str += ' ' + selected_value
    print(str)

def day_choose(selected_value):
    global str
    str += ' ' + selected_value
    print(str)

def absent_type_choose(selected_value):
    global str
    str += ' در ' + selected_value
    print(str)

def fn_build_message():
    global str
    str += ' غیبت داشته است. '
    print(str)


list_day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
combo_day = Combo(app, options = list_day, command = day_choose, width = '5')

instructions = Text(app, text="Choose a goblet")
combo_month = Combo(app, options=["مهر","آبان","آذر","دی","بهمن","اسفند","فروردین","اردیبهشت","خرداد","تیر",],\
                    command = month_choose, width = '15')

list_absent_type = ["کلاس مجازی","کلاس","امتحان"]
combo_absent_type = Combo(app, options = list_absent_type, command = absent_type_choose, width = '15')

PushButton(app, command = fn_build_message, text=" ارسال پیام ")

result = Text(app)
app.display()
