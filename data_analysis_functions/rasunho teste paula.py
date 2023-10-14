import pandas as pd
import doctest
# from analysis_management_beds import mean_by_management, median_by_management, std_by_management, unique_by_management


test_data = {"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"],
                     "LEITOS_SUS":[2, 3, 6, 4, 2, 4, 3, 1],
                     "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
df_test = pd.DataFrame(test_data, index = ["A", "B", "C", "D", "E", "F", "G", "H"]) 
        
# print("teste"
#       , mean_by_management(1, 1, 1))
df = 1[1["TP_GESTAO"] == "M"]
desvio_padrao = df["LEITOS_SUS"].std()

print(df)