import pandas as pd

column = ["Mariya", "Batman", "Spongebob"]
titled_columns = {"name": column, "height": [1.67, 2, 3], "weight": [12, 3, 2]}
data = pd.DataFrame(titled_columns)
select = data["weight"]
print(select)
