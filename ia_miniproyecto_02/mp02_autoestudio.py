import pandas as pd

# 1) Mediana robusta ante outliers (espera 3)
print("Mediana de [1,2,100,3,4]:", pd.Series([1,2,100,3,4]).median())

# 2) Mini-docs: primeras líneas de docstrings útiles
def show_doc(title, obj, n=12):
    print(f"\n{title} (primeras {n} líneas):")
    doc = (obj.__doc__ or "").splitlines()
    print("\n".join(doc[:n]))

show_doc("drop_duplicates", pd.DataFrame.drop_duplicates)
show_doc("fillna", pd.DataFrame.fillna)
show_doc("quantile", pd.Series.quantile)
