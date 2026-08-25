import pandas as pd

# Carregar o dataset a partir do CSV
df = pd.read_csv('data/play_tennis.csv')
target_col = 'Jogar'
feature_cols = [col for col in df.columns if col != target_col]

def train_oner(df, target_col, feature_cols):
    best_feature = None
    best_error_count = float('inf')
    best_rules = {}
    feature_reports = {}

    for col in feature_cols:
        # Tabela de frequência entre a feature e o target
        ct = pd.crosstab(df[col], df[target_col])
        
        rules = {}
        total_errors = 0
        
        for val in ct.index:
            # Classe com maior ocorrência para este valor de atributo
            most_frequent_class = ct.loc[val].idxmax()
            rules[val] = most_frequent_class
            
            # Erros = total de amostras para o valor - amostras da classe mais frequente
            total_samples = ct.loc[val].sum()
            correct_samples = ct.loc[val, most_frequent_class]
            errors = total_samples - correct_samples
            total_errors += errors
            
        feature_reports[col] = {
            'rules': rules,
            'total_errors': total_errors,
            'error_rate': total_errors / len(df)
        }
        
        if total_errors < best_error_count:
            best_error_count = total_errors
            best_feature = col
            best_rules = rules

    return best_feature, best_rules, feature_reports

best_feature, best_rules, reports = train_oner(df, target_col, feature_cols)

print("=== RELATÓRIO DE ERROS POR ATRIBUTO (OneR) ===")
for feat, rep in reports.items():
    print(f"Atributo: {feat:12s} | Erros: {rep['total_errors']}/{len(df)} | Taxa de Erro: {rep['error_rate']:.2%}")
    for val, cls in rep['rules'].items():
        print(f"   SE {feat} = {val:10s} -> ENTÃO {target_col} = {cls}")
    print("-" * 50)

print(f"\n🏆 MELHOR ATRIBUTO SELECIONADO: {best_feature}")
print("Regras Finais do Modelo OneR:")
for val, cls in best_rules.items():
    print(f"  • SE {best_feature} = {val} ENTÃO {target_col} = {cls}")