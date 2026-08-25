import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.preprocessing import OrdinalEncoder

# 1. Carregar dataset
df = pd.read_csv('data/play_tennis.csv')
X = df.drop(columns=['Jogar'])
y = df['Jogar']

# 2. Codificar variáveis categóricas (Scikit-learn exige números)
encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X)

# 3. Treinar a Árvore de Decisão
dt = DecisionTreeClassifier(criterion='entropy', random_state=42)
dt.fit(X_encoded, y)

# 4. Imprimir a estrutura em texto da árvore
tree_rules = export_text(dt, feature_names=list(X.columns))
print("=== ÁRVORE DE DECISÃO (Estrutura Hierárquica) ===")
print(tree_rules)

# 5. Gerar imagem visual da Árvore
plt.figure(figsize=(10, 6))
plot_tree(dt, feature_names=X.columns, class_names=dt.classes_, filled=True, rounded=True)
plt.title("Árvore de Decisão — Play Tennis")
plt.tight_layout()
plt.savefig("data/decision_tree.png")