from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente se necessário
load_dotenv()

# Conecte ao MongoDB
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri)
db = client['catalogo_produtos']
produtos_collection = db['produtos']

# Corrigir codigo_base para todos os produtos
produtos = list(produtos_collection.find({}))
count = 0

for produto in produtos:
    codigo_produto = produto.get('codigo_produto')
    if not codigo_produto or len(codigo_produto) < 2:
        continue
    # O codigo_base é o codigo_produto sem o último caractere
    codigo_base = codigo_produto[:-1]
    if produto.get('codigo_base') != codigo_base:
        produtos_collection.update_one(
            {'_id': produto['_id']},
            {'$set': {'codigo_base': codigo_base}}
        )
        count += 1

print(f"Corrigidos {count} produtos com codigo_base.")
