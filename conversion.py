# Конвертация километров в мили.
# Converting kilometers to miles.

from data import kilometers

# Коэффициент конвертации километров в мили.
# The conversion rate of kilometers to miles.
conversion_factor = 0.621371


# Формула конвертации километров в мили.
# The formula for converting kilometers to miles.
def miles():
    m = kilometers * conversion_factor
    return m
