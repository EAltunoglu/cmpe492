import pandas as pd

def hour_to_timestamp(hms: str) -> int:
    hms = hms.split(':')
    return int(hms[0]) * 3600 + int(hms[1]) * 60 + int(hms[2])
    
def hour_to_timestamp_rotate_12_hours(hms: str) -> int:
    hms = hms.split(':')
    t = int(hms[0]) * 3600 + int(hms[1]) * 60 + int(hms[2]) + 3600 * 12
    if t >= 86400:
        t -= 86400
    return t


# def eff_to_int(eff: float) -> int:
#     return int(eff * 100)

def main():
    sleeps = pd.read_csv("../original_data/sleep_daily.csv")
    sleeps['timetobed'] = sleeps['timetobed'].apply(hour_to_timestamp_rotate_12_hours)
    sleeps['timeoutofbed'] = sleeps['timeoutofbed'].apply(hour_to_timestamp)
    # sleeps['Efficiency'] = sleeps['Efficiency'].apply(eff_to_int)

    sleeps = sleeps.sort_values(by='egoid')

    sleeps.to_csv('../refined_data/sleep/sleep_daily_timestamp.csv', index=False)

if __name__ == "__main__":
    main()