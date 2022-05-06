import pandas as pd
# from  scripts.displot.displot import display_displot
def display_displot(data: pd.DataFrame):
    import seaborn as sns

    for index, column in enumerate(data.columns):
        if index > 1 and not (column == 'egoid' or column == 'dataDate' or column == 'datadate'):
            sns.displot(data, x=column)


def test_normality(data: pd.DataFrame):
    from scipy import stats

    alpha = 1e-3
    normal_items = []
    non_normal_items = []
    for index, column in enumerate(data.columns):
        if not (column == 'egoid' or column == 'dataDate' or column == 'datadate'):
            if index < 3 or True:
                k2, p = stats.normaltest(data[column], nan_policy='omit')
                if p < alpha:
                    # print(type())
                    print(column, 'is normal with p', p, 'and k', k2)
                    normal_items.append(column)
                else:
                    print(column, 'is not normal with p', p, 'and k', k2)
                    non_normal_items.append(column)
    print('non_normal_items', non_normal_items)
    data.filter(items=non_normal_items, axis='columns')

def anova(data: pd.DataFrame, label: pd.DataFrame):
    # TODO
    pass

def corr_matrixt_analyze(data: pd.DataFrame, drop=False):
    import seaborn as sns

    corr_matrix = data.corr()
    value_matrix = corr_matrix.values

    for i in range(value_matrix.shape[0]):
        for j in range(i+1, value_matrix.shape[0]):
            if value_matrix[i,j] > 0.7:
                print(corr_matrix.columns[i], '\t\t', corr_matrix.columns[j], '\t\t', value_matrix[i,j])
    
    if drop:
        # TODO: drop mostly correlated columns automatically. manual option is more efficient
        print('Drop them manually.')

    sns.heatmap(corr_matrix, annot=False, center=0)

def pca_bulk(data: pd.DataFrame):
    import numpy as np
    from numpy.linalg import eig

    normalized_data = (data-data.mean())/data.std()

    cov_matrix = normalized_data.cov()

    print('Covariance matrix:')
    print(cov_matrix)
    print()


    us_egnvalues, us_egnvectors = eig(cov_matrix)

    total_egnvalues = sum(us_egnvalues)

    cov_dict = {}
    for index, column in enumerate(data.columns):
        cov_dict[column] = us_egnvalues[index]
        print(us_egnvalues[index], '\t', column)

    eig_vector_row = np.transpose(us_egnvectors)
    cum_var = []
    step_var = []
    _index = 0
    for column, egn_val in sorted(cov_dict.items(), key = lambda kv:(kv[1],kv[0]), reverse=True):
        step_var.append(egn_val/total_egnvalues)
        if _index > 0:
            cum_var.append(egn_val/total_egnvalues + cum_var[_index - 1])
        else:
            cum_var.append(egn_val/total_egnvalues)
        _index += 1

    print('Total of eigenvalues:')
    print(total_egnvalues)
    print()

    print('Cumulative variance:')
    print(cum_var)
    print()

    import matplotlib.pyplot as plt

    x_labels = [column for column in cov_dict.keys()]

    plt.plot(x_labels, step_var, marker='o', markersize=6, color='skyblue', linewidth=2, label='Proportion of variance')
    plt.plot(x_labels, cum_var, marker='o', color='orange', linewidth=2, label="Cumulative variance")
    plt.legend()
    plt.title('Screen plot')
    plt.xlabel('Principal components')
    plt.ylabel('Proportion of variance')
    plt.show()





