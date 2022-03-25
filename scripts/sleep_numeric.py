import pandas as pd

def hour_to_timestamp(hms: str) -> int:
    try:
        hms = hms.split(':')
        return int(hms[0]) * 3600 + int(hms[1]) * 60 + int(hms[2])
    except:
        return hms

def eff_to_int(eff: float) -> int:
    return int(eff * 100)

def main():
    sleeps = pd.read_csv("../original_data/sleep.csv")
    sleeps['timetobed'] = sleeps['timetobed'].apply(hour_to_timestamp)
    sleeps['timeoutofbed'] = sleeps['timeoutofbed'].apply(hour_to_timestamp)
    sleeps['Efficiency'] = sleeps['Efficiency'].apply(eff_to_int)

    sleeps = sleeps.sort_values(by='egoid')

    sleeps.to_csv('../original_data/sleep_timestamp_eff.csv', index=False)

if __name__ == "__main__":
    main()