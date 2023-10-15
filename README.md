# Trabalho_LP_A1

Trabalho referente à avaliação 1 da disciplina de Linguagens de Programação do 2º período do curso de Ciência de Dados e Inteligência Artificial da Fundação Getúlio Vargas (FGV).

Alunos:
* Maria Eduarda Mesquita Magalhães
* Mariana Fernandes Rocha
* Paula Eduarda de Lima
* Pedro Henrique Coterli

O presente projeto possui as seguintes pastas:

* `dados`: Contém os arquivos .csv com os dados analisados.
* `data_analysis_functions`: Contém os módulos com as funções de análise de dados chamadas no arquivo `main`.
* `drafts`: Contém rascunhos do desenvolvimento do projeto.
* `graphs`: Contém as imagens dos gráficos finais do trabalho, gerados pela `main`.
* `graphs_functions`: Contém os módulos com as funções para a geração dos gráficos da pasta `graphs`. Essas funções também foram chamadas na `main`.
* `unittests`: Contém os arquivos com os testes unitários de todas as funções do projeto.

Além disso, na pasta raiz, existem os seguintes arquivos:

* `df_generator_functions`: Contém as funções de leitura, limpeza e manipulação dos dados para a geração dos dataframes utilizados nas análises e visualizações da `main`. Essas funções foram chamadas no arquivo `df_generator`.
* `df_generator`: Chama as funções do módulo `df_generator_functions` para geração dos dataframes utilizados na `main`.
* `index`: HTML da página inicial de apresentação do projeto.
* `main`: Chama todas as funções dos módulos de análise da pasta `data_analysis_functions` e dos módulos de plotagem de gráficos da pasta `graphs_functions` e os dataframes gerados no `df_generator` para efetivamente realizar a análise dos dados e a geração dos gráficos.
