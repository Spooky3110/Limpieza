import pandas as pd

df = pd.read_csv("ventas_desordenadas.csv")

print(df.head(10))
print(df.info())
print(df.describe())

#print(df[df.duplicated(keep=False)])
#print(df.isnull().sum())
#print(df["ciudad"].value_counts(dropna=False))
#print(df[df["precio_unitario"] < 0])
#print(df[df["cantidad"] <= 0]) 

print("Antes:", len(df))

df = df.drop_duplicates()

print("Después:", len(df))

print(df.isnull().sum())

df["ciudad"] = df["ciudad"].str.strip().str.title()

print(df["ciudad"].value_counts(dropna=False))

df["ciudad"] = df["ciudad"].replace({
    "Cordoba": "Córdoba"
})

precios_negativos = df[df["precio_unitario"] < 0]

print(precios_negativos)

# Crear columna para documentar problemas
df["observaciones"] = ""

# Identificar precios negativos
df.loc[
    df["precio_unitario"] < 0,
    "observaciones"
] = "Verificar precio con factura"

df.loc[
    df["cantidad"] <= 0,
    "observaciones"
] = "Verificar cantidad con registro de ventas"

print(df["categoria"].value_counts(dropna=False))

# Eliminar espacios y pasar todo a minúsculas
df["categoria"] = df["categoria"].str.strip().str.lower()

# Unificar los nombres
categorias = {
    "tecnología": "Tecnología",
    "periféricos": "Periféricos",
    "accesorios": "Accesorios",
    "audio": "Audio",
    "muebles": "Muebles",
    "electrónica": "Electrónica"
}

df["categoria"] = df["categoria"].map(categorias)

# Mostrar resultados
print(df["categoria"].value_counts(dropna=False))
print(df["categoria"].unique())

print(df["fecha"].value_counts(dropna=False))
print(df["fecha"].dtype)

# Convertir fechas a formato datetime
df["fecha"] = pd.to_datetime(
    df["fecha"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

# Comprobar resultados
print(df["fecha"].head(15))
print(df["fecha"].dtype)
print("Fechas nulas:", df["fecha"].isnull().sum())

print(df[df["fecha"].isnull()])
df.loc[df["fecha"].isnull(), "observaciones"] = (
    df.loc[df["fecha"].isnull(), "observaciones"]
    .fillna("") 
    + "Fecha faltante. Verificar registro original."
)

print(df["ciudad"].value_counts(dropna=False))
# Limpiar espacios
df["ciudad"] = df["ciudad"].str.strip()

# Normalizar mayúsculas y minúsculas
df["ciudad"] = df["ciudad"].str.title()

# Comprobar
print(df["ciudad"].value_counts(dropna=False))

df.loc[df["ciudad"].isnull(), "observaciones"] += (
    " Ciudad faltante. Verificar registro original."
)

print(df[["cantidad", "precio_unitario"]].describe())

print("Cantidades nulas:", df["cantidad"].isnull().sum())
print("Precios nulos:", df["precio_unitario"].isnull().sum())

print("Cantidades inválidas:")
print(df[df["cantidad"] <= 0])

print("Precios negativos:")
print(df[df["precio_unitario"] < 0])

df["estado_revision"] = "Correcto"

df.loc[df["cantidad"] <= 0, "estado_revision"] = "Revisar cantidad"

df.loc[df["precio_unitario"] < 0, "estado_revision"] = "Revisar precio"

df.loc[df["cantidad"].isnull(), "estado_revision"] = "Cantidad faltante"

print(df[["id_venta", "estado_revision"]])

print(df["medio_pago"].value_counts(dropna=False))
# Limpiar espacios y pasar a minúsculas
df["medio_pago"] = df["medio_pago"].str.strip().str.lower()

# Unificar nombres
df["medio_pago"] = df["medio_pago"].replace({
    "efectivo": "Efectivo",
    "tarjeta": "Tarjeta",
    "transferencia": "Transferencia",
    "crédito": "Crédito"
})

# Comprobar
print(df["medio_pago"].value_counts(dropna=False))

# RESUMEN GENERAL DE CALIDAD DE DATOS

print("Cantidad de filas y columnas:")
print(df.shape)

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nFilas duplicadas:")
print(df.duplicated().sum())

print("\nTipos de datos:")
print(df.dtypes)

print("\nResumen estadístico:")
print(df.describe())

#df.to_csv("ventas_limpias.csv", index=False, encoding="utf-8-sig")