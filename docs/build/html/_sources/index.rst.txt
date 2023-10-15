.. Trabalho_LP_A1 documentation master file, created by
   sphinx-quickstart on Sat Oct 14 15:32:52 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bem-vindo(a) à documentação do projeto Trabalho_LP_A1
=====================================================

O presente projeto possui as seguintes pastas:

* **dados**: Contém os arquivos .csv com os dados analisados.
* **data_analysis_functions**: Contém os módulos com as funções de análise de dados chamadas no arquivo `main`.
* **drafts**: Contém rascunhos do desenvolvimento do projeto.
* **graphs**: Contém as imagens dos gráficos finais do trabalho, gerados pela `main`.
* **graphs_functions**: Contém os módulos com as funções para a geração dos gráficos da pasta `graphs`. Essas funções também foram chamadas na `main`.
* **unittests**: Contém os arquivos com os testes unitários de todas as funções do projeto.

Além disso, na pasta raiz, existem os seguintes arquivos:

* **df_generator_functions**: Contém as funções de leitura, limpeza e manipulação dos dados para a geração dos dataframes utilizados nas análises e visualizações da `main`. Essas funções foram chamadas no arquivo `df_generator`.
* **df_generator**: Chama as funções do módulo `df_generator_functions` para geração dos dataframes utilizados na `main`.
* **index**: HTML da página inicial de apresentação do projeto.
* **main**: Chama todas as funções dos módulos de análise da pasta `data_analysis_functions` e dos módulos de plotagem de gráficos da pasta `graphs_functions` e os dataframes gerados no `df_generator` para efetivamente realizar a análise dos dados e a geração dos gráficos.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   data_analysis
   df_generator
   graphs

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
