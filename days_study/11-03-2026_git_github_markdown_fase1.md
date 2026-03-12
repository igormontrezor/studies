# 📚 Diário de Estudos

## 📅 11-03-2026 | 🎯 git_github_markdown_fase1
![alt text](../imagens/git_github.png)
---

## 📝 Resumo
- **Duração:**
- **Conteúdo:** Comandos Git essenciais e formatação Markdown básica
- **Fontes:** Documentação oficial, GitHub Guides

---

## 🎯 Aprendizados Principais

### **📋 Comandos Git Essenciais**

#### **🔧 Configuração**
```bash
# Configurar usuário
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

#### **📁 Repositório**
```bash
# Iniciar novo repositório
git init

# Clonar repositório existente
git clone https://github.com/user/repo.git

# Verificar status
git status
```

#### **📝 Arquivos**
```bash
# Adicionar arquivo específico
git add arquivo.txt

# Adicionar todos os arquivos
git add .

# Adicionar .gitignore
git add .gitignore

# Criar .gitignore
echo "arquivo.txt" > .gitignore
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore
```

# Ver mudanças antes de commit
git diff
```

#### **💾 Commits**
```bash
# Fazer commit
git commit -m "Mensagem clara"

# Adicionar e commitar tudo de uma vez
git commit -am "Mensagem rápida"
```

#### **🌐 GitHub (Remote)**
```bash
# Adicionar repositório remoto
git remote add origin https://github.com/user/repo.git

# Enviar para GitHub
git push

# Puxar mudanças do GitHub
git pull

# Primeiro envio (definir branch principal)
git push -u origin master

# Verificar conformidade entre máquina e GitHub
git fetch origin
git status
git diff HEAD origin/master
```

#### **⏮️ Desfazer**
```bash
# Desfazer mudanças não salvas
git restore arquivo.txt

# Desfazer último commit (mantém arquivos)
git reset --soft HEAD~1

# Reverter commit específico
git revert hash-do-commit
```

#### **🌿 Branches**
```bash
# Ver branches locais
git branch

# Ver branches locais e remotas
git branch -a

# Ver branch atual
git branch --show-current

# Criar nova branch (sem mudar para ela)
git branch nova-branch

# Criar e mudar para nova branch
git checkout -b nova-branch
git switch -c nova-branch

# Mudar para branch existente
git checkout nome-branch
git switch nome-branch

# Voltar para branch principal
git checkout master
git checkout main
git switch main

# Renomear branch atual
git branch -m novo-nome

# Renomear branch específica
git branch -m nome-antigo nome-novo

# Deletar branch local
git branch -d nome-branch
git branch -D nome-branch  # forçar

# Deletar branch remota
git push origin --delete nome-branch

# Juntar branches (merge)
git checkout main
git merge nova-branch

# Juntar sem commit (fast-forward)
git merge --ff-only nova-branch

# Cancelar merge em conflito
git merge --abort

# Ver branches com último commit
git branch -v

# Ver branches mescladas
git branch --merged

# Ver branches não mescladas
git branch --no-merged
```

#### **📊 Histórico**
```bash
# Ver commits recentes
git log --oneline

# Ver histórico completo
git log

# Ver mudanças específicas
git show
```

#### **🔄 GitHub CLI**
```bash
# Tornar repositório público
gh repo edit igormontrezor/studies --visibility public --accept-visibility-change-consequences

# Ver informações do repositório
gh repo view igormontrezor/studies
```

#### **�️ Remover Arquivos**
```bash
# Remover arquivo do diretório e do Git
git rm arquivo.txt

# Remover arquivo apenas do Git (manter no diretório)
git rm --cached arquivo.txt

# Remover arquivo já deletado do Git
git rm arquivo.txt

# Remover múltiplos arquivos
git rm arquivo1.txt arquivo2.txt arquivo3.txt

# Remover por padrão (wildcard)
git rm *.log
git rm temp_*

# Forçar remoção de arquivo modificado
git rm -f arquivo.txt

# Remover diretório inteiro
git rm -r pasta/

# Remover arquivo do GitHub (após commit e push)
git rm arquivo.txt
git commit -m "Remover arquivo.txt"
git push

# Remover arquivo que já foi deletado localmente
git add -A
git commit -m "Limpar arquivos deletados"
git push
```

#### **�� Fluxo Diário**
```bash
# 1. Atualizar com GitHub
git pull

# 2. Trabalhar nos arquivos
# ... editar ...

# 3. Ver o que mudou
git status

# 4. Salvar mudanças
git add .
git commit -m "O que foi feito"

# 5. Enviar para GitHub
git push
```

> **💡Comandos Markdown Essenciais** 🚀

---

### **📝 Markdown Básico**

#### **🔤 Formatação de Texto**
```markdown
# Título 1
## Título 2
### Título 3

**Texto em negrito**
*Texto em itálico*
~~Texto riscado~~
`Código inline`
```

#### **📋 Listas**
```markdown
# Lista não ordenada
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2

# Lista ordenada
1. Primeiro item
2. Segundo item
3. Terceiro item

# Lista de tarefas
- [ ] Tarefa pendente
- [x] Tarefa concluída
```

#### **🔗 Links e Imagens**
```markdown
# Link
[Texto do link](https://exemplo.com)

# Imagem
![Texto alternativo](caminho/da/imagem.jpg)

# Link em imagem
[![Texto alternativo](caminho/da/imagem.jpg)](https://exemplo.com)
```

#### **📊 Tabelas**
```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Dado 1   | Dado 2   | Dado 3   |
| Dado 4   | Dado 5   | Dado 6   |

# Alinhamento
| Esquerda | Centro | Direita |
|:---------|:------:|--------:|
| Texto    | Texto  | Texto   |
| Dados    | Dados  | Dados   |
```

#### **💻 Código**
```markdown
# Código inline
Use o comando `git status` para verificar.

# Bloco de código
```bash
git add .
git commit -m "Mensagem"
```

# Código com sintaxe destacada
```python
def hello_world():
    print("Hello, World!")
```
```

#### **📌 Citações e Destaques**
```markdown
# Citação
> Isso é uma citação importante.
> Pode ter múltiplas linhas.

# Citação aninhada
> Citação principal
>> Citação aninhada

# Linha horizontal
---
***
___
```

#### **🔧 Outros Elementos**
```markdown
# Texto com HTML
<u>Sublinhado</u>
<mark>Destacado</mark>

# Emojis
:rocket: 🚀
:book: 📚
:computer: 💻

# Referências
Veja a [seção de comandos][git] para mais detalhes.

[git]: #-comandos-git-essenciais


*Criado em: 11/03/2026 13:10*
