# Данные пользователя введенные в километрах.
# User data entered in kilometers.

ErrorInput = 'Enter data in kilometers (digital value)!\n\n'  # Введите данные в километрах (цыфровое значение)!

try:
    kilometers = float(input('Enter the distance in kilometers.\n'))  # Введите расстояние в километрах.
except:
    print(ErrorInput)
