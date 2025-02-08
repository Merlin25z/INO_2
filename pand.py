import pandas as pd

# Загружаем CSV файл в DataFrame
df = pd.read_csv('data1.csv')

# Просмотр первых строк для уверенности, что данные загружены корректно
print(df.head())

# Просмотр наименований столбцов
print(df.columns)

# Переименовываем столбцы для удобства
df.columns = ['datetime', 'atmospheric_pressure', 'rainfall', 'windspeed', 'wind_direction', 'surface_temperature', 'relative_humidity', 'solar_flux', 'battery']

# Проверим изменения
print(df.columns)

# Сохраняем первые 1000 строк в новый CSV файл
df.head(1000).to_csv('data_first_1000.csv', index=False)

# Загрузка сохранённого CSV файла
df_saved = pd.read_csv('data_first_1000.csv')

# Отображение первых 20 строк
print(df_saved.head(20))

# Отображение последних 20 строк
print(df_saved.tail(20))

# Пример среза (например, с 100-й по 120-ю строки)
print(df_saved.iloc[100:121])

# Теперь столбец называется 'relative_humidity'
column_name = 'relative_humidity'

# Проверим, сколько уникальных значений в этом столбце
unique_values = df[column_name].nunique()
print(f"Количество уникальных значений в столбце {column_name}: {unique_values}")



