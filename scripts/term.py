import pandas as pd
import time
import datetime

def date_to_timestamp(date: str) -> int:
    return time.mktime(datetime.datetime.strptime(date,"%Y-%m-%d").timetuple())

def date_to_term(date: str) -> float:
    date = date.split('-')
    month = int(date[1])
    month = month // 4
    year = int(date[0])
    year = year - 2015
    year *= 3

    return year + month

def period_to_term(date: str) -> float:
    year = int(date[:4])
    year = year - 2015
    
    
    month = int(date[4:])
    month = month // 10
    if month == 1:
        month = 2
    elif month == 2:
        month = 0
        year += 1
    else:
        month = 1
    
    year *= 3

    return year + month

def convert_sleep():
    sleeps = pd.read_csv("../original_data/sleep.csv")
    sleeps['term'] = sleeps['dataDate'].apply(date_to_term)
    sleeps = sleeps.sort_values(by='egoid')
    sleeps.to_csv('../original_data/sleep_term.csv', index=False)

def convert_activity():
    activitys = pd.read_csv("../original_data/activity.csv")
    activitys['term'] = activitys['datadate'].apply(date_to_term)
    activitys = activitys.sort_values(by='egoid')
    activitys.to_csv('../original_data/activity_term.csv', index=False)

def convert_grade():
    grades = pd.read_csv("../original_data/grade.csv")
    grades['term'] = grades['AcademicPeriod'].apply(period_to_term)
    grades = grades.sort_values(by='egoid')
    grades.to_csv('../original_data/grade_term.csv', index=False)

def main():
    convert_sleep()
    convert_activity()
    convert_grade()

if __name__ == "__main__":
    main()