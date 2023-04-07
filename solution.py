import pandas as pd
import numpy as np



chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = np.log(x)
    m = y.mean()
    sd = np.std(y)
    a = np.exp(m+(sd**2)/2)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return a # Ваш ответ
