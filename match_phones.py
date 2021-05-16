import os.path
import pandas as pd

class MergeFind:
    def __init__(self, cf, ap):
        self.Count_of_Absent_Files = cf
        self.absent_path = ap

        #Dictionary for store IDs and parent's phones
    dic_absent_phone = { "IDs" : [], "phones" : [] }

    def Merge_files(self):
        i = 0
        List_of_Absent_xlsx = []
        Msg_empty_file = ""
        Msg_file_not_found = ""
	#Get files from folder one by one rename and save to list
        while(i < self.Count_of_Absent_Files):
            if not(os.path.exists(self.absent_path + "/" +str(i) + ".xlsx")):
                Msg_file_not_found += " \n " + str(i+1) + ".xlsx not found !"
            else:
                f = pd.read_excel(self.absent_path + "/" +str(i) + ".xlsx")
            if f.empty:
                Msg_empty_file += " \n " + str(i) + ".xlsx was empty !"
            else:
                List_of_Absent_xlsx.append(f)
            i += 1
	#merge the files
        df = pd.concat(List_of_Absent_xlsx)
        writer = pd.ExcelWriter('./absent/students_id.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='sheet1', index=False)
        writer.save()

    def fn_compare_and_extract_phones(self):
        phones = []
        pd_std = pd.read_excel("./absent/students_id.xlsx")
        pd_parent = pd.read_excel("./parents.xlsx")

        df_std = pd.DataFrame(pd_std, columns= ['id'])
        df_parent_id = pd.DataFrame(pd_parent, columns= ['id'])
        df_phone = pd.DataFrame(pd_parent, columns= ['phone'])

        list_parent_id = df_parent_id.values.tolist()
        list_std_id = df_std.values.tolist()
        list_phone = df_phone.values.tolist()
        # print(list_std_id)
        # print(list_parent_id)
        # print(list_phone)

        #print("-------- result of search ---------")
        res =[]
        i = 0
        k = 0
        while (i < len(list_parent_id)):
            for k in range(0,len(list_std_id)):
                #match ID in Parent file and ID in Absent Students file
                if (list_std_id[k] == list_parent_id[i]):
                    self.dic_absent_phone["IDs"] += list_std_id[k]
                    self.dic_absent_phone["phones"] += list_phone[i]
            i += 1

    # printing result
        #print(self.dic_absent_phone)

        df = pd.DataFrame(phones)
        writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='phones', index=False)
        writer.save()
        return self.dic_absent_phone
