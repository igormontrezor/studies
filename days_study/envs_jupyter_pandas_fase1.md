# 📚 Diário de Estudos - Python Financeiro

## 📅 10-03-2026 | 🎯 Jupyter Lab + Pandas

---

## 📖 Resumo
- **Duração:** 8 horas
- **Conteúdo:** Jupyter Lab, magic commands, pandas básico, matplotlib
- **Fontes:**
  - Jupyter: https://www.youtube.com/watch?v=HW29067qVWk
  - Pandas: https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS

---

## 🎯 Aprendizados Principais

### **📝 Resumo Conceitual**

#### **Jupyter Lab**
- Ambiente web para executar código e ver resultados imediatos
- Magic commands: `%` (linha) e `%%` (célula)
- Ativação: `cd 'c:\Projects Python\envs\data_scientist_1'Scripts\activate` depois `cd 'c:\Projects Python\projects\data_scientist_1\notebook'` e `jupyter lab`

#### **Pandas**
- DataFrames são contêineres de Series
- Series são objetos de DataFrame
- Manipulação e análise de dados
- Integração com matplotlib para visualização

---

## 🐍 Criando Ambientes Virtuais

### **Passo a Passo Completo**

1. **Criar ambiente virtual:**
   ```bash
   python -m venv nome-do-venv
   ```

2. **Ativar ambiente virtual:**
   ```bash
   cd nome-do-venv
   Scripts\activate
   ```

3. **Instalar pacotes necessários:**
   ```bash
   pip install jupyter ipykernel matplotlib pandas
   ```

4. **⭐ REGISTRAR KERNEL DO JUPYTER (OBRIGATÓRIO):**
   ```bash
   python -m ipykernel install --user --name=nome-do-kernel --display-name="Python (nome-do-kernel)"
   ```

5. **Iniciar Jupyter Lab:**
   ```bash
   cd pasta-dos-notebooks
   jupyter lab
   ```

### **Importante:**
- **Todo ambiente virtual que for usar com Jupyter precisa ter um kernel registrado!**
- Criar venv **não** cria kernel automaticamente
- Sem kernel registrado, o Jupyter não encontrará os pacotes do ambiente

### **📝 Resumo Conceitual**

#### **Ambientes Virtuais**
- Isolam dependências por projeto
- Evitam conflitos entre versões
- Facilitam reprodução de resultados
- Podem ser compartilhados via requirements.txt

#### **Tipos de Environments**
- **Conda**: Gerenciador de pacotes e environments
- **venv**: Nativo do Python, mais leve
- **virtualenv**: Similar ao venv com mais recursos

### **🛠️ Comandos Práticos**

#### **Criar Environment**
```bash
# Conda
conda create -n meu_projeto python=3.14

# venv
python -m venv meu_projeto_env
```

#### **Criar Notebook pelo Shell**
```bash
# Criar notebook vazio
echo '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}' > notebook_novo.ipynb

# Criar notebook com célula básica
echo '{"cells": [{"cell_type": "code", "execution_count": null, "metadata": {}, "outputs": [], "source": ["# Novo Notebook\n\nimport pandas as pd\nimport matplotlib.pyplot as plt\n"]}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}' > notebook_com_celula.ipynb
```

#### **Gerenciar Environments**
```bash
# Listar (conda)
conda env list

# Ativar (conda)
conda activate meu_projeto

# Ativar (venv - Windows)
meu_projeto_env\Scripts\activate

# Desativar
conda deactivate
```

#### **Dependências**
```bash
# Instalar pacotes
pip install pandas numpy matplotlib

# Salvar dependências
pip freeze > requirements.txt

# Instalar de requirements
pip install -r requirements.txt
```

---

### **📋 Jupyter Lab Essencial**

#### **🚀 Iniciar e Navegar**
```bash
# Iniciar Jupyter Lab
jupyter lab

# Iniciar em diretório específico
jupyter lab --notebook-dir="C:/Projects Python/studies"

# Listar kernels disponíveis
jupyter kernelspec list

# Instalar novo kernel
python -m ipykernel install --user --name=meu_env --display-name="Python (meu_env)"
```

#### **⚡ Magic Commands**
```python
# Magic commands úteis
%lsmagic                    # Listar todos os magic commands
%pwd                        # Diretório atual
%ls                         # Listar arquivos
%cd pasta                   # Mudar diretório
%run script.py              # Executar script Python
%load script.py             # Carregar script na célula
%time                       # Medir tempo de execução
%%time                      # Medir tempo da célula inteira
%who                        # Listar variáveis
%whos                       # Listar variáveis com detalhes
```

#### **🔧 Atalhos e Dicas**
```python
# Atalhos úteis (modo Command)
# Esc: entrar em modo Command
# A: inserir célula acima
# B: inserir célula abaixo
# D+D: deletar célula
# M: mudar para Markdown
# Y: mudar para Code
# Shift+Enter: executar célula
# Ctrl+Enter: executar sem avançar

# Instalar pacotes dentro do notebook
!pip install pandas numpy plotly

# Ver informações do sistema
!python --version
!pip list
```

---

### **📊 Pandas Essencial**

#### **📁 Importar e Criar Dados**
```python
import pandas as pd
import numpy as np

# Importar CSV
df = pd.read_csv('arquivo.csv')

# Importar Excel
df = pd.read_excel('arquivo.xlsx')

# Criar DataFrame do zero
df = pd.DataFrame({
    'coluna1': [1, 2, 3],
    'coluna2': ['A', 'B', 'C']
})

# Criar Series
s = pd.Series([1, 2, 3, 4, 5])
```

#### **👀 Explorar Dados**
```python
# Ver primeiras linhas
df.head()
df.head(10)

# Ver últimas linhas
df.tail()

# Informações gerais
df.info()
df.describe()

# Dimensões
df.shape
df.columns
df.dtypes

# Ver valores únicos
df['coluna'].unique()
df['coluna'].nunique()
df['coluna'].value_counts()
```

#### **🔍 Selecionar e Filtrar**
```python
# Selecionar coluna
df['coluna']
df.coluna

# Selecionar múltiplas colunas
df[['coluna1', 'coluna2']]

# Selecionar por índice
df.iloc[0]        # Primeira linha
df.iloc[0:5]      # Primeiras 5 linhas
df.loc[0]         # Por label

# Filtrar condições
df[df['coluna'] > 10]
df[df['coluna'] == 'valor']
df[(df['col1'] > 10) & (df['col2'] == 'A')]

# Usar .query()
df.query('coluna > 10 and coluna2 == "A"')
```

#### **✏️ Modificar Dados**
```python
# Criar nova coluna
df['nova_coluna'] = df['coluna1'] * 2

# Aplicar função
df['nova'] = df['coluna'].apply(lambda x: x * 2)

# Renomear colunas
df.rename(columns={'velho': 'novo'})

# Remover coluna
df.drop('coluna', axis=1)
df.drop(columns=['col1', 'col2'])

# Remover linhas
df.drop(0)                    # Por índice
df.drop_duplicates()          # Remover duplicatas
```

#### **📊 Agrupar e Agregar**
```python
# Group by
df.groupby('coluna').mean()
df.groupby('coluna').sum()
df.groupby('coluna').count()

# Múltiplas agregações
df.groupby('coluna').agg({
    'col1': 'mean',
    'col2': 'sum',
    'col3': 'count'
})

# Pivot table
df.pivot_table(values='valor', index='categoria', columns='ano', aggfunc='mean')
```

#### **🔢 Lidar com Dados Faltantes**
```python
# Ver valores nulos
df.isnull()
df.isnull().sum()

# Remover nulos
df.dropna()
df.dropna(subset=['coluna'])

# Preencher nulos
df.fillna(0)
df.fillna(method='ffill')      # Forward fill
df.fillna(method='bfill')      # Backward fill
df['coluna'].fillna(df['coluna'].mean())
```

#### **📈 Trabalhar com Datas**
```python
# Converter para datetime
df['data'] = pd.to_datetime(df['data'])

# Extrair partes da data
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df['dia'] = df['data'].dt.day
df['dia_semana'] = df['data'].dt.dayofweek

# Filtros de data
df[df['data'] > '2024-01-01']
df[df['data'].dt.year == 2024]

# Definir data como índice
df.set_index('data', inplace=True)
```

#### **📊 Visualizações Rápidas**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Gráficos básicos com pandas
df['coluna'].plot()                    # Linha
df['coluna'].hist()                    # Histograma
df.plot.scatter(x='col1', y='col2')   # Dispersão
df.plot.box()                         # Boxplot

# Com matplotlib/ seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='col1', y='col2')
plt.show()
```

#### **💾 Salvar e Exportar**
```python
# Salvar em CSV
df.to_csv('saida.csv', index=False)

# Salvar em Excel
df.to_excel('saida.xlsx', index=False)

# Salvar em JSON
df.to_json('saida.json')

# Salvar em Parquet (mais eficiente)
df.to_parquet('saida.parquet')
```

---

### **🔄 Fluxo de Trabalho Típico**

```python
# 1. Importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. Carregar dados
df = pd.read_csv('dados.csv')

# 3. Explorar dados
print(df.head())
print(df.info())
print(df.describe())

# 4. Limpar dados
df = df.dropna()
df['data'] = pd.to_datetime(df['data'])

# 5. Análise
media = df['valor'].mean()
agrupado = df.groupby('categoria')['valor'].sum()

# 6. Visualizar
df['valor'].plot(title='Valores ao longo do tempo')
plt.show()

# 7. Salvar resultados
agrupado.to_csv('resultados.csv')
```

---

### **⚡ Dicas de Performance**

```python
# Usar .loc em vez de encadeamento
df.loc[df['coluna'] > 10, 'nova'] = 'alto'

# Evitar loops com pandas
# Ruim: for row in df.iterrows()
# Bom: df.apply() ou vectorização

# Usar tipagem adequada
df['coluna'] = df['coluna'].astype('category')  # Para poucos valores únicos
df['numero'] = pd.to_numeric(df['numero'])      # Converter para numérico

# Memory usage
df.memory_usage()
df.info(memory_usage='deep')
```

> **💡 Estes comandos resolvem 95% das suas necessidades com Pandas e Jupyter!** 🚀

---

## 🐛 Desafios
- Compreender magic commands
- Dominar atalhos do Jupyter
- Manipulação básica pandas/numpy

---

## � Arquivos Práticos
- `jupyter_basic.ipynb`
- `pandas_basic.ipynb`

---

## � Progresso
- **Conceito:** 6/10
- **Prática:** 5/10
- **Aplicação:** 4/10

---

## 🎯 Próximos Passos
- [ ] Praticar mais magic commands
- [ ] Explorar funções avançadas do pandas
- [ ] Criar visualizações com matplotlib

---

*Criado em: 10/03/2026 13:02*
