from datetime import datetime, timedelta

Date = input("YYYY-MM-DD: ")
try:
    Input_Date = datetime.strptime(Date, '%Y-%m-%d')

    New_Date = Input_Date + timedelta(days=1)

    New_new_Date = New_Date.strftime('%Y-%m-%d')

    print("Next Date:", New_new_Date)

except: print("Input format ERROR. Correct Format: YYYY-MM-DD")