import pandas as pd

def hour_to_timestamp(hms: str) -> int:
    try:
        hms = hms.split(':')
        return int(hms[0]) * 3600 + int(hms[1]) * 60 + int(hms[2])
    except:
        return hms

def main():
    sleeps = pd.read_csv("original_data/sleep.csv")
    print(sleeps.head())
    sleeps['timetobed'] = sleeps['timetobed'].apply(hour_to_timestamp)
    sleeps['timeoutofbed'] = sleeps['timeoutofbed'].apply(hour_to_timestamp)
    sleeps = sleeps.sort_values(by='egoid')

    sleeps.to_csv('original_data/sleep_timestamp.csv', index=False)

if __name__ == "__main__":
    main()