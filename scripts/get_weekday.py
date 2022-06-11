import datetime
import pandas as pd

def get_weekday(date: str):
    return datetime.datetime.strptime(date,"%Y-%m-%d").weekday()

def main():
    activity = pd.read_csv("../refined_data/activity/activity_knn.csv")
    activity['weekday'] = activity['datadate'].apply(get_weekday)

if __name__ == "__main__":
    main()