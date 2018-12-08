#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter
import tkinter.scrolledtext as tkst
from tkinter.ttk import *
from tkinter import ttk
from tkinter.constants import END,HORIZONTAL, VERTICAL, NW, N, E, W, S, SUNKEN, LEFT, RIGHT, TOP, BOTH, YES, NE, X, RAISED, SUNKEN, DISABLED, NORMAL, CENTER, WORD
import tkinter.filedialog as fdlg
from tkinter import messagebox as msb
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


## Default
matplotlib.style.use('ggplot')

###janela Principal
janela = Tk()

"""
------------------------------------
Inicializando menu (cascata)
------------------------------------
"""
menubar = Menu(janela)

janela.config(menu=menubar)

##Menus - Quantidade
filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)
filemenu4 = Menu(menubar)

###Autoria
autoria = '\n'+('==='*21)+"""
Análise realizada com PyEst
Software desenvolvido por Jackson Osvaldo da Silva Braga
Graduando em Engenharia Ambiental e Energias Renováveis
mail: jacksonenazus@gmail.com
fone: +5591991949964
"""

#####################
# Definindo funções #
#####################
def sair():
    sairQuestion = msb.askquestion(title='Sair', message='Você deseja sair?')
    if sairQuestion == "yes":
        janela.destroy()


def erro():
    msb.showerror(title='Erro', message='Não foi possível executar esta ação. Verique se o seu arquivo foi carregado corretamente.')


def exibir():
    exibir = msb.askquestion(title="Operação concluida", message='Operação realizada com sucesso. Deseja exibir os dados na área de saída?')
    return exibir


def carregarArquivo():

    try:
        arquivoTratamento = str(fdlg.askopenfilename(defaultextension='.csv'))
        global arquivoTratamento

        def teste():
            with open(arquivoTratamento) as t:
                a = t.readline()
                return a
        
        if teste() == None:
            msb.showwarning('Aviso','Arquivo não carregado. Para executar as operações estatísticas você precisa carregar um arquivo csv.')
        
        else:
            
            if msb.askquestion(title='Sucesso', message='Seu arquivo foi carregado com sucesso. Deseja exibi-lo?') == "yes":
                exibir = pd.read_csv(arquivoTratamento)
                saida.insert(END, str(exibir)+'\n')
                msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
        
    except NameError:
        msb.showwarning('Aviso','Arquivo não carregado. Para executar as operações estatísticas você precisa carregar um arquivo csv.')
    except OSError:
        msb.showwarning('Aviso','Arquivo não carregado. Para executar as operações estatísticas você precisa carregar um arquivo csv.')
    except FileNotFoundError:
        msb.showwarning('Aviso','Arquivo não carregado. Para executar as operações estatísticas você precisa carregar um arquivo csv.')
    except AttributeError:
        msb.showwarning('Aviso','Arquivo não carregado. Para executar as operações estatísticas você precisa carregar um arquivo csv.')

def exibir():
    exibir = pd.read_csv(arquivoTratamento)
    saida.insert(END, str(exibir)+'\n')
    msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')

def salvar():

    try:
        f = fdlg.asksaveasfile(mode='w', defaultextension = ".txt")
        if f is None:
            return
        tex2Save = str(saida.get(1.0, END)+autoria)
        f.write(tex2Save)
        msb.showinfo(title='Salvar', message='Dados salvos com sucesso!')
        f.close()
    except NameError:
        erro()

###Operações estatíticas - Medidas de Tendência Central
def resumo():
    try:
        resumo = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - RESUMO\n'+('==='*15)+'\n'+str(resumo.describe())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()

def media():
    try:
        tratarMedia = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - MEDIAS\n'+('==='*15)+'\n'+str(tratarMedia.mean())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()

def mediana():
    try:
        tratarMediana = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - MEDIANAS\n'+('==='*15)+'\n'+str(tratarMediana.median())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()
def quantil():
    try:
        tratarQuantil = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - QUANTIS\n'+('==='*15)+'\n'+str(tratarQuantil.quantile())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()

def moda():
    try:
        tratarModa = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - MODAS\n'+('==='*15)+'\n'+str(tratarModa.mode())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()



###Operações estatíticas - Medidas de dispersão
def amplitude():
    try:
        tratarAmplitude = pd.read_csv(arquivoTratamento)
        saida.insert(END,(('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - AMPLITUDE\n'+('==='*15)+'\n'+('==='*15)+'\n\t\t\tMÁXIMOS\n'+('==='*15)+'\n'+str(tratarAmplitude.max())+'\n'+('==='*15)+'\n\t\t\tMÍNIMOS\n'+('==='*15)+'\n'+str(tratarAmplitude.min())+'\n'))
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()

def variancia():
    try:
        tratarVar = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - VARIÂNCIAS\n'+('==='*15)+'\n'+str(tratarVar.var())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()
def desvioPadrao():
    try:
        tratarDesvPad = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\tANÁLISE CONCLUÍDA - DESVIO PADRÃO\n'+('==='*15)+'\n'+str(tratarDesvPad.std())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()

def desvAbsoluto():
    try:
        tratarDesvAbs = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\tANÁLISE CONCLUÍDA - DESVIO ABSOLUTO\n'+('==='*15)+'\n'+str(tratarDesvAbs.mad())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()

def covar():
    try:
        tratarCov = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\t\tANÁLISE CONCLUÍDA - COVARIÂNCIA\n'+('==='*15)+'\n'+str(tratarCov.cov())+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()

def Corr():
    try:
        tratarCorr = pd.read_csv(arquivoTratamento)
        saida.insert(END, ('==='*15)+'\n\tANÁLISE CONCLUÍDA - CORRELAÇÃO (pearson)\n'+('==='*15)+'\n'+str(tratarCorr.corr(method='pearson'))+'\n')
        msb.showinfo(title='Concluido', message='Operação realizada com sucesso!')
    except NameError:
        erro()
    except  OSError:
        erro()


###Configurando exibição dos gráficos    
def graph():
    
    try:
        arquivoTratamento
        
        try:
            
            graficos = Tk()

            ## Definindo função para criação dos gráficos
            def gerar():

                plotGraph = pd.read_csv(arquivoTratamento)                

                try:
                    if tiposGra.get() == 'cumsum' and colunas.get() == 'Todas':
                        plotGraph.cumsum()
                        plotGraph.plot()
                        plt.show()
                    else:
                        if tiposGra.get() == 'cumsum' and colunas.get() != 'Todas':
                            msb.showerror(title='Erro', message='Para exibir este tipo de gráfico, você deve selecionar a opção todas, em variáveis.')
                    
                    if tiposGra.get() == 'bar' and colunas.get() != None and colunas.get() != 'Todas':
                        plotGraph[colunas.get()].plot(kind='bar', title=str(colunas.get()))
                        plt.show()
                    else:
                        if tiposGra.get() == 'bar' and colunas.get() == 'Todas':
                            plotGraph.plot(kind='bar')
                            # plotGraph.plot(kind='bar', stacked=True)
                            
                            plt.show()
                    if tiposGra.get() == 'bar-stacked' and colunas.get() != None and colunas.get() == 'Todas':
                        plotGraph.plot(kind='bar', stacked=True)
                        plt.show()

                    else:
                        if tiposGra.get() == 'bar-stacked' and colunas.get() != None and colunas.get() != 'Todas':
                            msb.showerror(title='Erro', message='Para exibir este tipo de gráfico, você deve selecionar a opção todas, em variáveis.')
                    
                    
                    if tiposGra.get() == 'barh-stacked' and colunas.get() != None and colunas.get() == 'Todas':
                        plotGraph.plot(kind='barh', stacked=True)
                        plt.show()

                    else:
                        if tiposGra.get() == 'barh-stacked' and colunas.get() != None and colunas.get() != 'Todas':
                            msb.showerror(title='Erro', message='Para exibir este tipo de gráfico, você deve selecionar a opção todas, em variáveis.')

                    if tiposGra.get() == 'hist' and colunas.get() != None and colunas.get() == 'Todas':
                        plotGraph.plot(kind='hist')
                        plotGraph.diff().hist(color='k',alpha=0.5)
                        plt.show()
                    else:
                        if tiposGra.get() == 'hist' and colunas.get() != None and colunas.get() != 'Todas':
                            plotGraph[colunas.get()].plot(kind='hist', title=colunas.get())
                            plt.show()
                    
                    if tiposGra.get() == 'box' and colunas.get() != None and colunas.get() != 'Todas':
                        plotGraph[colunas.get()].plot(kind='box', title=colunas.get())
                        plt.show()
                    else:
                        if tiposGra.get() == 'box' and colunas.get() != None and  colunas.get() == 'Todas':
                            plotGraph.plot(kind='box')
                            plt.show()
                    
                    if tiposGra.get() == 'scatter' and eixoX.get() != None and eixoY.get() != None:
                        plotGraph.plot(kind='scatter', x = eixoX.get(), y = eixoY.get())
                        plt.show()

                    else:
                        if tiposGra.get() == 'scatter' and eixoX.get() == None and eixoY.get() == None:
                            msb.showerror(title='Erro', message='Para exibir este tipo de gráfico, você deve uma opção para o Eixo X e outra para o Eixo Y.')

                    if tiposGra.get() == 'kde' and colunas.get() != None and colunas.get() == 'Todas':
                        from pandas.tools.plotting import scatter_matrix
                        scatter_matrix(plotGraph, alpha=0.2, figsize=(6, 6), diagonal='kde')
                        plt.show()
                    else:
                        if tiposGra.get() == 'kde' and colunas.get() != None and colunas.get() != 'Todas':
                            plotGraph[colunas.get()].plot(kind='kde',title=colunas.get())
                            plt.show()
                except KeyError:
                    msb.showerror(title='Erro', message='Selecione os valores correspondentes ao tipo do gráfico. Apenas assim poderá exibi-lo.')
                except NameError:
                    msb.showerror(title='Erro', message='Selecione os valores correspondentes ao tipo do gráfico. Apenas assim poderá exibi-lo.')

            ##Box variáveis
            colunas = ttk.Combobox(graficos)
            colunas['font'] = ('12')

            ## Label Variáveis
            var = Label(graficos, text='Variáveis',font='12')

            ##Box tipo de gráfico
            tiposGra = ttk.Combobox(graficos)
            tiposGra['font'] = ('12')
            tiposGra['values'] = ('cumsum','bar','bar-stacked','barh-stacked', 'hist', 'box','scatter','kde')
            ## Label tipo de gráfico
            textTposGraf = Label(graficos, text='Tipo de Gráfico', font='12')

            
            ## Eixo x
            eixoX = ttk.Combobox(graficos)
            eixoX['font'] = ('12')
            ## Label Eixo X
            lEixoX = Label(graficos, text='Eixo X', font='12')
            
            ## Eixo y
            eixoY = ttk.Combobox(graficos)
            eixoY['font'] = ('12')
            ## Label Eixo X
            lEixoY = Label(graficos, text='Eixo Y', font='12')

            ## Botão para gerar gráfico
            plotar = Button(graficos, text='Plotar', comman = gerar)
    
            ## Rodando wid's
            var.pack()
            colunas.pack()
            textTposGraf.pack()
            tiposGra.pack()
            lEixoX.pack()
            eixoX.pack()
            lEixoY.pack()
            eixoY.pack()
            plotar.pack()

            a = open(str(arquivoTratamento),'r')
            i = 0
            for linha in a:
                linha = linha.strip()
                i = i + 1
                b = []
                col = []
                col = linha.split(sep=',')
                if i == 1:
                    colunas['values'] = ['Todas']+col
                    eixoX['values'] = col
                    eixoY['values'] = col
                    break
        

            graficos.resizable(0,0)
            graficos.title('Gráficos')
            graficos.mainloop()
        except NameError:
            erro()
        except FileNotFoundError:
            erro()
        except OSError:
            erro()
    except NameError:
        erro()
    except FileNotFoundError:
    	erro()
    except OSError:
        erro() 

###Configurando Aba Ajuda
def doc():
    msb._show(title='Documentação', message='Você pode ter acesso a documentação do PyEst no site da aplicação, o mesmo que você usou para fazer o download do arquivo executável.')

def formatoCSV():
    msb._show(title='Formato do Arquivo CSV para análise', message="""
    O arquivo csv para análise não deve conter acentos gráficos, nem espaços entre os nomes dos parâmetros. A primeira linha deve conter apenas os nomes das colunas. Nas demais linhas, seguem-se os dados para análise."""
    )

def sobre():
    msb._show(title='Sobre', message="""
    O PyEst é uma aplicação desenvolvida em Python (3.5) por Jackson Osvaldo da Silva Braga. A proposta da aplicação é ser útil em diversas áreas, dinamizando o tratamento e análise de dados, sejam eles ambientais ou não."""
    )

## Menu 01 - Arquivo
menubar.add_cascade(label='Arquivo',font='12', menu=filemenu)
menubar.add_separator()
filemenu.add_command(label='Carregar Arquivo',font='12', command = carregarArquivo)
filemenu.add_command(label='Resumo do Banco de Dados',font='12', command = resumo)
filemenu.add_command(label='Gráficos',font='12',command=graph)
filemenu.add_command(label='Salvar',font='12', command=salvar)
filemenu.add_separator()
filemenu.add_command(label='Sair',font='12', command=sair)

## Menu 02 - Medidas de Tendência Central
menubar.add_cascade(label = 'Medidas de Tendência Central',font='12', menu=filemenu2)
filemenu2.add_command(label='Média',font='12', command = media)
filemenu2.add_command(label='Mediana',font='12', command = mediana)
filemenu2.add_command(label='Quantil',font='12', command=quantil)
filemenu2.add_command(label='Moda',font='12', command=moda)


##Menu 03 - Medidas de Dispersão
menubar.add_cascade(label = 'Medidas de Dispersão',font='12', menu=filemenu3)
filemenu3.add_command(label='Amplitude',font='12', command = amplitude)
filemenu3.add_command(label='Variância',font='12',command=variancia)
filemenu3.add_command(label='Desvio Padrão',font='12',command=desvioPadrao)
filemenu3.add_command(label='Desvio Absoluto',font='12',command=desvAbsoluto)
filemenu3.add_command(label='Covariância',font='12',command=covar)
filemenu3.add_command(label='Correlação',font='12',command=Corr)

##Menu 04 - Ajuda e Documentação
menubar.add_cascade(label = 'Ajuda',font='12', menu=filemenu4)
filemenu4.add_command(label='Documentação',font='12', command=doc)
filemenu4.add_command(label='Formatação do arquivo csv para análise',font='12',command=formatoCSV)
filemenu4.add_command(label='Sobre',font='12', command=sobre)

"-----------------------------------"

### Configurando janela de saida das análises
saida = tkst.ScrolledText(master = janela,font='12',wrap= WORD,width  = 20,height = 10)
saida.pack(padx=10, pady=10, fill=BOTH, expand=True)


janela.title('PyEst - Desenvolvido por Jackson Osvaldo da Silva Braga')


janela.geometry('{}x{}'.format(janela.winfo_screenwidth(),janela.winfo_screenheight()))
janela.mainloop()
