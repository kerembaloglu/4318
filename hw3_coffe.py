import pandas as pd
import numpy as np

coffe = pd.read_csv("data4318.txt",sep = ";")
     
print(coffe.groupby(["Company","Payment"])["Quantity"].sum())

        
        
        

