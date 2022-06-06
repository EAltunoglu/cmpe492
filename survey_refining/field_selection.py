import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
from dython.nominal import identify_nominal_columns


def prepare_survey():
    # todo:
    # drop the unattended persons
    # look at their number of answered questions
    pass


def select_fields(index):
    # todo: do not forget to add egoid

    education = pd.read_csv(
        '../original_data/survey_partial_2/survey_education_{}.csv'.format(index))

    # select rows for education
    education_select = ['hs', 'hssex', 'hsgrade', 'apexams',
                        'degreeintent', 'hrswork', 'ndfirst', 'majorevent']
    # education_drop = ['major1rc', 'major2rc']
    # education_refine = ['hsclub1rc', 'hsclub2rc', 'hsclub3rc', 'hsclub4rc', 'hsclub5rc']

    # refine education
    education_refined = education[[
        field + '_' + str(index) for field in education_select]].copy()

    # filter number of clubs attended
    education_refined['hsclubrc_{}'.format(index)] = education.apply(lambda row: 0 if pd.isna(row['hsclub3rc_{}'.format(index)])
                                                                     or pd.isnull(row['hsclub3rc_{}'.format(index)]) else 1, axis=1)

    # imputation for all of them, most frequent
    education_refined = education_refined.apply(
        lambda column: column.fillna(column.value_counts().index[0]))

    ###########################################################################################

    health = pd.read_csv(
        '../original_data/survey_partial_2/survey_health_{}.csv'.format(index))

    # select rows for health
    health_select = ['Dieting', 'PhysicalDisability']
    # health_drop = []
    # health_refine = []

    health_refined = health[[
        field + '_' + str(index) for field in health_select]].copy()

    # refine health
    # imputation for all of them, most frequent
    health_refined = health_refined.apply(
        lambda column: column.fillna(column.value_counts().index[0]))

    ###########################################################################################

    mental_health = pd.read_csv(
        '../original_data/survey_partial_2/survey_mental_health_{}.csv'.format(index))

    #  select rows for mental health
    mental_health_select = ['STAITraitTotal', 'CESDOverall',
                            'BAIsum', 'STAITraitGroup', 'CESDGroup', 'BAIgroup']
    # mental_health_drop = []  # many. use only the overall scores
    # mental_health_refine = []

    # refine mental health
    mental_health_refined = mental_health[[
        field + '_' + str(index) for field in mental_health_select]].copy()

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
    origin_select = ['gender_1', 'momdec_1', 'momusa_1', 'daddec_1', 'dadusa_1', 'parentstatus_1', 'dadage_1', 'momage_1',
                     'numsib_1', 'birthorder_1', 'parentincome_1', 'parenteduc_1', 'momrace_1', 'dadrace_1', 'momrelig_1', 'dadrelig_1', 'yourelig_1']
    # origin_drop = ['parentND_1', 'grandparentND_1', 'siblingND_1', 'uncleND_1', 'cousinND_1', 'otherrelativeND_1',
    #                'madaddec_1', 'madadusa_1', 'mamomdec_1', 'mamomusa_1', 'padaddec_1', 'padadusa_1', 'pamomdec_1', 'pamomusa_1',
    #                'yrdadborn_1', 'yrdaddec_1', 'yrmomborn_1', 'yrmomdec_1', 'numbros_1', 'numsis_1', 'adopted_1', 'momeduc_1', 'dadeduc_1',
    #                'momrace_AmInd_1', 'momrace_Asian_1', 'momrace_Black_1', 'momrace_Latino_1', 'momrace_Haw_1', 'momrace_White_1',
    #                'dadrace_AmInd_1', 'dadrace_Asian_1', 'dadrace_Black_1', 'dadrace_Latino_1', 'dadrace_Haw_1', 'dadrace_White_1',
    #                'dad_multiracial_1', 'mom_multiracial_1', 'parentrace_1']
    # origin_refine = []

    # refine origin
    origin_refined = origin[[field + '_' +
                             str(index) for field in origin_select]].copy()

    # momdec_1, momusa_1, daddec_1, dadusa_1 insert 0 if null
    origin_refined[['momdec_1', 'momusa_1', 'daddec_1', 'dadusa_1']] = origin_refined[[
        'momdec_1', 'momusa_1', 'daddec_1', 'dadusa_1']].fillna(value=0)

    # others will be filled with most frequent
    origin_refined.apply(
        lambda column: column.fillna(column.value_counts().index[0]))

    ###########################################################################################

    personal = pd.read_csv(
        '../original_data/survey_partial_2/survey_personal_{}.csv'.format(index))
    # select rows for personal info (self perception)
    personal_select = ['SelfEsteem_1', 'Trust_1', 'SRQE_Ext_1', 'SRQE_Introj_1', 'SRQE_Ident_1', 'SRQE_Intrin_1',
                       'selsa_rom_1', 'selsa_fam_1', 'selsa_soc_1', 'SelfEff_exercise_scale_1', 'SelfEff_diet_scale_1', 'selfreg_scale_1']
    # many. use only the overall scores. exception: SRQE_RAI_1 is score of scores
    # personal_drop = []
    # personal_refine = []

    # refine personal info (self perception)
    personal_refined = personal[[field + '_' +
                                 str(index) for field in personal_select]]
    # fill all of them with means
    personal_refined.fillna(personal_refined.mean())

    ###########################################################################################

    sleep = pd.read_csv(
        '../original_data/survey_partial_2/survey_sleep_{}.csv'.format(index))

    # select rows for sleep
    sleep_select = ['PSQI_duration_1', 'PSQIGlobal_1',
                    'PSQIGroup_1', 'MEQTotal_1', 'MEQGroup_1']
    # sleep_drop = []  # many. use only the overall scores
    # sleep_refine = []

    # refine sleep
    sleep_refined = sleep[[field + '-' + str(index) for field in sleep_select]]

    # numeric (mean): PSQI_duration_1, PSQIGlobal_1, MEQTotal_1
    sleep_refined.fillna(sleep_refined.mean())

    # categorical (most frequent): PSQIGroup_1, MEQGroup_1
    sleep_refined.apply(lambda column: column.fillna(
        column.value_counts().index[0]))

    ###########################################################################################

    # do not use sexual orientation info

    ###########################################################################################

    # do not use big5 as their score is in personality inventory

    ###########################################################################################

    # use all rows for personality inventory
    personality_inv = pd.read_csv(
        '../original_data/survey_partial_2/survey_personalit_inv_{}.csv'.format(index))

    # fill with mean if there is any missing value
    personality_inv_refined = personality_inv.copy()
    personality_inv_refined.fillna(personality_inv_refined.mean())

    ###########################################################################################

    # use all rows for bad habits
    bad_habits = pd.read_csv(
        '../original_data/survey_partial_2/survey_bad_habits_{}.csv'.format(index))

    bad_habits_refined = bad_habits.copy()

    # fill with most frequent. all values are categorical
    bad_habits_refined.apply(lambda column: column.fillna(
        column.value_counts().index[0]))

    ###########################################################################################

    # use all rows for exercise
    # fill with most frequent. all values are categorical

    exercise = pd.read_csv(
        '../original_data/survey_partial_2/survey_exercise_{}.csv'.format(index))

    exercise_refined = exercise.copy()

    # fill with most frequent. all values are categorical
    exercise_refined.apply(lambda column: column.fillna(
        column.value_counts().index[0]))

    ###########################################################################################

    ego_id = exercise['egoid'].copy()

    # put the result into a file


select_fields(1)
