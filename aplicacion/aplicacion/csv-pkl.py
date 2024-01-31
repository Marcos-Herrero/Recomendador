from pathlib import Path
import csv
import pickle
import pandas as pd

df_preferences = pd.read_csv(open(r'aplicacion\aplicacion\historial_input\preferences_1706297704.7207527.csv', 'rb'))
df_stock = pd.read_csv(open(r'aplicacion\aplicacion\historial_input\stock_1706297704.7207527.csv', 'rb'))
df_sales = pd.read_csv(open(r'aplicacion\aplicacion\historial_input\sales_1706297704.7207527.csv', 'rb'))

df_preferences.to_pickle(r'aplicacion\aplicacion\datos\preferences_df_limpio_I.pickle')  
df_stock.to_pickle(r'aplicacion\aplicacion\datos\data_stock_limpio_I.pickle')
df_sales.to_pickle(r'aplicacion\aplicacion\datos\data_ov_limpio_I.pickle')
"""
with open(r'aplicacion\aplicacion\historial_input\preferences_1706297704.7207527.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f.to_dataframe())
    pickle.dump(list(reader), open(r'aplicacion\aplicacion\datos\preferences_df_limpio_I.pickle', 'wb'))

with open(r'aplicacion\aplicacion\historial_input\stock_1706297704.7207527.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    pickle.dump(list(reader), open(r'aplicacion\aplicacion\datos\data_stock_limpio_I.pickle', 'wb'))

with open(r'aplicacion\aplicacion\historial_input\sales_1706297704.7207527.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    pickle.dump(list(reader), open(r'aplicacion\aplicacion\datos\data_ov_limpio_I.pickle', 'wb'))
    """