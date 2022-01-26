import re
import pandas as pd
import numpy as np

def new_name(df):
    """función para que los nombres de las columnas no tengan valores raros"""
    new = []
    for col in df.columns:
        print(col)
        a = col.strip().lower()
        b = a.replace('.','_')
        c = b.replace(' ','_')
        print(c)
        new.append(c)    
    return new

def blanco(x): #funcion para capturar que tiburonres eran blancos y cuales no lo eran
    x = str(x)
    if re.search(r"[Ww](hite|HITE)",x):
        return "White shark"
    else:
        return "Other sharks"
