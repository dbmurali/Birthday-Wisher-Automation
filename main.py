import datetime as dt
import pandas as pd
import smtplib

user_id="your@gmail.com"
password="app_password"

today=dt.datetime.now().date()
current_day=(int(str(today.day)))
current_month=(int(str(today.month)))


csv_data=pd.read_csv("data.csv")
data=pd.DataFrame(csv_data)
new_data=data.to_dict(orient="records")
birthday_list=[val for val in new_data if( val["date"]==current_day)& (val["month"]==current_month)]
print(birthday_list)

for val in birthday_list:
    res_email=val["email"]
    res_name=val["name"]

    with open("letter.txt", "r") as letter:
        name_list = letter.readlines()
    updated_letter = [name.replace("[name]", f" {res_name}") for name in name_list]

    with open(f"{res_name}_letter.txt", "w") as letter:
        letter.writelines(updated_letter)
    with open(f"{res_name}_letter.txt","r")as renamed_letter:
        new=renamed_letter.read()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_id,password=password)
        connection.sendmail(from_addr=user_id,to_addrs=res_email,msg=f"Subject:Happy Birthday\n\n{new}")
        print(f"Mail send{res_name}")





