import pandas as pd

melbourne_file_path = "C:/Users/oneul/OneDrive/바탕 화면/Programing/csv/melb_data.csv"

melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.columns)

# melbourne_data.describe()
print(melbourne_data.describe())

#You can pull out a variable with dot-notation. This single column is stored in a Series, which is broadly like a DataFrame with only a single column of data. # select one column set -> <variable name>.<column name>
y = melbourne_data.Rooms
print(y)

#The columns that are inputted into our model (and later used to make predictions) are called "features." In our case, those would be the columns used to determine the home price. 
# Sometimes, you will use all columns except the target as features. Other times you'll be better off with fewer features.
# melbourne_data라는 데이터프레임에서 melbourne_features라는 리스트에 포함된 열(columns)만을 선택하여 새로운 데이터프레임을 생성
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
f = melbourne_data[melbourne_features]
print(f.describe())