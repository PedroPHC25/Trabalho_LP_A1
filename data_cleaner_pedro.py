from df_concatenator import data

def select_columns(df, columns):
    selected_columns = df[columns]
    return selected_columns