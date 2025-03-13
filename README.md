# Meu Repositório Git Personalizado

## Configuração Inicial

Para personalizar seu repositório Git, siga estas etapas:

### 1. Configurar Nome e E-mail Globalmente
```sh
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

### 2. Criar um Alias para Comandos Úteis
```sh
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm "commit -m"
```

### 3. Definir um Arquivo de Exclusão Global
Crie um arquivo de exclusão global para ignorar arquivos desnecessários:
```sh
git config --global core.excludesfile ~/.gitignore_global
```
Adicione regras ao `~/.gitignore_global`:
```
*.log
node_modules/
.DS_Store
```

### 4. Definir Cores no Terminal
```sh
git config --global color.ui auto
```

### 5. Habilitar Rebase no Pull
```sh
git config --global pull.rebase true
```

### 6. Verificar Configurações
```sh
git config --list
```

## Criando e Clonando um Repositório

### Criar um Novo Repositório
```sh
git init meu-repositorio
cd meu-repositorio
echo "# Meu Repositório" > README.md
git add .
git commit -m "Primeiro commit"
git branch -M main
git remote add origin https://github.com/seuusuario/meu-repositorio.git
git push -u origin main
```

### Clonar um Repositório Existente
```sh
git clone https://github.com/seuusuario/meu-repositorio.git
```

---

## Simples Nacional

O **Simples Nacional** é um regime tributário diferenciado, criado para **microempresas (ME) e empresas de pequeno porte (EPP)** no Brasil. Ele unifica o pagamento de diversos tributos federais, estaduais e municipais em uma única guia, o **DAS (Documento de Arrecadação do Simples Nacional)**.

### **Principais Características:**
- **Abrangência:** Empresas com faturamento anual de até **R$ 4,8 milhões**.
- **Tributos unificados:** Inclui **IRPJ, CSLL, PIS, COFINS, IPI, CPP, ICMS e ISS**.
- **Alíquotas progressivas:** Variam conforme a receita bruta dos últimos 12 meses e são definidas em **5 anexos** conforme a atividade da empresa.
- **Facilidade de pagamento:** Uma única guia mensal (DAS).
- **Menos burocracia:** Simplificação no cumprimento das obrigações acessórias.

### **Vantagens:**
✔️ Redução da carga tributária para muitos negócios.  
✔️ Menos obrigações fiscais e contábeis.  
✔️ Unificação do pagamento dos tributos.  
✔️ Permite a participação de MEI, ME e EPP.  

### **Desvantagens:**
❌ Restrições para algumas atividades.  
❌ Nem sempre é o regime mais vantajoso para todas as empresas.  
❌ Empresas com muitos funcionários podem pagar mais encargos previdenciários.  

Se precisar de algo mais específico, posso aprofundar em qualquer ponto!
