import pandas as pd
import math
import time
import datetime

calendercsv = pd.read_csv('original_data/calender.csv')
calenderrows = [row for index, row in calendercsv.iterrows()]
shortenedrows = []
BEGIN_DATE = 'Beginning event date'
END_DATE = 'End event date'
holidays = ['Thanksgiving', 'Mid-term break', 'Mid-Term break', 'Easter', 'Summer break',
            'Winter break', 'Fall break', 'Spring break', 'fall break', 'spring break']


for row in calenderrows:
    if not math.isnan(row[BEGIN_DATE]):
        shortenedrows.append(row)


def get_term(date: str):
    if 1 <= int(date.split('-')[1]) <= 7:
        return 'spring'
    return 'fall'

def get_timestamp(date: str):
    return int(time.mktime(datetime.datetime.strptime(date,
                                             "%Y-%m-%d").timetuple()))

def get_class(date: str):
    date_float = float(date.replace('-', ''))
    last_applicable = 'summer_break'

    for row in shortenedrows:
        if row[BEGIN_DATE] <= date_float <= row[END_DATE]:
            if row['Event'] == 'Class begins' or row['Event'] == 'Classes begin':
                return get_term(date) + '_class'
            if row['Event'] == 'Final exam' or row['Event'] == 'Final Exams' or row['Event'] == 'Final exams':
                return get_term(date) + '_final'
            return get_term(date) + '_break'

        if row[BEGIN_DATE] <= date_float:
            last_applicable = row['Event']

    if last_applicable == 'Class begins' or last_applicable == 'Classes begin':
        last_applicable = get_term(date) + '_class'

    if last_applicable in holidays:
        return get_term(date) + '_class'

    if last_applicable == 'Final exams' or last_applicable == 'Final exam':
        if 2 <= int(date.split('-')[1]) <= 10:
            return 'summer_break'
        return 'winter_break'

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

# print(get_class('2017-04-14'))

# print(get_class('2016-01-10'))
# print(get_class('2016-01-11'))
# print(get_class('2016-01-12'))
# print(get_class('2016-01-13'))

def create_data_for_year(survey_wave: int, start_date: str, end_date: str):
    # activity = pd.read_csv('original_data/activity.csv')
    activity = pd.read_csv('refined_data/activity/activity_knn.csv')
    sleep = pd.read_csv('refined_data/sleep/sleep_daily_timestamp.csv')
    survey = pd.read_csv('refined_data/survey_all_{}.csv'.format(survey_wave))

    # activity = activity[activity['datadate'].str.startswith(
    #     str(year))]
    # sleep = sleep[sleep['dataDate'].str.startswith(str(year))].dropna()

    start_timestamp = get_timestamp(start_date)
    end_timestamp = get_timestamp(end_date)

    activity['timestamp'] = activity['datadate'].apply(get_timestamp)
    sleep['timestamp'] = sleep['dataDate'].apply(get_timestamp)

    activity = activity[activity['timestamp'].between(start_timestamp, end_timestamp, 'left')]
    sleep = sleep[sleep['timestamp'].between(start_timestamp, end_timestamp, 'left')]

    activity.drop('timestamp', axis=1, inplace=True)
    sleep.drop('timestamp', axis=1, inplace=True)

    activity_sleep = pd.merge(sleep, activity, left_on=[
        'egoid', 'dataDate'], right_on=['egoid', 'datadate'])

    activity_sleep.drop('datadate', axis=1, inplace=True)
    activity_sleep['dataDate'] = activity_sleep['dataDate'].apply(get_class)
    activity_sleep_survey = pd.merge(activity_sleep, survey, on='egoid')
    activity_sleep_survey.to_csv(
        'final_data/sleep_timestamp/activity_sleep_survey_date_extended_{}.csv'.format(survey_wave), index=False)

def create_data_without_survey(wave: int, start_date: str, end_date: str):
    # activity = pd.read_csv('original_data/activity.csv')
    activity = pd.read_csv('refined_data/activity/activity_knn.csv')
    sleep = pd.read_csv('refined_data/sleep/sleep_daily_timestamp.csv')

    # activity = activity[activity['datadate'].str.startswith(
    #     str(year))]
    # sleep = sleep[sleep['dataDate'].str.startswith(str(year))].dropna()

    start_timestamp = get_timestamp(start_date)
    end_timestamp = get_timestamp(end_date)

    activity['timestamp'] = activity['datadate'].apply(get_timestamp)
    sleep['timestamp'] = sleep['dataDate'].apply(get_timestamp)

    activity = activity[activity['timestamp'].between(start_timestamp, end_timestamp, 'left')]
    sleep = sleep[sleep['timestamp'].between(start_timestamp, end_timestamp, 'left')]

    activity.drop('timestamp', axis=1, inplace=True)
    sleep.drop('timestamp', axis=1, inplace=True)

    activity_sleep = pd.merge(sleep, activity, left_on=[
        'egoid', 'dataDate'], right_on=['egoid', 'datadate'])

    activity_sleep.drop('datadate', axis=1, inplace=True)
    activity_sleep['dataDate'] = activity_sleep['dataDate'].apply(get_class)
    activity_sleep.to_csv(f'final_data/activity_sleep/activity_sleep_date_extended_{wave}.csv', index=False)

#               201400       201510       
##              8/3/2015     1/31/2016    6/20/2016    11/1/2016   4/10/2017   11/9/2017   4/26/2018     4/12/2019
begin_dates = ['2015-1-1' , '2015-11-1', '2016-4-15', '2016-9-1', '2017-1-1', '2017-7-1', '2018-1-1', '2019-1-1']
end_dates   = ['2015-11-1', '2016-4-15', '2016-9-1' , '2017-1-1', '2017-7-1', '2018-1-1', '2019-1-1', '2020-1-1']

# for wave in range(1, 9):
#     create_data_for_year(wave, begin_dates[wave-1], end_dates[wave-1])

for wave in range(1, 9):
    create_data_without_survey(wave, begin_dates[wave-1], end_dates[wave-1])

# create_data_for_year(2016, 1, begin_dates[1], end_dates[1])
# create_data_for_year(2016, 2)
