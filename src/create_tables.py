def export_csv(df, filename, index_bool=False, header_bool=False):
    filepath = "../data/" + filename + ".csv"
    df.to_csv(filepath, index=index_bool, header=header_bool)
