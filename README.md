

# Mercado Livre Scrapper

Um simples script em Python para acompanhar o preço de um produto no Mercado Livre e notificar o usuário por e-mail quando o preço cair abaixo de um certo valor.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina.

Também é necessário instalar a biblioteca `bs4` (BeautifulSoup), que pode ser instalada usando o seguinte comando:

```
pip install beautifulsoup4
```

## Como usar

1. Clone ou faça o download deste repositório.

2. Abra o arquivo `main.py` em um editor de código ou ambiente de desenvolvimento Python.

3. No código, atualize a variável `page` com o link do produto que você deseja monitorar:

```python
page = requests.get('linkdoproduto')
```

4. Defina o valor de referência que você deseja para o preço no método `price_checker`:

```python
def price_checker(price_conv):
    if price_conv < 100:
        email_sender()
    else:
        print("sistema funcionando")
        pass
```

5. Preencha as informações necessárias para o envio de e-mail no método `email_sender`:

```python
mail_from = 'Home@nilberth.com'
mail_to = ['nilberthsouza@gmail.com']
mail_subject = 'O seu produto baixou de preço'
mail_message_body = 'https://produto.mercadolivre.com.br/MLB-698976428-peruca-cosplay-branca-prata-prontaentrega-_JM'
```

6. Execute o script executando o seguinte comando no terminal:

```
python main.py
```

O script continuará rodando em um loop, verificando o preço do produto em intervalos regulares. Se o preço cair abaixo do valor definido, você receberá um e-mail de notificação.

## Interface Gráfica (GUI)

Além do script de linha de comando, o código também inclui uma interface gráfica básica usando a biblioteca Tkinter. Para executar a interface gráfica, siga as instruções abaixo:

1. Abra o arquivo `gui.py` em um editor de código.

2. Execute o script com o comando:

```
python gui.py
```

Uma janela de interface gráfica será aberta, permitindo que você insira o link do produto e visualize informações.
