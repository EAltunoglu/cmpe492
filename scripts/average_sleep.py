import pandas as pd
import pandasql as psql

def main():
    sleeps = pd.read_csv("sleep.csv")
    average_sleeps = psql.sqldf(
        '''
        SELECT
            egoid,
            AVG(bedtimedur) as bedtimedur,
            AVG(minstofallasleep) as minstofallasleep,
            AVG(minsafterwakeup) as minsafterwakeup,
            AVG(minsasleep) as minasleep,
            AVG(minsawake) as minsawake,
            AVG(Efficiency*100) as efficiency
        FROM sleeps
        GROUP BY egoid
        '''
    )

    weighted_average_sleeps = psql.sqldf(
        '''
        SELECT
            *,
            SUM(minasleep*efficiency) / SUM(minasleep) as weighted_efficiency,
            AVG(minasleep*efficiency) as sleep_score
        FROM average_sleeps
        GROUP BY egoid
        '''
    )

    weighted_average_sleeps = weighted_average_sleeps.sort_values(by='egoid')
    weighted_average_sleeps.to_csv('average_sleeps.csv', index=False)

if __name__ == "__main__":
    main()