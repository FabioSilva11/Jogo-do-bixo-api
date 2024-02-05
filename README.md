# Jogo-do-bixo-api

Este é uma apu simples em Flask que oferece duas rotas principais: `/sorteio` e `/lista_animais`. O objetivo principal é fornecer um sorteio aleatório de animais para o jogo do bixo seus respectivos números associados e links para imagens.

## Configuração e Execução Local

### 1. Instalação das Dependências

Antes de iniciar, certifique-se de ter o Flask instalado. Caso contrário, você pode instalá-lo utilizando o seguinte comando no terminal:
```bash
pip install Flask
```

### 2. Execução do Aplicativo

Para iniciar o aplicativo, execute o seguinte comando no terminal, substituindo "app.py" pelo nome real do seu arquivo Python:
```bash
python app.py
```

O aplicativo estará disponível em 
```bash
http://127.0.0.1:5000/
```
ou

```bash
http://localhost:5000/
```

## Rotas Disponíveis

### Rota 1: Sorteio de Animais

- **URL:** `/sorteio`

- **Descrição:** Gera um sorteio aleatório de um animal, fornecendo o número sorteado, o nome do animal e um link para a imagem correspondente.

- **Exemplo de Resposta:**
- 
  ```json
  {
    "numero_sorteado": 42,
    "animal_sorteado": "Cavalo",
    "imagem": "link_para_imagem11.jpg"
  }
  ```

### Rota 2: Lista de Animais

- **URL:** `/lista_animais`

- **Descrição:** Retorna a lista completa de animais com seus números associados e links para as imagens correspondentes.

- **Exemplo de Resposta:**
  ```json
  {
    "Avestruz": {"numero": [0, 1, 2, 3], "imagem": "link_para_imagem1.jpg"},
    "Águia": {"numero": [4, 5, 6, 7], "imagem": "link_para_imagem2.jpg"},
    "Veado": {"numero": [92, 93, 94, 95], "imagem": "link_para_imagem24.jpg"}
  }
  ```

Lembre-se jogo do bixo e crime, use a api apenas para estudo
