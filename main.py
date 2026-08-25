import pandas as pd
from src.oner import train_oner
from src.prism import prism

# Carregando dados
df = pd.read_csv('data/play_tennis.csv')
target = 'Jogar'
features = [col for col in df.columns if col != target]

# Executando OneR
best_feat, oner_rules, oner_errors = train_oner(df, target, features)
print(f"OneR - Melhor Feature: {best_feat} (Erros: {oner_errors})")

# Executando PRISM
prism_rules = prism(df, target, features)
print(f"PRISM - Regras geradas: {len(prism_rules)}")