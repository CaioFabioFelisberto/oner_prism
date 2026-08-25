import pandas as pd

df = pd.read_csv('data/play_tennis.csv')
target_col = 'Jogar'
feature_cols = [col for col in df.columns if col != target_col]

def prism(df, target_col, feature_cols):
    rules = []
    classes = df[target_col].unique()
    
    for cls in classes:
        df_subset = df.copy()
        
        while len(df_subset[df_subset[target_col] == cls]) > 0:
            current_subset = df_subset.copy()
            current_features = feature_cols.copy()
            rule_conditions = {}
            
            # Constrói regras refinadas termo a termo
            while len(current_subset[current_subset[target_col] != cls]) > 0 and len(current_features) > 0:
                best_feature, best_value = None, None
                best_precision, best_coverage = -1.0, 0
                
                for feat in current_features:
                    for val in current_subset[feat].unique():
                        sub = current_subset[current_subset[feat] == val]
                        if len(sub) == 0:
                            continue
                        
                        precision = len(sub[sub[target_col] == cls]) / len(sub)
                        coverage = len(sub[sub[target_col] == cls])
                        
                        if precision > best_precision or (precision == best_precision and coverage > best_coverage):
                            best_precision, best_coverage = precision, coverage
                            best_feature, best_value = feat, val
                
                if best_feature is None:
                    break
                    
                rule_conditions[best_feature] = best_value
                current_subset = current_subset[current_subset[best_feature] == best_value]
                current_features.remove(best_feature)
            
            rules.append((rule_conditions, cls, best_precision))
            
            # Remoção dos exemplos já cobertos (Estratégia Separate)
            matched_indices = df_subset.index
            for feat, val in rule_conditions.items():
                matched_indices = matched_indices[df_subset.loc[matched_indices, feat] == val]
            
            df_subset = df_subset.drop(index=matched_indices)
            
    return rules

rules = prism(df, target_col, feature_cols)

print("=== REGRAS PRISM ===")
for conds, cls, prec in rules:
    cond_str = " E ".join([f"{k} = {v}" for k, v in conds.items()])
    print(f"SE {cond_str} ENTÃO {target_col} = {cls} (Precisão: {prec:.0%})")