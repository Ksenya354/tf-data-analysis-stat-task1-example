import pandas as pd
import numpy as np



chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = np.log(247+x)
    m = y.mean()
    sd = np.std(y)
    a = np.exp(m+(sd**2)/2)
    return a
