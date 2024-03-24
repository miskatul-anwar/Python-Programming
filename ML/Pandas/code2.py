import pandas as pd

list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
titled_column = {"Day": list}
data = pd.DataFrame(titled_column)
print(data)
