import pandas as pd
import numpy as np
import os

# set-up
dir = ""
origins = os.listdir(dir)
origins.sort()

no = 0

l_merge = []
time = []
i = 0

for origin in origins:
    # read csv & convert to df
    data = pd.read_csv("inp/" + origin, delim_whitespace=True)
    df = pd.DataFrame(data)

    # create id column
    n = len(df)
    id = [no] * n
    df["id"] = id
    no = no + 1

    # convert to list
    l_df = df.values.tolist()

    # insert row
    for j in range(len(l_df)):
        # check if needs delete old
        current = l_df[j][0]
        if (current in time) and (len(l_merge) > 0):
            for k in range(len(l_merge)):
                if l_merge[k][0] == current:
                    if (l_merge[k][9] == -1) or (l_merge[k][9] == l_df[j][9]):
                        break
                    elif l_merge[k][9] < l_df[j][9]:
                        # print('catch ' + current + ' in ' + str(l_df[j][9]))
                        l_merge[k][9] = -1
        else:
            time.append(l_df[j][0])
        # insert new
        l_merge.append([])
        for k in range(10):
            l_merge[i].append(l_df[j][k])
        i = i + 1

df_merge = pd.DataFrame(l_merge, columns=df.columns)
f = open("d_combine.csv", "w")
f.write(
    "timestamp".ljust(25)
    + "object_id".ljust(15)
    + "colum2".ljust(10)
    + "colum3".ljust(10)
    + "colum4".ljust(10)
    + "colum5".ljust(10)
    + "colum6".ljust(10)
    + "colum7".ljust(10)
    + "colum8".ljust(10)
    + "\n"
)

f.close()
for i in range(len(df_merge)):
    with open("d_combine.csv", "a") as f:
        if df_merge.loc[i, "id"] > -1:
            f.write(
                str(df_merge.loc[i, "timestamp"]).ljust(25)
                + str(df_merge.loc[i, "object_id"]).ljust(15)
                + str(df_merge.loc[i, "colum2"]).ljust(10)
                + str(df_merge.loc[i, "colum3"]).ljust(10)
                + str(df_merge.loc[i, "colum4"]).ljust(10)
                + str(df_merge.loc[i, "colum5"]).ljust(10)
                + str(df_merge.loc[i, "colum6"]).ljust(10)
                + str(df_merge.loc[i, "colum7"]).ljust(10)
                + str(df_merge.loc[i, "colum8"]).ljust(10)
                + "\n"
            )
