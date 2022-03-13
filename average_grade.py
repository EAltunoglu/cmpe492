import pandas as pd
import pandasql as psql

LETTERGRADES = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'E': 0,
    'F': 0
}

def get_number_grade(letter_grade: str) -> float:
    return LETTERGRADES[letter_grade]

def get_average_manually(grades: pd.DataFrame) -> pd.DataFrame:
    grade_count = {}
    grade_sum = {}
    averages = []
    egos = []

    for index, row in grades.iterrows():
        grade_count[row['egoid']] = 0
        grade_sum[row['egoid']] = 0

    for index, row in grades.iterrows():
        grade_count[row['egoid']] += 1
        grade_sum[row['egoid']] += row['FinalGrade']

    for k, v in grade_sum.items():
        egos.append(int(k))
        averages.append(v / grade_count[k])

    return pd.DataFrame.from_dict({'egoid': egos, 'average': averages})


def main():
    grades = pd.read_csv("grades.csv")
    grades = grades.loc[grades['FinalGrade'].isin(LETTERGRADES.keys())]
    grades['FinalGrade'] = grades['FinalGrade'].apply(get_number_grade)

    ans = psql.sqldf('SELECT egoid, AVG(FinalGrade) as average_grade FROM grades GROUP BY egoid')
    manual_results = get_average_manually(grades)

    ans = ans.sort_values(by='egoid')
    manual_results = manual_results.sort_values(by='egoid')

    ans.to_csv('average_grades.csv', index=False)

if __name__ == "__main__":
    main()