import pandas as pd
import numpy as np

#array creation and manipulation
x = np.arange(10, 50)
reshaped_data = x.reshape(5, 8)
df = pd.DataFrame(reshaped_data)
print(df)

#extract  elements from the second to fourth row and third to sixth column
subset= df.iloc[1:4, 2:6]
print(subset)

random_operation = np.random.randint(0, 111, (3, 3))
df = pd.DataFrame(random_operation,columns = ["A", "B", "C"])
print("DataFrame:\n", df)
print("\n Mean :\n" ,df.mean())
print("\n median :\n" ,df.median())
print("\n standard deviation :\n" ,df.std())

data = {"name" : ["john", "anna", "peter", "linda"], "age" : [28, 24, 35, 32], "city" : ["New York", "paris", "berlin", "London"]}
df = pd.DataFrame(data)  #sort the data in 2d array form
print("first two rows :\n" ,df.head(2)) 
print("\n last two rows:\n", df.tail(2))
df["salary"] = [7000, 8000, 120000, 110000]

# a) filter individuals older than 30
older_than_30 = df[df["age"] > 30]
print("\n Individuals older than 30:\n", older_than_30)

#b) calculate average age and  salary 
average_age = df["age"].mean()
average_salary = df["salary"].mean()
print(f"\nAverage age : {average_age : .2f}")
print(f"Average salary : {average_salary:.2f}")

#c) sort by age in descending order
age_sort = df.sort_values(by = "age", ascending=False)
print("\nDataFrame sorted by age (Descending Order) :\n", age_sort)








