# 📚 Diário de Estudos

## 📅 11-03-2026 | 🎯 git_github_fase1
![alt text](imagens\git_github.png)
---

## � Resumo
- **Duração:**
- **Conteúdo:**
- **Fontes:**

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
# Ver branches
git branch

# Criar e mudar para nova branch
git checkout -b nova-branch

# Voltar para branch principal
git checkout master

# Juntar branches
git merge nova-branch
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

#### **🔄 Fluxo Diário**
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

> **💡 Estes 15 comandos resolvem 90% das suas necessidades!** 🚀
-
-
-

---

## 🐛 Desafios
-
-
-

---

##  Arquivos Práticos
-

---

## � Progresso
- **Conceito:** /10
- **Prática:** /10
- **Aplicação:** /10

---

## 🎯 Próximos Passos
- [ ]
- [ ]
- [ ]

---

*Criado em: 11/03/2026 13:10*
