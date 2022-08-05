
# import pandas as pd
# df = pd.read_csv (r'C:\Users\Kishor Kore\Desktop\pandas\sample_file.csv')
# row_number=df[df[df.columns[0]]=='Job ID'].index
# from_job_id=row_number[0]

# row_number=df[df[df.columns[0]]=='Database server Info'].index
# to_describe_info=row_number[0]

# all_data=df.iloc[from_job_id:to_describe_info]
# print(all_data)

# all_data.to_excel('C:\\Users\\Kishor Kore\\Desktop\\pandas\\master1_excel.xlsx',index=False)





# import pandas as pd

# data = pd.read_csv(r'C:\Users\Kishor Kore\Desktop\pandas\Sorted Fields RCE.txt',delimiter = "\t")
# print(data[[data.columns[1]]])

# ss=data[[data.columns[1]]].transpose()
# ss.to_excel('C:\\Users\\Kishor Kore\\Desktop\\pandas\\upper.xlsx',index=False)

# # print(ss)

# import pandas as pd
# l=[]
# with open(r'C:\Users\Kishor Kore\Desktop\pandas\Sorted Fields RCE.txt') as f:
#     s=(f.readlines())
# for i in s:
#     if i is not None:
#         l.append(i)

# df =pd.DataFrame(l)
# ss=df.t()
 

# import pandas as pd
# df = pd.read_csv (r'C:\Users\Kishor Kore\Desktop\pandas\sample_file.csv')
# all_data=df.filter(regex='Job ID', axis=1)

# row_number=df[df[df.columns[0]]=='Job ID'].index
# from_job_id=row_number[0]

# row_number=df[df[df.columns[0]]=='Database server Info'].index
# to_describe_info=row_number[0]

# all_data=df.iloc[from_job_id:to_describe_info]
# print("---------------------------------",all_data)

# dic=df.to_dict()
# for i in dic:
#     for j in range(len((dic[i]))):
#         if dic[i][j]=="Job ID":
#             print(dic[i])

# from xml.etree.ElementTree import indent
# import pandas as pd

# d1={"A":[1,1,1],"B":[2,2,2],"C":[3,3,3]}
# d2={"A":[6,6,6],"B":[5,5,5],"C":[4,4,4]}
# d3={"A":[7,7,7],"B":[8,8,8],"C":[9,9,9]}

# df1=pd.DataFrame(d1)
# df2=pd.DataFrame(d2)
# df3=pd.DataFrame(d3)

# # print(df1)
# # print(df2)
# # print(df2)
# af=[df1,df2,df3]
# ss=pd.concat(af,ignore_index=True)
# print(ss)


# from operator import index
# import pandas as pd
# df = pd.read_csv (r'C:\Users\Kishor Kore\Desktop\pandas\sample_file.csv')
 
# from_job=df.loc[df[df[df.columns[0]]=='Job ID'].index[0]:df[df[df.columns[0]]=='Database server Info'].index[0]]
# data=from_job.rename(columns={ k:v for (k,v) in zip((df.columns[0:11]),df.iloc[df[df[df.columns[0]]=='Job ID'].index[0]])})

# # new_list=list(filter(lambda x: list(data.columns)[x]== "Media Agent" or list(data.columns)[x]== "BackupSet" or list(data.columns)[x]== "Backup Type" , range(len(list(data.columns)))))
# new_list=['Media Agent','BackupSet','Backup Type']
# data.drop(new_list,axis=1,inplace=True)


# # new_list=list(filter(lambda x: list(data.columns)[x]== "Media Agent" or list(data.columns)[x]== "BackupSet" or list(data.columns)[x]== "Backup Type" , range(len(list(data.columns)))))
 




# from_job=df.loc[df[df[df.columns[0]]=='Job ID'].index[0]:df[df[df.columns[0]]=='Databases in SQL Server and Sybase Backup Jobs'].index[0]-1]

# from operator import index



import pandas as pd
 
df = pd.read_csv (r'C:\Users\Kishor Kore\Downloads\daily_failed_report.csv')
from_to=df[df.columns[0]]=='Job ID'.index[0]
till_to=df[df[df.columns[0]]=='Databases in SQL Server and Sybase Backup Jobs'].index[0]-1

from_job=df.loc[df[from_to:till_to]]
data=from_job.rename(columns={ k:v for (k,v) in zip((df.columns[0:11]),df.iloc[df[df[df.columns[0]]=='Job ID'].index[0]])})
 
l2=[]
for ind in range(4,data.index.stop):
    for j in range(ind+1,data.index.stop):
        if data['Server'][ind]==data['Server'][j] and  data['Subclient'][ind]==data['Subclient'][j] and data['Agent'][ind]==data['Agent'][j]:
                l2.append(ind)

    if data['Job status'][ind]=="Delayed" and (data['Failure Reason'][ind]=="The number of running Synthetic Full jobs has exceeded the limit"  or data['Failure Reason'][ind]=="Number of active streams for running jobs reaches the limit" or  pd.isnull(data.at[ind,'Failure Reason'])):
        l2.append(ind)

    if data['Job status'][ind]=="Completed" and pd.isnull(data.at[ind,'Failure Reason']):
        l2.append(ind)

    if data['Job status'][ind]=="Completed with errors" and (data['Failure Reason'][ind]=="Another Backup is already running" or data['Agent'][ind]=="SharePoint server"):
        l2.append(ind)
        
    if data['Agent'][ind]=="Virtual Server" and data['Failure Reason'][ind]=="Failed to enable changed block tracking ":
        l2.append(ind)
 
l3=set(l2)
l2=list(l3)
new_df=data.drop(l2)
new_df.to_excel('C:\\Users\\Kishor Kore\\Desktop\\pandas\\master7_excel.xlsx',index=False)
 



# import pandas as pd
 
# df = pd.read_csv (r'C:\Users\Kishor Kore\Downloads\daily_failed_report.csv')
# from_to=df[df[df.columns[0]]=='Job ID'].index[0]
# till_to=df[df[df.columns[0]]=='Databases in SQL Server and Sybase Backup Jobs'].index[0]-1

# from_job=df.loc[ from_to:till_to]

# data=from_job.rename(columns={ k:v for (k,v) in zip((df.columns[0:11]),df.iloc[df[df[df.columns[0]]=='Job ID'].index[0]])})
 
# l1=data[data['Job status'].str.contains("Delayed", na=False)].index
# l2=data[data['Failure Reason'].str.contains("The number of running Synthetic Full jobs has exceeded the limit", na=False)].index
# l3=data[data['Failure Reason'].str.contains("Number of active streams for running jobs reaches the limit", na=False)].index
 
# l4=data['Failure Reason'].isnull().index

# print( (l4))


# l2=[]
# for ind in range(4,data.index.stop):
#     for j in range(ind+1,data.index.stop):
#         if data['Server'][ind]==data['Server'][j] and  data['Subclient'][ind]==data['Subclient'][j] and data['Agent'][ind]==data['Agent'][j]:
#                 l2.append(ind)

#     if data['Job status'][ind]=="Delayed" and (data['Failure Reason'][ind]=="The number of running Synthetic Full jobs has exceeded the limit"  or data['Failure Reason'][ind]=="Number of active streams for running jobs reaches the limit" or  pd.isnull(data.at[ind,'Failure Reason'])):
#         l2.append(ind)

#     if data['Job status'][ind]=="Completed" and pd.isnull(data.at[ind,'Failure Reason']):
#         l2.append(ind)

#     if data['Job status'][ind]=="Completed with errors" and (data['Failure Reason'][ind]=="Another Backup is already running" or data['Agent'][ind]=="SharePoint server"):
#         l2.append(ind)
        
#     if data['Agent'][ind]=="Virtual Server" and data['Failure Reason'][ind]=="Failed to enable changed block tracking ":
#         l2.append(ind)
 
# l3=set(l2)
# l2=list(l3)

 
 