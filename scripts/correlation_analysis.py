import pandas as pd
import math

def multiple_sum(x: pd.Series, y: pd.Series, n: int):
    return sum(x[i]*y[i] for i in range(n))

def var(x: pd.Series, n: int):
    return multiple_sum(x,x,n) - sum(x)*sum(x)/n

def corr_analysis(x: pd.Series, y: pd.Series):
    if x.size != y.size:
        raise ValueError('Should be same length')
    
    n = x.size
    ans = (multiple_sum(x,y,n) - sum(x)*sum(y)/n) / math.sqrt(var(x,n)*var(y,n))
    
    assert ans >= -1
    assert ans <= 1

    return ans

# sleep_grade = pd.read_csv('../sleep_grade_data/sleep_grade_2.csv')
# corr_analysis(sleep_grade['minsasleep'], sleep_grade['grade'])