import datetime
from dateutil.relativedelta import relativedelta


def generate_data():

    today = datetime.date.today()
    last_month = today + relativedelta(months=-1)
    next_month = today + relativedelta(months=+1)

    d = [{"_id": f"demo-{day.year}-{day.month:02}", "user_id": "demo", "month": f"{day.year}-{day.month:02}"}
         for day in [today, last_month, next_month]]

    return {'user': { 'user_id': 'demo' }, 'plans': d}

if __name__ == '__main__':
    print(generate_data())