import pandas as pd
import numpy as np

# reading csv files
data_a1 = pd.read_csv('ch1_a.csv', delim_whitespace=True)
data_a2 = pd.read_csv('ch2_a.csv', delim_whitespace=True)
person = 'cl1'

# convert to df
df_a1 = pd.DataFrame(data_a1)
df_a2 = pd.DataFrame(data_a2)

# create channel column
n1 = len(df_a1)
channel1 = ['ch1'] * n1
n2 = len(df_a2)
channel2 = ['ch2'] * n2

# add column to df
df_a1['channel'] = channel1
df_a2['channel'] = channel2

# create lists
l_a = []
l_a1 = df_a1.values.tolist()
l_a2 = df_a2.values.tolist()

# delete values from lists
del_list = []
for i in range (len(l_a1)):
    if l_a1[i][8] != person:
        del_list.append(i)
count = 0
for i in del_list:
    l_a1.pop(i-count)
    count = count+1
n1 = n1 - len(del_list)

del_list.clear()
count = 0
for i in range (len(l_a2)):
    if l_a2[i][8] == person:
        del_list.append(i)
for i in del_list:
    l_a2.pop(i-count)
    count = count+1
n2 = n2 - len(del_list)

# create arrays
ar_a1 = np.array(l_a1)
ar_a2 = np.array(l_a2)

# init
i1 = i2 = 0
n = n1 + n2
check1 = check2 = 0

while (len(l_a) < n):
    # slice ar_a1
    if (check1 == 0):
        j1 = i1 + 1
        while (j1 < n1) and (l_a1[i1][0] == l_a1[j1][0]):
            j1 = j1 + 1
        if (j1 <= n1):
            t1 = ar_a1[i1:j1,:]
            t1 = t1.tolist()
            check1 = 1
        else:
            t1 = []
    
    # slice ar_a2
    if (check2 == 0):    
        j2 = i2 + 1
        while (j2 < n2) and (l_a2[i2][0] == l_a2[j2][0]):
            j2 = j2 + 1
        if (j2 <= n2):
            t2 = ar_a2[i2:j2,:]
            t2 = t2.tolist()
            check2 = 1
        else:
            t2 = []
    
    #merge
    if  (check2 == 0) or ((check1 == 1) and (l_a1[i1][0] <= l_a2[i2][0])):
        l_a = l_a + t1
        check1 = 0
        i1 = j1
    elif (check1 == 0) or ((check2 == 1) and (l_a2[i2][0] < l_a1[i1][0])):
        l_a = l_a + t2
        check2 = 0
        i2 = j2
    
df_a = pd.DataFrame(l_a)
df_a.columns = df_a1.columns
f = open('a_combine_cutClass.csv', 'w')
f.write('timestamp'.ljust(25) + 'colum1'.ljust(10) + 'colum2'.ljust(10) + 'colum3'.ljust(10) + 'colum4'.ljust(10) + 'colum5'.ljust(10) + 'colum6'.ljust(10) + 'colum7'.ljust(10) + 'colum8'.ljust(10) + 'channel'.ljust(15) + '\n') 

f.close()
for i in range(len(df_a)):
    with open('a_combine_cutClass.csv', 'a') as f:
        f.write(str(df_a.loc[i, 'timestamp']).ljust(25) + str(df_a.loc[i, 'colum1']).ljust(10) + str(df_a.loc[i, 'colum2']).ljust(10) + str(df_a.loc[i, 'colum3']).ljust(10) + str(df_a.loc[i, 'colum4']).ljust(10) + str(df_a.loc[i, 'colum5']).ljust(10) + str(df_a.loc[i, 'colum6']).ljust(10) + str(df_a.loc[i, 'colum7']).ljust(10) + str(df_a.loc[i, 'colum8']).ljust(10)+ str(df_a.loc[i, 'channel']).ljust(15) + '\n') 
