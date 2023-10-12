# subdata = select_columns(data, ["REGIAO", "LEITOS_EXISTENTES"])
# subdata = reset_index(subdata)
# subdata = not_necessary_columns(subdata, "CNES")
# subdata = group_and_sum(subdata, ["COMP", "REGIAO"], "LEITOS_EXISTENTES")
# subdata = date_conversor(subdata, "COMP", "%Y%m")

# subdata.reset_index(inplace = True)
# subdata.drop("CNES", axis = 1, inplace = True)
# subdata = subdata.groupby(["COMP"])["LEITOS_EXISTENTES"].sum().reset_index()
# subdata["COMP"] = pd.to_datetime(subdata["COMP"], format = "%Y%m")

# data_centrooeste = subdata[subdata["REGIAO"] == "CENTRO-OESTE"]
# data_nordeste = subdata[subdata["REGIAO"] == "NORDESTE"]
# data_norte = subdata[subdata["REGIAO"] == "NORTE"]
# data_sudeste = subdata[subdata["REGIAO"] == "SUDESTE"]
# data_sul = subdata[subdata["REGIAO"] == "SUL"]

# plt.figure(figsize = (15, 5))
# plt.plot(subdata["COMP"], subdata["LEITOS_EXISTENTES"])
# plt.show()