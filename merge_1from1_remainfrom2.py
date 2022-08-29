import pandas as pd
import numpy as np

# reading csv files
data_a1 = pd.read_csv('ch1_summary.csv', delim_whitespace=True)
data_a2 = pd.read_csv('ch2_summary.csv', delim_whitespace=True)
person = 'cl1'

# convert to df
df_a1 = pd.DataFrame(data_a1)
df_a2 = pd.DataFrame(data_a2)
n1 = len(df_a1)
n2 = len(df_a2)

# create lists
l_a = []
l_a1 = df_a1.values.tolist()
l_a2 = df_a2.values.tolist()

i = i1 = i2 = 0

while (i1 != n1) and (i2 != n2):
    # if single
    if (i1 == n1) or (i2 == n2) or (l_a1[i1][0] != l_a2[i2][0]):
        if (i2 == n2) or (l_a1[i1][0] < l_a2[i2][0]):
            i1 = i1 + 1
        else:
            i2 = i2 + 1
    # if double
    else:    
        l_a.append([])
        
        # set timestamp
        l_a[i].append(l_a1[i1][0])
        
        # set col 1
        l_a[i].append(l_a1[i1][1])

        # set col 2 to 6
        for j in range(2,7):
            l_a[i].append(l_a2[i2][j])

        i1 = i1 + 1
        i2 = i2 + 1
    
    i = i + 1
    
df_a = pd.DataFrame(l_a)
df_a.columns = df_a1.columns
f = open('merge_1from1_remainfrom2.csv', 'w')
f.write('timestamp'.ljust(25) + 'col1'.ljust(10) + 'col2'.ljust(10) + 'col3'.ljust(10) + 'col4'.ljust(10) + 'col5'.ljust(10) + 'col6'.ljust(10) + '\n') 

f.close()
for i in range(len(df_a)):
    with open('merge_1from1_remainfrom2.csv', 'a') as f:
        f.write(str(df_a.loc[i, 'timestamp']).ljust(25) + str(df_a.loc[i, 'col1']).ljust(10) + str(df_a.loc[i, 'col2']).ljust(10) + str(df_a.loc[i, 'col3']).ljust(10) + str(df_a.loc[i, 'col4']).ljust(10) + str(df_a.loc[i, 'col5']).ljust(10) + str(df_a.loc[i, 'col6']).ljust(10) + '\n') 
