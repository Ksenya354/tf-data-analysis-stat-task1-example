import pandas as pd
import numpy as np



chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = np.log(x-247)
    m = y.mean()
    return m
