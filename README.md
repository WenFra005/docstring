# 📝 docpdf

O **docpdf** é uma ferramenta simples e útil para gerar uma documentação limpa e organizada de projetos Python. Ele extrai os comentários de documentação (docstrings) direto do código-fonte e cria um PDF com todas essas informações — pronto para compartilhar ou consultar.

> 📦 **Disponível no PyPI**: você pode instalar com apenas um comando!  
> 👉 `pip install docpdf`

## 🚀 Para que serve?

Você pode usar essa ferramenta para:

- Compartilhar a documentação do seu código de forma profissional.
- Ter uma visão geral rápida de todas as funções e classes do seu projeto.
- Evitar a leitura manual do código para entender o que ele faz.

## ✅ O que o programa faz?

- Lê todos os arquivos `.py` (Python) em uma pasta.
- Extrai as docstrings de classes, funções e módulos.
- Gera um arquivo PDF organizado com essas informações.

## 📦 Instalação

### Opção 1: Instalar via PyPI (recomendado)

```bash
pip install docpdf
```

Depois de instalado, você pode usar o comando:

```bash
docpdf main.py
```

Por padrão, ele irá escanear o diretório atual e gerar um PDF com o nome `docstrings_output.pdf`.

### Opção 2: Instalar manualmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/WenFra005/docstring
   cd docstring
   ```

2. Instale as dependências:

   ```bash
   pip install fpdf
   ```

3. Rode o script manualmente:

   ```bash
   python main.py
   ```

## ⚙️ Como usar

Após a instalação, vá até a pasta do seu projeto (onde estão seus arquivos `.py`) e execute:

```bash
docpdf main.py
```

Um PDF será gerado no mesmo diretório contendo todas as docstrings encontradas.

Você também pode usar o comando com um caminho específico:

```bash
docpdf path/para/seu/projeto
```

## 📁 Exemplo de uso

```python
def soma(a, b):
    """
    Retorna a soma de dois números.
    """
    return a + b
```

O PDF vai mostrar algo assim:

```
Arquivo: meu_script.py

Função: soma
Descrição: Retorna a soma de dois números.
```

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um fork do repositório.
2. Crie uma branch:

   ```bash
   git checkout -b minha-melhoria
   ```

3. Faça suas mudanças.
4. Envie um Pull Request.

Você também pode abrir uma [issue](https://github.com/WenFra005/docstring/issues) com sugestões ou relatando bugs.

## 📄 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo [LICENSE](https://github.com/WenFra005/docstring/blob/main/LICENSE) para mais detalhes.