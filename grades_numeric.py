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


def main():
    grades = pd.read_csv("grades.csv")
    grades = grades.loc[grades['FinalGrade'].isin(LETTERGRADES.keys())]
    grades['FinalGrade'] = grades['FinalGrade'].apply(get_number_grade)

    ans = psql.sqldf('SELECT egoid, FinalGrade as grade, CourseReferenceNumber FROM grades GROUP BY egoid, CourseReferenceNumber')

    ans = ans.sort_values(by='egoid')

    ans.to_csv('grades_numeric.csv', index=False)

if __name__ == "__main__":
    main()