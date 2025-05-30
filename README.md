# Catálogo de Produtos

Aplicação web para gerenciamento de catálogo de produtos, permitindo a seleção de produtos ativos e exportação para o sistema Protheus.

## Requisitos

- Python 3.8+
- MongoDB Atlas (banco de dados na nuvem)
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd catalogo_web
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
SECRET_KEY=sua-chave-secreta-aqui
MONGODB_URI=sua-string-de-conexao-mongodb-atlas
```

5. Configuração do MongoDB Atlas:
   - Acesse o MongoDB Atlas (https://cloud.mongodb.com)
   - Crie um cluster gratuito se ainda não tiver
   - Obtenha a string de conexão no botão "Connect"
   - Substitua `<password>` pela senha do seu usuário
   - Cole a string de conexão no arquivo `.env`

## Executando a Aplicação

1. Ative o ambiente virtual (se ainda não estiver ativo):
```bash
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

2. Execute a aplicação:
```bash
python app.py
```

3. Acesse a aplicação em seu navegador:
```
http://localhost:5000
```

## Uso

### Login
- Dono (para marcar produtos no catálogo):
  - Usuário: dono
  - Senha: senha123
- Admin (para gerenciar produtos e imagens):
  - Usuário: admin
  - Senha: admin123

### Funcionalidades

1. **Visualização Pública**
   - A galeria de produtos é pública e pode ser acessada sem login
   - Mostra todos os produtos com suas imagens e descrições

2. **Área do Dono**
   - Acesse com as credenciais do dono
   - Marque quais produtos devem permanecer no catálogo
   - Salve as decisões

3. **Área do Admin**
   - Acesse com as credenciais do admin
   - Importe produtos via Excel
   - Faça upload de imagens
   - Exporte dados para Protheus

## Estrutura do Projeto

```
catalogo_web/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências
├── .env               # Configurações (não versionado)
├── templates/         # Templates HTML
│   ├── base.html
│   ├── login.html
│   ├── galeria.html
│   └── admin.html
└── uploads/          # Diretório para uploads
    └── images/       # Imagens dos produtos
```

## Segurança

- O arquivo `.env` contém informações sensíveis e não deve ser versionado
- Em ambiente de produção:
  - Altere a chave secreta no arquivo `.env`
  - Implemente um sistema de autenticação mais robusto
  - Use HTTPS
  - Configure o MongoDB Atlas com regras de acesso restritas
  - Use variáveis de ambiente do servidor em vez do arquivo `.env` 