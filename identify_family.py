import pandas as pd
import numpy as np
import sys
import csv


df = pd.read_csv("family.csv")
families = df["family"].unique()
df_family = {}
for family in families:
    indices = [i for i, x in enumerate(df["family"]) if x == family]
    df_family[family] = indices


threshold = 0.001

query_file = open(sys.argv[1],'r')
Lines = query_file.readlines()
query_names = []
for i in range(len(Lines)):
    if i%4==0:
        query_names.append(Lines[i].strip())

summary_array = {}
for query in query_names:
    summary_array[query]=[]

count = 0 #G000307305.fq_DB__SAMN02604089_32_mer_counts_dumps.fa
for species in df["speciesID"]:
    result_file = "search_result/"+sys.argv[1].split("/")[1]+"_DB__"+species+"_32_mer_counts_dumps.fa.csv"
    df2 = pd.read_csv(result_file)
    for query in query_names:
        if query in list(df2["Query_read_id"]):
            i=df2[df2["Query_read_id"]==query]
            #print("==>",str(float(i["match (normalized)"])))
            summary_array[query].append(float(i["match (normalized)"]))
            '''
            if float(i["jaccard"]) >= threshold:
                summary_array[query].append(1)
            else :
                summary_array[query].append(0)
            '''
        else :
            summary_array[query].append(0.0)
        
    count +=1 

#print(summary_array)
f_out = open("family_out.csv",'w')
f_out.write("query_read_id ")
for family in families:
    f_out.write(str(family)+" ")
f_out.write("\n")
'''
for key, value in summary_array.items():
    f_out.write(key+",")
    for val in value[:-1]:
        f_out.write(str(val)+",")
    f_out.write(str(value[-1])+"\n")
f_out.close()
'''
for key in summary_array:
    f_out.write(key+" ")
    for family in families:
        flag = 1
        for idx in df_family[family]:
            if summary_array[key][idx] == 0:
                flag = 0
        if flag == 1:
            f_out.write(str(1)+" ")
        else:
            f_out.write(str(0)+" ")
    f_out.write("\n")
