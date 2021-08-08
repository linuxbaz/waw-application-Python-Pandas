import pandas as pd
import numpy as np
import jinja2


#convert miladi to shamsi
def gregorian_to_jalali(gy, gm, gd):
 g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
 if (gm > 2):
  gy2 = gy + 1
 else:
  gy2 = gy
 days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
 jy = -1595 + (33 * (days // 12053))
 days %= 12053
 jy += 4 * (days // 1461)
 days %= 1461
 if (days > 365):
  jy += (days - 1) // 365
  days = (days - 1) % 365
 if (days < 186):
  jm = 1 + (days // 31)
  jd = 1 + (days % 31)
 else:
  jm = 7 + ((days - 186) // 30)
  jd = 1 + ((days - 186) % 30)
 return [jy, jm, jd]




#Create Report Table Data
def create_report_data(dict):
    print(dict)
    report_data = []
    str_date = ''
    for d in dict["data"]:
        year = d[3].date().strftime('%Y')
        month = d[3].date().strftime('%m')
        day = d[3].date().strftime('%d')
        #[dd,mm,dd]
        temp_date_list = gregorian_to_jalali(int(year),int(month),int(day))
        #list date to numeric
        for dd in temp_date_list:
            str_date += str(dd)
        report_data.append([int(str_date),int(d[2])])
        str_date = ''
    count_column_list = list(range(1, dict["count"][0]+1))
    print(report_data)

#DataFrame

    df = pd.DataFrame(report_data, columns=['تاریخ','شماره موبایل'],
                      index = count_column_list)
    def color_negative_red(val):
        color = 'red'
        return f'color: {color}'

    styler = df.style.applymap(color_negative_red)

    # Template handling
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
    template = env.get_template('template.html')
    html = template.render(my_table=styler.render())

    # # Plot
    # ax = df.plot.bar()
    # fig = ax.get_figure()
    # fig.savefig('plot.svg')

    # Write the HTML file
    with open('report.html', 'w') as f:
        f.write(html)
