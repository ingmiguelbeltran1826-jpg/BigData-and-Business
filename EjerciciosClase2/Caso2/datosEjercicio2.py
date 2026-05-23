from pathlib import Path
import pandas as pd

csv_path = Path(
    r"C:\Users\MIGUEL SAAVEDRA\Documents\framework_Qa\BigData-and-Business\EjerciciosClase2\Caso2\datos_rrss_t1(1).csv"
)

df = pd.read_csv(csv_path)
print(df)

print("--------------------------------------------------")

csv_path2 = Path(
    r"C:\Users\MIGUEL SAAVEDRA\Documents\framework_Qa\BigData-and-Business\EjerciciosClase2\Caso2\datos_rrss_t2(1).csv"
)
df2 = pd.read_csv(csv_path2, sep=";")
print(df2)

print("--------------------------------------------------")

csv_path3 = Path(
    r"C:\Users\MIGUEL SAAVEDRA\Documents\framework_Qa\BigData-and-Business\EjerciciosClase2\Caso2\datos_rrss_t3(1).csv"
)
df3 = pd.read_csv(csv_path3, header=None, names=["Nombre", "Cantidad", "ES_FBK","Año"])
print(df3)