import pandas as pd
import time
import datetime

def date_to_timestamp(date: str) -> int:
    return time.mktime(datetime.datetime.strptime(date,"%Y-%m-%d").timetuple())

def date_to_term(date: str) -> int:
    date = date.split('-')
    month = int(date[1])
    year = int(date[0])
    #    201800: Summer semester of AY 2018-2019 which is Summer of calendar year 2018
    #    201810:   Fall semester of Academic Year  (AY) 2018-2019
    #    201820:  Spring semester of AY 2018-2019, i.e.  Spring of calendar year 2019
    
    term_suff = 1 # Fall months 9-10-11-12 

    if month <= 6: # Spring check
        term_suff = 2
        year -= 1
    elif month < 9: # Summer check
        term_suff = 0

    return '{}{}0'.format(year, term_suff)

def convert_sleep():
    sleep = pd.read_csv("../refined_data/sleep/sleep_daily_timestamp.csv")
    sleep['AcademicPeriod'] = sleep['dataDate'].apply(date_to_term)
    sleep = sleep.sort_values(by='egoid')
    sleep.to_csv('../refined_data/sleep/sleep_daily_timestamp_term.csv', index=False)
    return sleep

def convert_activity():
    activity = pd.read_csv("../refined_data/activity/activity_knn.csv")
    activity['AcademicPeriod'] = activity['datadate'].apply(date_to_term)
    activity = activity.sort_values(by='egoid')
    activity.to_csv('../refined_data/activity/activity_knn_term.csv', index=False)
    return activity

def main():
    sleep = convert_sleep()
    activity = convert_activity()
    

def test():
    print(date_to_term('2019-08-01'))
    print(date_to_term('2019-11-02'))
    print(date_to_term('2019-05-03'))
    print(date_to_term('2019-09-03'))

if __name__ == "__main__":
    main()
    # test()
