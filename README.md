# Catálogo Web Luzarte

Este é um sistema web para gerenciamento de catálogo de produtos, desenvolvido para a Luzarte. O sistema permite visualizar, gerenciar e exportar produtos com suas variantes, preços e imagens.

## Funcionalidades Principais

### Galeria de Produtos
- Visualização de produtos em formato de cards
- Filtro por descrição do produto
- Seleção de diferentes tabelas de preço
- Paginação dos resultados
- Visualização de variantes de cores por produto

### Gerenciamento de Produtos
- Upload de planilha Excel para importação de produtos
- Upload de imagens para produtos
- Edição de preços por grupo de produtos
- Ajuste de preços por percentual ou valor fixo
- Controle de visibilidade dos produtos no catálogo

### Exportação
- Exportação do catálogo em PDF
- Opção de exportar apenas produtos com fotos
- Seleção da tabela de preço para exportação
- Exportação de dados para o sistema Protheus

### Tabelas de Preço
O sistema suporta múltiplas tabelas de preço.

### Níveis de Acesso
- **Dono**: Acesso total ao sistema, incluindo edição de preços e controle de visibilidade
- **Admin**: Gerenciamento de produtos e upload de imagens
- **Usuário**: Acesso apenas à visualização do catálogo

## Tecnologias Utilizadas
- Python/Flask
- MongoDB
- Bootstrap
- WeasyPrint (para geração de PDF)
- HTML/CSS/JavaScript

## Requisitos
- Python 3
- MongoDB
- Dependências listadas em requirements.txt


## Uso
1. Acesse o sistema através do navegador
2. Faça login com suas credenciais
3. Navegue pela galeria de produtos
4. Utilize as ferramentas de administração conforme seu nível de acesso
5. Exporte o catálogo em PDF quando necessário 