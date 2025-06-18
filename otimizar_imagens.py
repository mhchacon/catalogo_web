import os
from PIL import Image

# Caminho da pasta de imagens
PASTA_IMAGENS = 'static/uploads/images'
TAMANHO_MAX_KB = 500

def otimizar_imagem(caminho):
    try:
        img = Image.open(caminho)
        # Se for PNG com transparência, converte para fundo branco
        if img.mode in ("RGBA", "P"):
            fundo = Image.new("RGB", img.size, (255, 255, 255))
            fundo.paste(img, mask=img.split()[-1])  # Usa o canal alpha como máscara
            img = fundo
        else:
            img = img.convert("RGB")
        # Tenta salvar com qualidade decrescente até ficar < 500 KB
        qualidade = 85
        while qualidade >= 30:
            img.save(caminho, format='JPEG', quality=qualidade, optimize=True)
            tamanho_kb = os.path.getsize(caminho) // 1024
            if tamanho_kb <= TAMANHO_MAX_KB:
                print(f"{os.path.basename(caminho)}: {tamanho_kb} KB (qualidade {qualidade})")
                return
            qualidade -= 5
        print(f"{os.path.basename(caminho)}: não foi possível reduzir abaixo de 500 KB (ficou {tamanho_kb} KB)")
    except Exception as e:
        print(f"Erro ao otimizar {caminho}: {e}")

def otimizar_pasta():
    for nome_arquivo in os.listdir(PASTA_IMAGENS):
        caminho = os.path.join(PASTA_IMAGENS, nome_arquivo)
        if not os.path.isfile(caminho):
            continue
        # Só processa imagens
        if nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            otimizar_imagem(caminho)

if __name__ == '__main__':
    otimizar_pasta()
    print('Otimização concluída!')
