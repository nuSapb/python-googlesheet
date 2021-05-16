import re
import gspread

gc = gspread.service_account(filename='keys.json')
sh = gc.open_by_key('1BrhnuTtRs8yB0FHBbNu7G4Na1yQvbv1V242cqB4Dcyo')

worksheet = sh.sheet1

# res = worksheet.get_all_records() #return dict {}
# res = worksheet.get_all_values() #return list []
# res = worksheet.row_values(1) #return specific row
# res = worksheet.col_values(1) #return specific column
# res = worksheet.get('A2:C2') #retrun range of data

user = ["Susan", 25, "Sydney"]
# worksheet.insert_row(user,3) #insert data to specific row
worksheet.append_row(user) #append data to last row
worksheet.update_cell(6,2,28) #update data to specific cell (row, column, )

# print(res)