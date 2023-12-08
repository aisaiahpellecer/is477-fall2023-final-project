from ydata_profiling import ProfileReport
import pandas as pd
import os

path = "data/wine/"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)

columns = [
    'Class',
    'Alcohol',
    'Malicacid',
    'Ash',
    'Alcalinity_of_ash',
    'Magnesium',
    'Total_phenols',
    'Flavanoids',
    'Nonflavanoid_phenols',
    'Proanthocyanins',
    'Color_intensity',
    'Hue',
    'OD280/OD315_of_diluted wines',
    'Proline'
]

df_wine = pd.read_csv(os.path.join(path,'wine.data'), names=columns,
                              sep=',', engine='python')

profile_path = "profiling/"
isExist = os.path.exists(profile_path)
if not isExist:
    os.makedirs(profile_path)


profile = ProfileReport(df_wine, title="Profiling Report")
profile.to_file(os.path.join(profile_path,'report.html'))
