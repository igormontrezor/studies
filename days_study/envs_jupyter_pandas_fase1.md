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
people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreySchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}

df = pd.DataFrame(people)

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

# Remover linhas com condição
df.drop(df[df['coluna'] > 10].index)
```

---

### **🔧 Métodos e Funções Principais**

#### **📊 replace() - Substituir valores**
```python
# Substituir valores específicos
df['first'].replace('Corey', 'Chris')

# Exemplo com people: substituir nomes
df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})

# Substituir em todo DataFrame
df.replace('Doe', 'Smith')
```

#### **�️ map() - Aplicar função elemento por elemento**
```python
# Mapear valores
df['first'].map({'Corey': 1, 'Jane': 2, 'John': 3})

# Exemplo com people: converter para maiúsculas
df['first'].map(str.upper)

# Contar caracteres
df['email'].map(len)
```

#### **⚡ apply() - Aplicar função em Series/DataFrame**
```python
# Em Series (coluna)
df['email'].apply(len)              # Contar caracteres
df['first'].apply(str.upper)        # Maiúsculas

# Exemplo com people: tamanho do email
df['email'].apply(lambda x: len(x.split('@')[0]))  # Tamanho antes do @

# Em DataFrame
df.apply(len, axis='columns')        # Por linhas
```

#### **🎯 loc[] - Seleção por label**
```python
# Seleção por índice/nome
df.loc[0]                           # Primeira pessoa (Corey)
df.loc[0:2, 'first']                # Nomes das primeiras 3 pessoas

# Exemplo com people: filtrar e modificar
df.loc[df['last'] == 'Doe', 'status'] = 'mesmo_sobrenome'
```

#### **� iloc[] - Seleção por posição**
```python
# Por índice numérico (posição)
df.iloc[0]                          # Primeira linha
df.iloc[0:2]                        # Primeiras 2 linhas
df.iloc[0, 1]                       # Linha 0, coluna 1 (last)

# Exemplo com people: selecionar específicos
df.iloc[[0, 2], [0, 2]]             # Corey e John (nome e email)
```

#### **🎯 value_counts() - Contar valores**
```python
# Contar ocorrências de cada valor
df['coluna'].value_counts()

# Exemplo com people: contar sobrenomes
df['last'].value_counts()
```

#### **� contains() - Verificar se contém texto**
```python
# Verificar se texto contém substring
df['coluna'].str.contains('texto', na=False)

# Exemplo com people: encontrar quem tem 'gmail'
df['email'].str.contains('gmail', na=False)
```

#### **📋 isin() - Verificar se está em lista**
```python
# Verificar se valores estão em uma lista
nomes = ['Corey', 'John']
df['first'].isin(nomes)

# Exemplo com people: filtrar sobrenomes específicos
df[df['last'].isin(['Schafer', 'Doe'])]
```

#### **🏷️ rename() - Renomear colunas/índices**
```python
# Renomear colunas
df.rename(columns={'first': 'nome', 'last': 'sobrenome'})

# Exemplo com people: padronizar para português
df.rename(columns={'first': 'primeiro_nome', 'last': 'ultimo_nome', 'email': 'e_mail'})
```

#### **📐 set_index() - Definir coluna como índice**
```python
# Definir coluna como índice
df.set_index('email')

# Exemplo com people: usar email como índice
df.set_index('email')  # emails viram índice
```

#### **↩️ reset_index() - Resetar índice**
```python
# Transformar índice em coluna
df.reset_index()

# Exemplo com people: voltar índice numérico
df.reset_index()  # email volta a ser coluna
```

#### **🔧 str methods - Métodos de string**
```python
# Converter para minúsculas/maiúsculas
df['first'].str.lower()
df['first'].str.upper()

# Substituir texto
df['email'].str.replace('gmail', 'outlook')

# Exemplo com people: extrair domínio do email
df['email'].str.split('@').str[1]  # gmail.com, email.com, etc.
```

#### **📊 sort_values() - Ordenar dados**
```python
# Ordenar por coluna
df.sort_values('first')

# Exemplo com people: ordenar por sobrenome
df.sort_values('last', ascending=False)
```
# Memory usage
df.memory_usage()
df.info(memory_usage='deep')

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
