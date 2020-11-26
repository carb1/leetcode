import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
table = pd.read_excel('./acc_run_time.xlsx')
table['table'] = table['morning'].apply(lambda x: x.split(' ')[2])
table['morning_time'] = table['morning'].apply(lambda x: x.split(' ')[3])
table['afternoon_time'] = table['afternoon'].apply(lambda x: x.split(' ')[3])
table = table[['table', 'morning_time', 'afternoon_time']]
table['morning_time'] = pd.to_datetime(table['morning_time'], format='%H:%M:%S.%f')
table['afternoon_time'] = pd.to_datetime(table['afternoon_time'], format='%H:%M:%S.%f')
table['time_sub'] = table['afternoon_time'] - table['morning_time']

run_date = table[table.index % 2 == 0]
print(run_date)

end_date = table[table.index % 2 == 1]
print(end_date)
