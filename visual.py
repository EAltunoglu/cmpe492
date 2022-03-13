import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def main():
    average_grades = pd.read_csv('average_grades.csv')
    average_sleeps = pd.read_csv('average_sleeps.csv')

    ans = pd.merge(average_grades, average_sleeps, on=['egoid'])

    print(ans.head())

    xpoints = ans['sleep_score'].to_numpy()
    ypoints = ans['average_grade'].to_numpy()

    print(len(xpoints))
    print(len(ypoints))

    # plt.scatter(xpoints, ypoints)
    # plt.show()

    sns.pairplot(ans, hue='average_grade')

if __name__ == "__main__":
    main()