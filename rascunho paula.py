import pandas as pd
import doctest
from graphs_functions import graph_bar_management_beds as gbm
# from analysis_management_beds import mean_by_management, median_by_management, std_by_management, unique_by_management

print("a")
test_data = {"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"],
                     "LEITOS_SUS":[2, 3, 6, 4, 2, 4, 3, 1],
                     "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
df_test = pd.DataFrame(test_data, index = ["A", "B", "C", "D", "E", "F", "G", "H"]) 


gbm.replacement(df_test, "TP_GESTAO", "M", "municipal")
gbm.replacement(df_test, "TP_GESTAO", "E", "Estadual")
gbm.replacement(df_test, "TP_GESTAO", "D", "Dupla gestão")
print(df_test)


gbm.graph_bar(df_test, "TP_GESTAO", "LEITOS_SUS")
print("a")