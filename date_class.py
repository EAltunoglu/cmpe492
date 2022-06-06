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
holidays = ['Thanksgiving', 'Mid-term break', 'Mid-Term break', 'Easter', 'Halloween', 'Christmas', 'Fall break', 'Spring break', 'Summer break', 'Winter break', 'fall break', 'spring break', 'summer break', 'winter break', 'thanksgiving', 'easter', 'halloween']


for row in calenderrows:
    # if not math.isnan(row['Beginning event date']) and not math.isnan(row['End event date']):
    if not math.isnan(row[BEGIN_DATE]):
        shortenedrows.append(row)


def get_class(date: str):
    date_float = float(date.replace('-', ''))
    last_applicable = 'b'

    for row in shortenedrows:
        if row[BEGIN_DATE] <= date_float <= row[END_DATE]:
            if row['Event'] == 'Class begins' or row['Event'] == 'Classes begin':
                return 'c'
            if row['Event'] == 'Final exam' or row['Event'] == 'Final exams':
                return 'f'
            return 'b'
        
        if row[BEGIN_DATE] <= date_float:
            last_applicable = row['Event']


    if last_applicable == 'Class begins' or last_applicable == 'Classes begin':
        last_applicable = 'c'

    if last_applicable in holidays:
        return 'c'
    
    if last_applicable == 'Final exams' or last_applicable == 'Final exam':
        return 'b'

    return last_applicable


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

activity = activity[activity['datadate'].str.startswith("2015")]
sleep = sleep[sleep['dataDate'].str.startswith("2015")]


activity_sleep = pd.merge(sleep, activity, left_on=['egoid', 'dataDate'], right_on=['egoid', 'datadate'] )
activity_sleep.drop('datadate', axis=1, inplace=True)
activity_sleep['dataDate'] = activity_sleep['dataDate'].apply(get_class)
activity_sleep.to_csv('merged_data/activity_sleep_daily_date_class_2015.csv', index=False)
