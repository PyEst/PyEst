# PyEst

![Alt Text](https://github.com/PyEst/pyest.github.io/blob/master/logo.png)

PyEst é uma ferramenta para tratamento estatístico desenvolvida em Python. Proposta por [Jackson Osvaldo da Silva Braga](https://jacksonosvaldo.github.io), a aplicação pretende ser útil em diversas áreas, dinamizando o tratamento e análise de dados, sejam eles ambientais ou não.

Em sua primeira versão (0.1), tornada pública em 25 de maio de 2018, ainda temos alguns bugs não resolvidos e outros que, com o decorrer do tempo, surgirão. Esperamos que a comunidade, seja ela científica, de programadores ou de curiosos sobre o assunto, colaborem com a proposta da aplicação, ajudando a melhorar e aprimorar o software.

# Windows

[Download Windows](https://github.com/PyEst/PyEst/blob/master/exe/PyEst_win.zip?raw=true)

Para Executar o software em ambiente Windows, é necessário a instalação da linguagem [Python](https://python.org), versão 3.5.

## Instalação da Linguagem de Programação Python

Para instalar a linguagem em ambiente Windows, atentando-se a arquitetura da máquina, se 32 bits ou 64 bits, deve-se seguir os seguintes passos.

**1º Passo**: Download do Instalador

Python 64 Bits | Python 32 Bits
------------ | -------------
[python-3.5.3-amd64.exe](https://www.python.org/ftp/python/3.5.3/python-3.5.3-amd64.exe) | [python-3.5.3.exe](https://www.python.org/ftp/python/3.5.3/python-3.5.3.exe)

**2º Passo**: Executando Instalador

Após concluído o download, execute o instalador em modo administrativo. O sistema perguntará se você deseja prosseguir àquela operação. Clique em "sim" e aguarde.

Deixe marcada a opção para adicionar os caminhos das pastas da linguagem às variáveis de ambiente do sistema. Marque a opção relativa a instalação padrão e prossiga.

Clique em prosseguir e aguarde a instalação terminar.

Caso a explicação acima esteja confusa, veja o tutorial gravado por mim de título [*PyEst - Instalação em Ambiente Windows*](https://youtu.be/YWtz38CqAMc).

**3º Passo**: Concluindo

Após a instalação da linguagem, deve-se instalar as bibliotecas [Pandas](https://pandas.pydata.org/), [Scipy](https://www.scipy.org/), [Numpy](http://www.numpy.org/) e [Matplotlib](https://matplotlib.org/). A instalação pode ser feita clicando em *install_libs.bat*.

Uma maneira alternativa para instalar as dependências é execuntado as seguintes linhas de comando:
```
python -m pip install scipy matplotlib pandas numpy
```
# Linux

[Dowload Linux](https://github.com/PyEst/PyEst/blob/master/exe/PyEst_linux.zip?raw=true)

Em ambiente linux, caso não esteja instalada a versão 3.5 da linguagem Python, pode-se fazer isso executando o script *install_libs.sh* via linha comando. Para isso, deve-se atribuir permissão ao arquivo com o comando *chmod +x install_libs.sh*. Feito isso, basta executar o script com *./install_libs.sh*.

Uma maneira alternativa para instalar as dependências é execuntado as seguintes linhas de comando:

```
sudo apt-get install python3.5
```

```
python3 -m pip install scipy matplotlib pandas numpy
```

# Código Fonte
Para ter acesso ao repositório com o código fonte da aplicação, basta clicar [aqui](https://github.com/PyEst/PyEst/tree/master/source).

# Dúvidas ou erros

Qualquer dúvida ou notificação sobre o incorreto funcionamento da aplicação, mande-me um e-mail.

[jacksonosvaldo@live.com](mailto:jacksonosvaldo@live.com)

# Referência

> [BRAGA, Jackson Osvaldo da Silva](http://lattes.cnpq.br/9545832415473039). **PyEst**. Version 0.1. [S.l.: s.n.], 2018.

# Citação

Com autor no texto: ... Braga (2018)

Com autor entre parênteses: ... (BRAGA, 2018)

# Publicações

BRAGA, J. O.; CAMPOS, L. D. [**PyEst**: Software Estatístico Desenvolvido em Python](https://github.com/PyEst/pyest.github.io/blob/master/pub/I%20JORNADA%20DE%20TECNOLOGIA%20DA%20INFORMAÇÃO%20DA%20UFRA.pdf). 2018. (Apresentação de Trabalho/Comunicação).

UNIVERSIDADE FEDERAL RURAL DA AMAZÔNIA. **PyEst | Software Estatístico Desenvolvido em Python | Jackson Osvaldo da Silva Braga**. Capanema, Pará, 10 jun. 2019. Disponível em: [https://bit.ly/2IAAIF6](https://bit.ly/2IAAIF6).
