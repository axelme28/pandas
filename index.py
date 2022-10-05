import pandas as pd

# json array of data
data = {
    "data": [
        {
            "id": "b130",
            "name": "Jack",
            "last_name": "Sparrow",
            "age": 35,
        },
        {
            "id": "b125",
            "name": "John",
            "last_name": "Doe",
            "age": 25,
        },
        {
            "id": "b126",
            "name": "Jane",
            "last_name": "Doe",
            "age": 23,
        },
        {
            "id": "b127",
            "name": "Peter",
            "last_name": "Doe",
            "age": 27,
        },
        {
            "id": "b128",
            "name": "Mary",
            "last_name": "Doe",
            "age": 21,
        },
        {
            "id": "b129",
            "name": "Oliver",
            "last_name": "Twist",
            "age": 19,
        },
        
    ]
}

## Read the data xlsx file
df = pd.read_excel("/content/example.xlsx")
## delete the - from the ID items in the data
df["ID"] = df["ID"].str.replace("-", "")

## convert the json to a data frame and change the column names
df2 = pd.DataFrame(data["data"])
df2.columns = ["ID", "NOMBRE", "APELLIDO", "EDAD"]

## fill the data frame with the data from the data frame 2 and the data frame 1 with the same ID
df3 =df.join(df2.set_index("ID"), on="ID", how="left", lsuffix='_left', rsuffix='_right')
## DELETE THE COLUMNS THAT ARE NOT NEEDED
df3 = df3.drop(['NOMBRE_left', 'APELLIDO_left', 'EDAD_left'], axis=1)

## save the data frame to a new excel file
df3.to_excel("example2.xlsx", index=False)

## save the data frame to a new excel file
df4.to_excel("example3.xlsx", index=False)

## print the data frame
print(df3)
print(df4)