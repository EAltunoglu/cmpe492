import pandas as pd


def select_fields(index):
    education = pd.read_csv(
        '../original_data/survey_partial_2/survey_education_{}.csv'.format(index))

    # select rows for education
    education_select = ['egoid', 'hs', 'hssex', 'hsgrade', 'apexams',
                        'degreeintent', 'hrswork', 'ndfirst', 'majorevent']
    # education_drop = ['major1rc', 'major2rc']
    # education_refine = ['hsclub1rc', 'hsclub2rc', 'hsclub3rc', 'hsclub4rc', 'hsclub5rc']

    add = ['egoid']

    for field in education_select:
        if f'{field}_{index}' in education.columns:
            add.append(f'{field}_{index}')

    # refine education
    education_refined = education[add].copy()
    # education_refined = education_refined.dropna(axis=0, thresh=2)

    # filter number of clubs attended
    try:
        education_refined['hsclubrc_{}'.format(index)] = education.apply(lambda row: 0 if pd.isna(row['hsclub3rc_{}'.format(index)])
                                                                        or pd.isnull(row['hsclub3rc_{}'.format(index)]) else 1, axis=1)
    except:
        # education_refined['hsclubrc_{}'.format(index)] = education.apply(lambda row: 0)
        pass
    # imputation for all of them, most frequent
    # print(index)
    # print(education_refined)
    education_refined = education_refined.apply(
        lambda column: column.fillna(column.value_counts().index[0]))

    ###########################################################################################

    health = pd.read_csv(
        '../original_data/survey_partial_2/survey_health_{}.csv'.format(index))

    # select rows for health
    health_select = ['egoid', 'Dieting', 'PhysicalDisability']
    # health_drop = []
    # health_refine = []

    add = ['egoid']

    for field in health_select:
        if f'{field}_{index}' in health.columns:
            add.append(f'{field}_{index}')

    health_refined = health[add].copy()
    # health_refined = health_refined.dropna(axis=0, thresh=2)

    # refine health
    # imputation for all of them, most frequent
    health_refined = health_refined.apply(
        lambda column: column.fillna(column.value_counts().index[0]))

    ###########################################################################################

    mental_health = pd.read_csv(
        '../original_data/survey_partial_2/survey_mental_health_{}.csv'.format(index))

    #  select rows for mental health
    mental_health_select = ['egoid', 'STAITraitTotal', 'CESDOverall',
                            'BAIsum', 'STAITraitGroup', 'CESDGroup', 'BAIgroup']
    # mental_health_drop = []  # many. use only the overall scores
    # mental_health_refine = []

    add = ['egoid']

    for field in mental_health_select:
        if f'{field}_{index}' in mental_health.columns:
            add.append(f'{field}_{index}')

    # refine mental health
    mental_health_refined = mental_health[add].copy()
    # mental_health_refined = mental_health_refined.dropna(axis=0, thresh=2)

    # STAITraitTotal_1, CESDOverall_1, BAIsum_1 are numeric; STAITraitGroup_1, CESDGroup_1, BAIgroup_1 are categorical
    # imputation: mean for numerics, most frequent for categoricals
    mental_health_refined = mental_health_refined.fillna(
        mental_health_refined.mean())
    mental_health_refined = mental_health_refined.apply(
        lambda column: column.fillna(column.value_counts().index[0]))

    ###########################################################################################

    origin = pd.read_csv(
        '../original_data/survey_partial_2/survey_origin_{}.csv'.format(index))
    #  select rows for origin
    origin_select = ['egoid', 'gender', 'momdec', 'momusa', 'daddec', 'dadusa', 'parentstatus', 'dadage', 'momage',
                     'numsib', 'birthorder', 'parentincome', 'parenteduc', 'momrace', 'dadrace', 'momrelig', 'dadrelig', 'yourelig']
    # origin_drop = ['parentND', 'grandparentND', 'siblingND', 'uncleND', 'cousinND', 'otherrelativeND',
    #                'madaddec', 'madadusa', 'mamomdec', 'mamomusa', 'padaddec', 'padadusa', 'pamomdec', 'pamomusa',
    #                'yrdadborn', 'yrdaddec', 'yrmomborn', 'yrmomdec', 'numbros', 'numsis', 'adopted', 'momeduc', 'dadeduc',
    #                'momrace_AmInd', 'momrace_Asian', 'momrace_Black', 'momrace_Latino', 'momrace_Haw', 'momrace_White',
    #                'dadrace_AmInd', 'dadrace_Asian', 'dadrace_Black', 'dadrace_Latino', 'dadrace_Haw', 'dadrace_White',
    #                'dad_multiracial', 'mom_multiracial', 'parentrace']
    # origin_refine = []

    # refine origin
    add = ['egoid']
    for field in origin_select:
        if f'{field}_{index}' in origin.columns:
            add.append(f'{field}_{index}')

    origin_refined = origin[add].copy()
    # origin_refined = origin_refined.dropna(axis=0, thresh=2)

    fill_zero = [f'momdec_{index}', f'momusa_{index}', f'daddec_{index}', f'dadusa_{index}']

    for zero_col in fill_zero:
        try:
            origin_refined[zero_col] = origin_refined[zero_col].fillna(0)
        except:
            pass

    # momdec, momusa, daddec, dadusa insert 0 if null
    # origin_refined[fill_zero] = origin_refined[
    # fill_zero].fillna(value=0)

    # others will be filled with most frequent
    origin_refined = origin_refined.apply(
        lambda column: column.fillna(column.value_counts().index[0]))

    ###########################################################################################

    personal = pd.read_csv(
        '../original_data/survey_partial_2/survey_personal_{}.csv'.format(index))
    # select rows for personal info (self perception)
    personal_select = ['egoid', 'SelfEsteem', 'Trust', 'SRQE_Ext', 'SRQE_Introj', 'SRQE_Ident', 'SRQE_Intrin',
                       'selsa_rom', 'selsa_fam', 'selsa_soc', 'SelfEff_exercise_scale', 'SelfEff_diet_scale', 'selfreg_scale']
    # many. use only the overall scores. exception: SRQE_RAI_1 is score of scores
    # personal_drop = []
    # personal_refine = []

    add = ['egoid']

    for field in personal_select:
        if f'{field}_{index}' in personal.columns:
            add.append(f'{field}_{index}')

    # refine personal info (self perception)
    personal_refined = personal[add]
    # personal_refined = personal_refined.dropna(axis=0, thresh=2)
    # fill all of them with means
    personal_refined.fillna(personal_refined.mean(), inplace=True)

    ###########################################################################################

    sleep = pd.read_csv(
        '../original_data/survey_partial_2/survey_sleep_{}.csv'.format(index))

    # select rows for sleep
    sleep_select = ['egoid', 'PSQI_duration', 'PSQIGlobal',
                    'PSQIGroup', 'MEQTotal', 'MEQGroup']
    # sleep_drop = []  # many. use only the overall scores
    # sleep_refine = []

    add = ['egoid']

    for field in sleep_select:
        if f'{field}_{index}' in sleep.columns:
            add.append(f'{field}_{index}')

    # refine sleep
    sleep_refined = sleep[add]
    # sleep_refined = sleep_refined.dropna(axis=0, thresh=2)

    # numeric (mean): PSQI_duration_1, PSQIGlobal_1, MEQTotal_1
    sleep_refined.fillna(sleep_refined.mean(), inplace=True)

    # categorical (most frequent): PSQIGroup_1, MEQGroup_1
    sleep_refined = sleep_refined.apply(lambda column: column.fillna(
        column.value_counts().index[0]))

    ###########################################################################################

    # do not use sexual orientation info

    ###########################################################################################

    # do not use big5 as their score is in personality inventory

    ###########################################################################################

    # use all rows for personality inventory
    personality_inv = pd.read_csv(
        '../original_data/survey_partial_2/survey_personality_inv_{}.csv'.format(index))
    # personality_inv = personality_inv.dropna(axis=0, thresh=2)

    # fill with mean if there is any missing value
    personality_inv_refined = personality_inv.copy()
    personality_inv_refined.fillna(personality_inv_refined.mean(), inplace=True)

    ###########################################################################################

    # use all rows for bad habits
    bad_habits = pd.read_csv(
        '../original_data/survey_partial_2/survey_bad_habits_{}.csv'.format(index))
    # bad_habits = bad_habits.dropna(axis=0, thresh=2)

    bad_habits_refined = bad_habits.copy()

    # fill with most frequent. all values are categorical
    bad_habits_refined = bad_habits_refined.apply(lambda column: column.fillna(
        column.value_counts().index[0]))

    ###########################################################################################

    # use all rows for exercise
    # fill with most frequent. all values are categorical

    exercise = pd.read_csv(
        '../original_data/survey_partial_2/survey_exercise_{}.csv'.format(index))
    # exercise = exercise.dropna(axis=0, thresh=2)

    exercise_refined = exercise.copy()

    # fill with most frequent. all values are categorical
    exercise_refined = exercise_refined.apply(lambda column: column.fillna(
        column.value_counts().index[0]))

    ###########################################################################################

    # put the result into a file

    education_refined.to_csv('../refined_data/survey_education_{}.csv'.format(index), index=False)
    origin_refined.to_csv('../refined_data/survey_origin_{}.csv'.format(index), index=False)
    personal_refined.to_csv('../refined_data/survey_personal_{}.csv'.format(index), index=False)
    sleep_refined.to_csv('../refined_data/survey_sleep_{}.csv'.format(index), index=False)
    personality_inv_refined.to_csv('../refined_data/survey_personality_inv_{}.csv'.format(index), index=False)
    bad_habits_refined.to_csv('../refined_data/survey_bad_habits_{}.csv'.format(index), index=False)
    exercise_refined.to_csv('../refined_data/survey_exercise_{}.csv'.format(index), index=False)

    ###########################################################################################

    # join all the dataframes

    m1 = pd.merge(education_refined, origin_refined, on='egoid', how='outer')
    m1 = pd.merge(m1, personal_refined, on='egoid', how='outer')
    m1 = pd.merge(m1, sleep_refined, on='egoid', how='outer')
    m1 = pd.merge(m1, personality_inv_refined, on='egoid', how='outer')
    m1 = pd.merge(m1, bad_habits_refined, on='egoid', how='outer')
    m1 = pd.merge(m1, exercise_refined, on='egoid', how='outer')


    m1.to_csv('../refined_data/survey_all_{}.csv'.format(index), index=False)

    
    

for i in range(1, 9):
    select_fields(i)
