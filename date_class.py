import pandas as pd
import math

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

def create_data_for_year(year: int, survey_wave: int):
    activity = pd.read_csv('original_data/activity.csv')
    sleep = pd.read_csv('original_data/sleep_daily.csv')
    survey = pd.read_csv('refined_data/survey_all_{}.csv'.format(survey_wave))

    activity = activity[activity['datadate'].str.startswith(
        str(year))]
    sleep = sleep[sleep['dataDate'].str.startswith(str(year))]

    activity_sleep = pd.merge(sleep, activity, left_on=[
        'egoid', 'dataDate'], right_on=['egoid', 'datadate'])

    activity_sleep.drop('datadate', axis=1, inplace=True)
    activity_sleep['dataDate'] = activity_sleep['dataDate'].apply(get_class)
    activity_sleep_survey = pd.merge(activity_sleep, survey, on='egoid')
    activity_sleep_survey.to_csv(
        'final_data/activity_sleep_survey_date_extended_class_{}.csv'.format(year), index=False)


create_data_for_year(2015, 1)
