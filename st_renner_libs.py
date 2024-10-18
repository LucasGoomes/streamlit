import streamlit as st
import plotly.express as px
import base64
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

def descricao_projeto():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Descrição do Projeto</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_descricao_problema = '''
        Com o crescente aumento do uso de e-commerce, diversidade de produtos e serviços disponíveis, e características distintas de clientes que utilizam este tipo de plataforma, estratégias que funcionavam de maneira eficiente tempos atrás, podem não responder tão bem às demandas atuais. 

        Conseguir identificar de maneira correta as diferenças fundamentais entre grupos de clientes e a partir disso, ser capaz de elaborar estratégias ideais para cada grupo é um desafio contemporâneo e dinâmico, mas que tem se tornado um diferencial importante na retenção e incremento de receitas. 
    '''

    # Mostra o texto na página
    st.markdown(texto_descricao_problema)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Descrição da Solução Proposta</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_descricao_solucao = '''
        Como proposta de trabalho, o grupo planeja desenvolver uma ferramenta chamada “Renner 
        Rethink”, que visa analisar cada cliente sob diversos prismas e agrupá-los através de técnicas de 
        Clusterização, para identificar os produtos mais relevantes a serem oferecidos para cada grupo de 
        clientes. 
        Os entregáveis serão feitos através de páginas web com as seguintes funções: 
        - Detalhamentos das análises e tratamento dos dados 
        - Modelagem interativa, onde a Renner pode executar testes e avaliar resultados sobre os modelos 
        - Relatório em PDF com toda a explicação do projeto baseado no CRISP-DM
    '''

    # Mostra o texto na página
    st.markdown(texto_descricao_solucao)

def compreensao_negocio():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Background</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_background = '''
        - Mercado de e-commerce cada vez mais concorrido:
            - Maior oferta e diversidade de opções 
            - Clientes podem rapidamente encontrar informações relevantes sobre suas demandas
        - Entender o comportamento do público
        - Definir estratégias competitivas
        - Ser acurado na identificação de campanhas atrativas para diferentes grupos 
            - Peça-chave na prospecção e fidelização de clientes 

        - Grupo Renner: um dos players mais importantes no país
            - Busca ser referência no uso de dados para inteligência de mercado
            - Alinhando tecnologia aos produtos de moda, decoração, financeiro e serviços
    '''

    # Mostra o texto na página
    st.markdown(texto_background)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Objetivos de Negócio</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_objetivos_negocio = '''        
        - Encontrar agrupamentos de clientes com base no estágio de vida e padrão de consumo
        - Buscar identificar quais produtos e canais são mais aderentes ao seus gostos
        - Hipótese: estes segmentos refletem necessidades e preferências distintas, permitindo:
            - Campanhas de marketing mais direcionadas e personalizadas
            - Estratégias de vendas otimizadas
    '''

    # Mostra o texto na página
    st.markdown(texto_objetivos_negocio)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Critérios de Sucesso</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_criterios_negocio = '''
        - Técnico:
            - Métricas consolidadas para avaliação dos clusters
            - Capacidade de representar segmentos distintos de clientes baseado nas características comuns entre indivíduos de um mesmo cluster. 

        - Negócio: 
            - Clusters explicáveis e coerentes, com caracterização clara de similaridade e diferenciação. 
            - Resultados e características dos clusters coerentes e alinhados com as expectativas da Renner. 
        '''

    # Mostra o texto na página
    st.markdown(texto_criterios_negocio)

def eda():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Análise Exploratória</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_analise_exp = '''
        - Objetivo principal: entender a distribuição, características e particularidades dos dados
        - Para garantir um melhor entendimento e possibilitando o grupo a escolher as melhores abordagens para serem aplicadas tanto ne preparação, quanto na modelagem do problema. 

        Abaixo, algumas observações feitas pelo grupo:
    '''

    # Mostra o texto na página
    st.markdown(texto_analise_exp)

    # Insere uma imagem na página
    st.image('dist_idade_clientes.png', use_column_width=True)

    # Cria o texto da página
    texto_idade = '''
        - Casos com idade negativa
            - Análise dos valores indicou que podem ser facilmente tratados tomando-se o valor absoluto das idades
    '''

    # Mostra o texto na página
    st.markdown(texto_idade)

    # Insere uma imagem na página
    st.image('dist_genero_clientes.png', use_column_width=True)

    # Cria o texto da página
    texto_idade = '''
        - Grande predominância de clientes do sexo feminino, o que era esperado considerando as tendências de clientes do negócio da organização parceira
    '''

    # Mostra o texto na página
    st.markdown(texto_idade)

    # Insere uma imagem na página
    st.image('dist_cidades.png', use_column_width=True)

    # Cria o texto da página
    texto_cidades = '''
        - São Paulo e Rio de Janeiro representam 20% do número total de clientes
        - Adicionando-se Porto Alegre e Brasília obtém-se pouco mais de 25%, o que demonstra como as duas primeiras cidades possuem grande representatividade no dataset
    '''

    # Mostra o texto na página
    st.markdown(texto_cidades)

    # Insere uma imagem na página
    st.image('eventos_navegacao.png', use_column_width=True)

    # Cria o texto da página
    texto_eventos = '''
        - Predominante a presença dos eventos 'view_item' e 'select_item', tendo os demais eventos poucos registros
    '''

    # Mostra o texto na página
    st.markdown(texto_eventos)

    # Insere uma imagem na página
    st.image('tipo_venda.png', use_column_width=True)

    # Cria o texto da página
    texto_tipo_vendas = '''
        - Grande diferença de registros quando comparadas compras Online e Offline
        - Vendas Online representam em torno de 1/3 do total de vendas 
    '''

    # Mostra o texto na página
    st.markdown(texto_tipo_vendas)

    # Insere uma imagem na página
    st.image('valor_por_categoria.png', use_column_width=True)

    # Cria o texto da página
    texto_valores = '''
        - Os valores das vendas por categoria têm certo equilíbrio nos dados
        - Porém, ainda existem muitos outliers que deverão ser tratados 
    '''

    # Mostra o texto na página
    st.markdown(texto_valores)

    # Insere uma imagem na página
    st.image('itens_mais_vendidos.png', use_column_width=True)

    # Cria o texto da página
    texto_top10_total = '''
        - Avaliando os 10 itens com maior valor total em vendas, podemos perceber que há um item com Código 108799 que possui valor total acima de 2 milhões de reais
            - O segundo item que mais vende (Código 77850) possui um total de pouco mais de 115 mil reais
            - Supõe-se que possa haver algum tipo de erro para o primeiro caso que deverá ser tratado
    '''

    # Mostra o texto na página
    st.markdown(texto_top10_total)


def etl():
    # Cria o título da página
    st.markdown("<h1 style='color: #FF0000;'>Renner ReThink.</h1>", unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>ETL</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_etl = '''
        - Casos com idade negativa:
            - Valor absoluto destas idades 
        - Nova distribuição dos valores ficou conforme abaixo: 
    '''

    # Mostra o texto na página
    st.markdown(texto_etl)

    # Insere uma imagem na página
    st.image('dist_idades_corrigida.png', use_column_width=True)

    # Cria o texto da página
    texto_idade_corrigida = '''
        - Verificamos 23 clientes cuja data da primeira compra na Renner estava registrada como posterior a data da última compra
        - Fizemos a inversão dos registros para corrigir o problema
    '''

    # Mostra o texto na página
    st.markdown(texto_idade_corrigida)

    # Insere uma imagem na página
    st.image('intervalo_entre_compras.png', use_column_width=True)


def feature_engineering():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Feature Engineering</h3>", unsafe_allow_html=True)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Criação de atributos e registros</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_fe = '''
        Foi verificado que um mesmo item possuía diversos valores de venda e para tentar entender melhor esse comportamento, criamos um dataset auxiliar em que capturamos o preço mínimo, médio, máximo e a moda do preço para cada item. 
        Com essas informações, pudemos calcular o desvio padrão, amplitude e coeficiente de variação de cada um dos itens, totalizando 186.127 itens. 
        
        Com objetivo de reduzir outliers, aplicamos as seguintes regras em sequência: 

        - Descartar Itens com moda do preço menor do que R$1,00. 
        - Descartar itens com desvio padrão calculado a partir de 1,5. 

        Na base de clientes criamos métricas para cada indivíduo, com dados de contagem de comprar por modalidade e por tipo de produto. Calculamos a diferença entre a primeira e a última compra, total de compras, tempo médio entre compras e ticket médio. Além disso, fizemos uma classificação se este cliente é de uma capital ou não. 

        Para os registros de navegação, aplicamos somente dados de contagem de cada evento por cliente. 
    '''

    # Mostra o texto na página
    st.markdown(texto_fe)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Integração de dados</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_integracao= '''
        Como recebemos bases com 3 perspectivas diferentes (Cliente, Navegação, Transação), utilizamos como chave primária em todas elas o campo id_cliente, dessa forma, foi possível unir todas as tabelas e criar um dataset completo com foco nos clientes, seus dados e características agregadas. 

        Após as junções, totalizamos 23.664 clientes diferentes.  
    '''

    # Mostra o texto na página
    st.markdown(texto_integracao)


def modelagem():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Modelagem</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_modelagem = '''
        Como uma das estratégias utilizadas para a clusterização, decidimos utilizar o score RFM para segmentar os consumidores em perfis de consumo. 
        O score RFM é uma métrica amplamente utilizada dentro de setores de marketing para entender perfis de clientes, e assim traçar estratégias adequadas. 
        Também é utilizado em diversos resultados estado-da-arte para segmentação de clientes nos mais diversos domínios de consumo. 
        O cálculo do score se dá pela concatenação de 3 métricas, representando Recência (o quão recente o cliente comprou um produto), Frequência (qual a quantidade de compras esse cliente fez), e monetário (o valor que essa cliente gasta em suas compras). 
        Cada uma dessas métricas é escalada dentro de uma faixa de valores (a definir dependendo da estratégia utilizada) e sua concatenação resulta no score RFM. 
	    A partir da geração desse score para cada uma das três métricas, é possível criar grupos (clusters) baseados em clientes que entram em determinadas faixas de valores. Para a criação dos clusters, nos baseamos na metodologia adotada pelo artigo publicado pelo site OmniConverter. 
        Nesta metodologia, os autores constroem grupos de clientes em uma analogia com status de relacionamento, onde clientes podem apresentar diversos perfis, a serem detalhados mais abaixo. 
        Tais clusterizações, além de fornecerem um perfil pré-traçado, permite o desenvolvimento de estratégias de marketing e fidelização visando tais grupos. 
        Abaixo destacamos os grupos criados e possíveis análises sobre eles: 
    '''

    # Mostra o texto na página
    st.markdown(texto_modelagem)

    # Cria o texto da página
    texto_modelagem = '''
    - Soulmates: Cluster dedicado aos clientes ideais que compram com frequência e gastam bem. É essencial manter seu engajamento com experiências positivas, monitorar sua contribuição para a receita e garantir que se sintam valorizados com um atendimento especial. 

    - Lovers: São clientes promissores que você deseja transformar em Soulmates. Para isso, é preciso entender suas dificuldades e oferecer valor em cada interação, aumentando a frequência de compras e a confiança na marca. 

    - New Passions: são novos clientes com alto potencial de compra. Se bem tratados, podem se tornar Lovers ou Soulmates. É importante evitar a típica perda de 70-85% desses clientes após o primeiro pedido, analisando seu comportamento e ajustando a jornada do cliente. Para reter esses clientes, pode ser interessante se implementar um processo de onboarding que inclua medições de experiência, suporte direto e uma melhor experiência de unboxing, além de usar feedback do Net Promoter Score para construir confiança e resolver problemas rapidamente. 

    - Flirting: são novos clientes que fizeram sua primeira compra, mas não tão recentemente e com menor valor. Mas apenas o fato deste cluster não ter um score de frequência alto não significa que não podem trazer mais valor no longo prazo. Eles apenas podem não ter tido a oportunidade de comprar mais vezes. Para retê-los, é importante aplicar as lições aprendidas com Soulmates e Lovers. Se não forem engajados, esses clientes podem ser classificados como "About to Dump You" devido à queda na frequência de compras. Assim, um processo de onboarding que construa confiança e ofereça valor é essencial, mantendo o foco nos clientes certos nos momentos certos. 

    - Apprentice: É um segmento de clientes que fez 1-2 compras de baixo valor, mas ainda pode ter potencial para gastar mais. Esses clientes são cautelosos, pois não desenvolveram confiança na marca e podem comprar em concorrentes. Em decorrência de não termos muitos dados sobre esse tipo de cliente, a melhor maneira de abordar ele pode ser com conversas, que podem trazer valiosos insights para o negócio. 

    - Platonic Friends: São clientes ativos que fazem um número moderado de pedidos de valor médio. 

    - Potential Lovers: São clientes recém adquiridos com maior potencial de virarem Soulmates. 

    - About to Dump You: É um segmento de clientes inativos que não compram há algum tempo; eles têm uma pontuação de Recência de 2-3 e uma frequência e valor monetário de 1 a 5. É crucial identificar os clientes com maior valor e frequência e entender por que eles pararam de comprar. Realize análises detalhadas sobre os produtos adquiridos, categorias preferidas e feedbacks anteriores para compreender suas motivações. Para engajar novamente este grupo pode ser necessário elaborar campanhas de reativação utilizando os mesmos canais pelos quais eles compraram antes, buscando sempre abordar suas experiências de forma respeitosa e evitando abordagens puramente transacionais.  

    - Ex Lovers: São clientes que tinham alta frequência e valor de compras, mas abandonaram a marca, frequentemente devido à baixa qualidade dos produtos ou frustrações. Embora o desejo seja reconquistá-los, é importante entender os motivos da separação para oferecer um fechamento significativo. Coletar feedback sobre o que desagrada esses clientes é crucial para aprimorar a estratégia da marca a longo prazo, reconhecendo que nem sempre é possível retomar a relação. 

    - Don Juan: São clientes que fizeram uma ou poucas compras de alto valor, mas nunca retornaram; é crucial entender por que isso aconteceu. O objetivo é reengajá-los em uma conversa, buscando feedback sobre sua experiência para identificar onde e qual foi o problema na jornada do cliente. Essas informações são valiosas para melhorar o processo de compra e aumentar a probabilidade de novas compras futuras. 

    - Break-Ups: São clientes de baixo valor que compraram poucas vezes, têm alta taxa de devolução e só compram quando incentivados por descontos. Este segmento geralmente faz parte da taxa natural de churn de 15-25%, e não é necessário buscar fechamento como nos Ex-Lovers. O foco deve ser em entender seu comportamento e padrões de compra, monitorando a experiência em todos os canais. Aceitar a saída desses clientes pode ser benéfico, permitindo que você concentre recursos em segmentos mais promissores. 
    '''

    # Mostra o texto na página
    st.markdown(texto_modelagem)

    # Dados da tabela
    data = {
        "Grupo": ["Soulmates", "Lovers", "New Passions", "Flirting", "Apprentice", "Platonic Friends", "Potencial Lovers"],
        "Score de Recência": ["5", "4-5", "5", "4", "4", "3-4", "5"],
        "Score de Frequência": ["5", "3-5", "1", "1", "1", "3", "1"],
        "Score Monetário": ["5", "3-5", "4-5", "4", "1", "3-4", "5"]
    }

    # Criar DataFrame
    df = pd.DataFrame(data)

    # Exibir a tabela no Streamlit
    st.table(df.style.hide(axis="index"))

def conclusao():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Conclusão</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_conclusao = '''
        Com base nos resultados obtidos, podemos concluir que a segmentação de clientes permite uma melhor personalização das estratégias de marketing, aumentando o engajamento e a satisfação dos clientes.
        
        O arquivo a seguir contém o relatório final do projeto:
    '''

    # Mostra o texto na página
    st.markdown(texto_conclusao)
    
    # Função para exibir PDF
    file = 'C:\\Users\\ferre\\OneDrive\\PUCRS\\ProjetoEmCienciaDeDadosI\\Renner_Rethink\\ProjCD - Relatorio de Andamento.pdf'

    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display =  f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 800px;">"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def segmentacao_final():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Segmentação Final</h3>", unsafe_allow_html=True)

    # Cria o texto da página    
    texto_segmentacao = '''
        A segmentação final dos clientes foi realizada com sucesso, agrupando-os em cinco categorias distintas com base em características comportamentais.

        Exemplo de código para visualização dos segmentos:
    '''

    # Mostra o texto na página
    st.markdown(texto_segmentacao)