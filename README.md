## GRUPO 2
Arthur Salvador Rocha<BR>
Guilherme Nakano Nalin<BR>
Lucas Gabriel Mendes de Oliveira<BR>
Patricia Yoshie Kishi Bueno<BR>
Paulo Gustavo Maciel Lopes

# RAMster Trade

### Descrição
O objetivo é criar um robô para operar criptomoedas em uma plataforma simulada Trei Dimais
(https://cripto-dash.herokuapp.com/). Nesta plataforma, todas as transações são fictícias,
envolvendo apenas valores simulados. Apesar disso, todas as cotações das criptomoedas são
consultadas em tempo real, o que permite que os alunos sejam livres para criarem features que
envolvam variáveis externas, como notícias, sentimentos em redes sociais, variáveis
macroeconômicas etc.

### Por que esse trabalho?
O objetivo é resolvermos um problema de série temporal, deixando os alunos livres para escolherem a
técnica. Posto desta maneira, este trabalho pode ser realizado utilizando:
• Modelos tradicionais de Machine Learning, como o template fornecido
• Modelos tradicionais de séries temporais, como ARIMA
• Modelos de Deep Learning
• Modelos de Redes Recorrentes, como LSTM ou GRU
Além de ser um trabalho que permite uma ampla gama de estratégias e modelos, é um bom exemplo de
modelos reais em produção. Além disso, deixa clara a dificuldade que é criar soluções para operar ativos
de maneira automática.

### Por onde começar
#### 1. Criação do token individual
Cada um deve entrar na plataforma https://cripto-dash.herokuapp.com/ para gerar o próprio token.
Para isso, usem o menu da esquerda, preenchendo:
• O nome do robô: fique à vontade para inventar o nome, mas saiba que ele irá aparecer nos
rankings dessa página
• Descrição: opcional, é uma descrição que irá aparecer ao lado do nome
• Imagem: opcional, atualmente não utilizado
• ID de Grupo: Digitar id do grupo, conforme passado pelo professor em sala
Clique no botão “Gerar Token!”. Anote o token que aparecerá na tela. Se tiver qualquer problema,
mande um email para bernardo.aflalo@gmail.com ou uma msg no linkedin
https://www.linkedin.com/in/bernardo-aflalo-b0a26550/.

#### 2. Clone do repositório exemplo
Utilizar o template de notebook fornecido em: https://github.com/BernardoAflalo/cripto-simulator�client. Substitui o token ‘token_dummy_001’ nos notebooks pelo token que vocês geraram no passo
anterior. Leia a descrição no repositório para mais detalhes.

### Objetivo específico do trabalho
• Explorar os dados históricos das cotações das criptomoedas (1_treino_simples.ipynb)
• Criar features que possam ser relevantes para o problema. Sejam criativos! Como os dados de
cotação são reais e avaliados em tempo real, nada impede que vocês criem features baseado
em notícias, sentimentos de redes sociais etc (1_treino_simples.ipynb)
• Testar modelos diferentes, explorar diferente hiperparâmetros. Será considerado diferencial o
uso de deep learning e redes recorrentes (1_treino_simples.ipynb)
• Rodar o robô por alguns minutos, para que ele possa operar de fato no mercado. Rodar sempre
com o time.sleep(60) entre loops (2_my_robot.ipynb) para que o robô acesse a API apenas uma
vez por minuto
Para este trabalho, não é necessário criar a API final do robô (conforme notebook 3_api_robot.ipynb)!

### Avaliação
São critérios de avaliação:
• Processo de resolução do problema
• Features Criadas
• Escolha de modelos e tratamentos realizados, juntamente com as explicações
• Organização do código
Atenção: os notebooks são fornecidos para facilitar o trabalho de vocês, permitindo que vocês foquem
na modelagem, análise, backtest e geração de features! Não serão aceitos trabalhos com nenhuma ou
pouca modificação em relação ao template padrão!
