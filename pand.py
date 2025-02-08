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

