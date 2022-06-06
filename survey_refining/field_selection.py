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
    # select rows for education
    education_select = ['hs_1', 'hssex_1', 'hsgrade_1', 'apexams_1', 'degreeintent_1', 'hrswork_1', 'ndfirst_1', 'majorevent_1']
    education_drop = ['major1rc_1', 'major2rc_1']
    education_refine = ['hsclub1rc_1', 'hsclub2rc_1', 'hsclub3rc_1', 'hsclub4rc_1', 'hsclub5rc_1']

    # refine education
    # todo: imputation for all of them, most frequent
    # todo: filter number of clubs attended


    # select rows for health
    health_select = ['Dieting_1', 'PhysicalDisability_1']
    health_drop = []
    health_refine = []


    # refine health
    # todo: imputation for all of them, most frequent


    #  select rows for mental health
    mental_health_select = ['STAITraitTotal_1', 'CESDOverall_1', 'BAIsum_1', 'STAITraitGroup_1', 'CESDGroup_1', 'BAIgroup_1']
    mental_health_drop = [] # many. use only the overall scores
    mental_health_refine = []

    # refine mental health

    # STAITraitTotal_1, CESDOverall_1, BAIsum_1 are numeric; STAITraitGroup_1, CESDGroup_1, BAIgroup_1 are categorical
    # todo: imputation: knn for numerics, most frequent for categoricals


    #  select rows for origin
    origin_select = ['gender_1', 'momdec_1', 'momusa_1', 'daddec_1', 'dadusa_1', 'parentstatus_1', 'dadage_1', 'momage_1',
        'numsib_1', 'birthorder_1', 'parentincome_1', 'parenteduc_1', 'momrace_1', 'dadrace_1', 'momrelig_1', 'dadrelig_1', 'yourelig_1']
    origin_drop = ['parentND_1', 'grandparentND_1', 'siblingND_1', 'uncleND_1', 'cousinND_1', 'otherrelativeND_1',
        'madaddec_1', 'madadusa_1', 'mamomdec_1', 'mamomusa_1', 'padaddec_1', 'padadusa_1', 'pamomdec_1', 'pamomusa_1',
        'yrdadborn_1', 'yrdaddec_1', 'yrmomborn_1', 'yrmomdec_1', 'numbros_1', 'numsis_1', 'adopted_1', 'momeduc_1', 'dadeduc_1',
        'momrace_AmInd_1', 'momrace_Asian_1', 'momrace_Black_1', 'momrace_Latino_1', 'momrace_Haw_1', 'momrace_White_1',
        'dadrace_AmInd_1', 'dadrace_Asian_1', 'dadrace_Black_1', 'dadrace_Latino_1', 'dadrace_Haw_1', 'dadrace_White_1',
        'dad_multiracial_1', 'mom_multiracial_1', 'parentrace_1']
    origin_refine = []

    # refine origin

    # momdec_1, momusa_1, daddec_1, dadusa_1 insert 0 if null
    # others will be filled with most frequent


    # select rows for personal info (self perception)
    personal_select = ['SelfEsteem_1', 'Trust_1', 'SRQE_Ext_1', 'SRQE_Introj_1', 'SRQE_Ident_1', 'SRQE_Intrin_1',
        'selsa_rom_1', 'selsa_fam_1', 'selsa_soc_1', 'SelfEff_exercise_scale_1', 'SelfEff_diet_scale_1', 'selfreg_scale_1']
    personal_drop = [] # many. use only the overall scores. exception: SRQE_RAI_1 is score of scores
    personal_refine = []

    # refine personal info (self perception)
    # fill all of them with means


    # select rows for sleep
    sleep_select = ['PSQI_duration_1', 'PSQIGlobal_1', 'PSQIGroup_1', 'MEQTotal_1', 'MEQGroup_1']
    sleep_drop = [] # many. use only the overall scores
    sleep_refine = []

    # refine sleep

    # numeric (mean): PSQI_duration_1, PSQIGlobal_1, MEQTotal_1
    # categorical (most frequent): PSQIGroup_1, MEQGroup_1


    # do not use sexual orientation info

    # do not use big5 as their score is in personality inventory


    # use all rows for personality inventory
    # fill with mean if there is any missing value


    # use all rows for bad habits
    # fill with most frequent. all values are categorical


    # use all rows for exercise
    # fill with most frequent. all values are categorical


    # put the result into a file