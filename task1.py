from datetime import datetime

#date = "2024-05-30"

def get_days_from_today(date):

    date_object = datetime.strptime(date, '%Y-%m-%d').date() #str to datatime
    today = datetime.today().date()  #now without time

    return (today - date_object).days


#print(get_days_from_today(date))