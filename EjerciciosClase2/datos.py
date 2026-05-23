from pathlib import Path
import pandas as pd

excel_path = Path(
    r"C:\Users\MIGUEL SAAVEDRA\Documents\framework_Qa\BigData-and-Business\tabla\rutaTablaclase2.xlsx"
)

df = pd.read_excel(excel_path)
print(df)

print("--------------------------------------------------")
df=pd.read_excel(excel_path, sheet_name="Hoja2")
print(df)

print("--------------------------------------------------")
df=pd.read_excel(excel_path, sheet_name="Hoja3", header=None, names=["Nombre", "Cantidad", "ES_FBK","Año"])
print(df)