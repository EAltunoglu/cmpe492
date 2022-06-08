import pandas as pd
import math

calendercsv = pd.read_csv('../original_data/calender.csv')
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

def create_data_activity_sleep_survey_grade(survey_wave: int, academic_period: int):
    activity = pd.read_csv('../refined_data/activity/activity_knn_term.csv')
    sleep = pd.read_csv('../refined_data/sleep/sleep_daily_timestamp_term.csv')
    survey = pd.read_csv('../refined_data/survey_all_{}.csv'.format(survey_wave))
    grade = pd.read_csv('../original_data/grade.csv')

    # activity = activity[activity['AcademicPeriod'] == academic_period]
    # sleep = sleep[sleep['AcademicPeriod'] == academic_period]

    activity_sleep = pd.merge(sleep, activity, left_on=[
        'egoid', 'dataDate', 'AcademicPeriod'], right_on=['egoid', 'datadate', 'AcademicPeriod'])
    activity_sleep = activity_sleep[activity_sleep['AcademicPeriod'] == academic_period]

    activity_sleep.drop('datadate', axis=1, inplace=True)
    activity_sleep['dataDate'] = activity_sleep['dataDate'].apply(get_class)
    activity_sleep_survey = pd.merge(activity_sleep, survey, on='egoid')

    # activity_sleep_survey.to_csv('../refined_data/activity_sleep_survey_grade_{}.csv'.format(survey_wave), index=False)
    activity_sleep_survey_grade = pd.merge(activity_sleep_survey, grade, on=['egoid', 'AcademicPeriod'])
    activity_sleep_survey_grade.to_csv(
        '../final_data/activity_sleep_survey_grade/activity_sleep_survey_grade_{}.csv'.format(survey_wave), index=False)


# missing 201500 201700 201800 201810
#               201510       201520       201600       201610      201620      201710      201720      201820
academic_periods = [201510, 201520, 201600, 201610, 201620, 201710, 201720, 201820]

for wave in range(1, 9):
    create_data_activity_sleep_survey_grade(wave, academic_period=academic_periods[wave - 1])
