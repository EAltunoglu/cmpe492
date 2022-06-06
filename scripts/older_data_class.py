import pandas as pd
import numpy as np
import math

calendercsv = pd.read_csv('original_data/calender.csv')
calenderrows = [row for index, row in calendercsv.iterrows()]
shortenedrows = []
BEGIN_DATE = 'Beginning event date'
END_DATE = 'End event date'
# BEGIN_DATE = 'Begin Date'
# END_DATE = 'End date'
holidays = ['Thanksgiving', 'Mid-term break', 'Mid-Term break', 'Easter']


for row in calenderrows:
    # if not math.isnan(row['Beginning event date']) and not math.isnan(row['End event date']):
    if not math.isnan(row[BEGIN_DATE]):
        shortenedrows.append(row)


def get_class(date: str):
    date_float = float(date.replace('-', ''))
    # next_class_begin = None
    # last_class_begin = 20140325
    # last_final_exam = 20140325
    # next_final_exam = None
    last_applicable = 'Summer break'

    for row in shortenedrows:
        if row[BEGIN_DATE] <= date_float <= row[END_DATE]:
            if row['Event'] == 'Class begins' or row['Event'] == 'Classes begin':
                return 'class'
            if row['Event'] == 'Final exam':
                return 'final exams'
            return row['Event'].lower()
        
        if row[BEGIN_DATE] <= date_float:
            last_applicable = row['Event']

        # if row[END_DATE] < date_float and row['Event'] == 'Final exams':
        #     last_final_exam = row[END_DATE]
        
        # if row[BEGIN_DATE] > date_float and next_class_begin is None and row['Event'] == 'Class begins':
        #     next_class_begin = row[BEGIN_DATE]
        
        # if row[BEGIN_DATE] > date_float and next_final_exam is None and row['Event'] == 'Final Exams':
        #     next_class_begin = row[BEGIN_DATE]
        
        # if row[]

    # if not next_class_begin:
    #     next_class_begin = 20220000
    # if not next_final_exam:
    #     next_final_examp = 2022000

    if last_applicable == 'Class begins' or last_applicable == 'Classes begin':
        last_applicable = 'Class'

    if last_applicable in holidays:
        return 'class'
    
    if last_applicable == 'Final exams' or last_applicable == 'Final exam':
        if 2 <= int(date.split('-')[1]) <= 10:
            return 'summer break'
        return 'winter break'

    return last_applicable.lower()


# print(get_class('2015-08-22'))
# print(get_class('2015-08-23'))
# print(get_class('2015-08-25'))
# print(get_class('2015-08-26'))
# print(get_class('2015-10-16'))
# print(get_class('2015-10-17'))
# print(get_class('2015-10-25'))
# print(get_class('2015-10-26'))

# print(get_class('2015-11-24'))
# print(get_class('2015-11-25'))
# print(get_class('2015-11-29'))
# print(get_class('2015-11-30'))
# print(get_class('2015-12-18'))
# print(get_class('2015-12-19'))



# activity = pd.read_csv('original_data/activity.csv')
# activity['datadate'] = activity['datadate'].apply(get_class)
# activity.to_csv('original_data/activity_date_class.csv', index=False)

# sleep = pd.read_csv('original_data/sleep_daily.csv')
# sleep['dataDate'] = sleep['dataDate'].apply(get_class)
# sleep.to_csv('original_data/sleep_daily_date_class.csv', index=False)

activity = pd.read_csv('original_data/activity.csv')
sleep = pd.read_csv('original_data/sleep_daily.csv')

activity_sleep = pd.merge(sleep, activity, left_on=['egoid', 'dataDate'], right_on=['egoid', 'datadate'] )
activity_sleep.drop('datadate', axis=1, inplace=True)
activity_sleep['dataDate'] = activity_sleep['dataDate'].apply(get_class)
activity_sleep.to_csv('merged_data/activity_sleep_daily_date_class.csv', index=False)

# activity_sleep = pd.read_csv('merged_data/sleep_activity.csv')
# activity_sleep['dataDate'] = activity_sleep['dataDate'].apply(get_class)
# activity_sleep.drop('datadate', axis=1, inplace=True)
# activity_sleep.to_csv('merged_data/activity_sleep_date_class.csv', index=False)
