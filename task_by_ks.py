
import pandas as pd
df = pd.read_csv (r'C:\Users\Kishor Kore\Desktop\pandas\sample_file.csv')
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

dic=df.to_dict()
for i in dic:
    for j in range(len((dic[i]))):
        if dic[i][j]=="Job ID":
            print(dic[i])