"""
Carga un dataset de series temporales y calcula tendencias.
"""
import pandas as pd

datos = pd.date_range(start="2023-01-01", periods=365, freq='D')
serie = pd.Series(np.random.randn(365).cumsum(), index=datos)

serie.plot(title="Tendencia de la Serie Temporal")
