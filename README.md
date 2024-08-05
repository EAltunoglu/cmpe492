[Academic Performance Relation with Behavioral Trends and
Personal Characteristics: Wearable Device Perspective](https://www.researchgate.net/profile/Berrenur-Saylam/publication/366977067_Academic_Performance_Relation_with_Behavioral_Trends_and_Personal_Characteristics_Wearable_Device_Perspective/links/63bc753d097c7832caa1ff35/Academic-Performance-Relation-with-Behavioral-Trends-and-Personal-Characteristics-Wearable-Device-Perspective.pdf)
# Cmpe492

## Survey's feature selection and imputation

We noticed that people tend not to answer many questions in a subgroup if they do not answer some of them. So, we decided not to use knn. Instead we filled with mean and most frequent values, which works independendet from other features.


### Education: 
* Information about people's majors are dropped. High school club activities is simplifed such that it indicates the person registered at least 3 clubs or not

### Health:
* We dropped weight and height, kept dieting status and existance of disability 

### Mental Health:
* We used the ones that indicate overall results. Namely ```['STAITraitTotal', 'CESDOverall', 'BAIsum', 'STAITraitGroup', 'CESDGroup', 'BAIgroup']```

### Origin:
* Selected features ```['gender', 'momdec', 'momusa', 'daddec', 'dadusa', 'parentstatus', 'dadage', 'momage', 'numsib', 'birthorder', 'parentincome', 'parenteduc', 'momrace', 'dadrace', 'momrelig', 'dadrelig', 'yourelig']```
* We dropped others beacuse they can be obtained from the remaining data or the overall score is enough for us. For example, number of siblings is enough, so, we dropped number or brothers and sisters

### Personal:
* Selected result values: ```['egoid', 'SelfEsteem', 'Trust', 'SRQE_Ext', 'SRQE_Introj', 'SRQE_Ident', 'SRQE_Intrin', 'selsa_rom', 'selsa_fam', 'selsa_soc', 'SelfEff_exercise_scale', 'SelfEff_diet_scale', 'selfreg_scale']```

### Sleep:
* Selected result values: ```['egoid', 'PSQI_duration', 'PSQIGlobal', 'PSQIGroup', 'MEQTotal', 'MEQGroup']```

### Sex:
* Did not use sexual oritentation data

### Big5:
* Personality inventory includes final result. Dropped all of them

### Personality Inventory:
* Used all 5 features

### Bad Habits:
* Used all features, categoric information such as dring 2-3 times a week

