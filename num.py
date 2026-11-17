import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# array**=2
# print(array+[1,2,3,4]) 

# array1=np.array([[1,2,3,4]])
# array2=np.array([[1],[2],[3],[4]])
# print(array1.shape)
# print(array2.shape)
# print(array1*array2)



# array=np.array([[1,2,3,4],
#                 [2,4,5,7],
#                 [7,8,9,10]]) 
# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.max(array))
# print(np.min(array))
# print(np.var(array))
# print(np.argmin(array))
# print(np.argmax(array))
# print(np.sum(array,axis=0))
# print(np.sum(array,axis=1))
# x=array[array>5]
# print(x)
# y=array[array<=5]
# print(y)
# z=np.where(array>5,array,0)
# print(z)


# x=[2023,2024,2025,2026]
# y=[15,25,30,20]
# plt.plot(x,y,marker=".",
#              markersize=30,
#              markerfacecolor="cyan" ,
#              linestyle="dotted")
# plt.xlabel("year")
# plt.ylabel("value")
# plt.title("year vs value")
# plt.show()

# x=[1,2,3,4,5]
# y=[5,10,15,20,25]
# plt.grid()
# plt.plot(x,y)
# plt.show()

# category=["garins","vegetables","fruit","protein","dairy","sweets"]
# value=[4,5,2,5,3,7]
# plt.bar(category,value)
# plt.xlabel("category")
# plt.ylabel("vlaue")
# plt.show()

# categories=["freshman","junior","senior","sophomores"]
# numbers=np.array([300,250,275,155])
# colors=["red","yellow","blue","green"]
# plt.pie(numbers,labels=categories,autopct="%1f",colors=colors,explode=[0.2,0,0,0])
# plt.show()

# x=[0,1,5,4,2,3,5,2,7]
# y=[55,65,52,5,5,22,25,55,48]
# plt.xlabel("hours studied")
# plt.ylabel("grades")
# plt.scatter(x,y)
# plt.show()


# scores=np.random.normal(loc=80,scale=10,size=100)
# plt.hist(scores)
# plt.show()

df=pd.read_csv("students_data.csv")
# print(df)
# df=df.describe()
# print(df)
# df=df.dtypes
# print(df)
# df=df.shape
# print(df)
# df=df.dropna()
# print(df)
# df=df.dropna(subset={"marks","attendance","department"})
# print(df)
# df=df.dropna()
# df=df[(df["marks"]>=75)&(df["attendance"]>=80)]
# print(df)

# group=df.groupby("department")
# df=group["marks"].mean()
# print(df)

# group=df.groupby("department")
# df=group["marks"].max()
# print(df)

# df=df.dropna()
# group=df.groupby("department")
# df=group["attendance"].max()
# print(df)

# max_marks=df["marks"].max()
# df=df[df["marks"]==max_marks]
# print(df)

# max_marks=df["marks"].max()
# df=df[df["marks"]==max_marks]["department"]
# print(df)

# df=df.to_csv("cleaned.csv")
# print(df)
df=df.describe()
df.to_csv("cleaned.csv")





