import pandas as pd

class EnsaioRaw:
    def __init__(self,folder: str, unidade: str, n_ensaio: int):
        self.unidade = unidade
        self.n_ensaio = n_ensaio
        self.data = pd.read_csv(folder)
    
    def filtro_MM(self,M: int):
        
