import pandas as pd
import time
import datetime

def date_to_timestamp(date: str) -> int:
    return time.mktime(datetime.datetime.strptime(date,"%Y-%m-%d").timetuple())

def date_to_term(date: str) -> int:
    date = date.split('-')
    month = int(date[1])
    month = month // 4
    year = int(date[0])
    term_suff = 1    

    if month <= 6:
        term_suff = 2
        year -= 1
    elif month <= 9:
        term_suff = 0

    return '{}{}0'.format(year,term_suff)

def convert_sleep():
    sleeps = pd.read_csv("../original_data/sleep.csv")
    sleeps['AcademicPeriod'] = sleeps['dataDate'].apply(date_to_term)
    sleeps = sleeps.sort_values(by='egoid')
    sleeps.to_csv('../original_data/sleep_term.csv', index=False)

def convert_activity():
    activitys = pd.read_csv("../original_data/activity.csv")
    activitys['AcademicPeriod'] = activitys['datadate'].apply(date_to_term)
    activitys = activitys.sort_values(by='egoid')
    activitys.to_csv('../original_data/activity_term.csv', index=False)

def main():
    convert_sleep()
    convert_activity()

if __name__ == "__main__":
    main()