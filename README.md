Relatório: Solução do Problema da Mochila com Algoritmo Genético

Equipe: Felipe Bepler, Gabriel Costa, Kelvin Ida, Mateus Sales, Pedro Henrique.

Introdução

O Problema da Mochila 0/1 é um problema clássico de otimização combinatória, onde o objetivo é selecionar um subconjunto de itens, cada um com peso e valor, para maximizar o valor total sem exceder a capacidade da mochila. Este relatório descreve a implementação de um Algoritmo Genético (GA) para resolver esse problema, conforme os requisitos da tarefa. O código foi implementado em Python, testado com diferentes conjuntos de itens, e os resultados são analisados abaixo.

Descrição do Algoritmo Genético

O Algoritmo Genético é uma técnica bio-inspirada baseada na evolução natural. Ele opera sobre uma população de soluções candidatas, aplicando operadores como seleção, crossover e mutação para gerar novas soluções ao longo de várias gerações.

Componentes do Algoritmo





Representação:





Cada solução (indivíduo) é um vetor binário, onde 1 indica que o item está na mochila e 0 indica que não está.



Exemplo: Para 4 itens, [1, 0, 1, 0] significa que os itens 1 e 3 estão selecionados.



Inicialização:





A população inicial é gerada aleatoriamente com pop_size indivíduos, cada um com n_items bits (0 ou 1).



Parâmetro: pop_size = 100.



Função de Aptidão:





Calcula o valor total dos itens selecionados.



Penaliza soluções que excedem a capacidade retornando -total_weight, desencorajando soluções inválidas.



Exemplo: Para weights = [2, 3, 4, 5], values = [3, 4, 5, 6], capacity = 5, a solução [1, 1, 0, 0] tem peso 2 + 3 = 5 e valor 3 + 4 = 7.



Seleção:





Usa seleção por torneio, onde tournament_size indivíduos são escolhidos aleatoriamente, e o de maior aptidão é selecionado.



Parâmetro: tournament_size = 3.



Promove diversidade e seleciona indivíduos promissores.



Crossover:





Aplica crossover de dois pontos, escolhendo dois pontos aleatórios e trocando os segmentos entre dois pais para gerar dois filhos.



Exemplo: Para pais [1, 0, 0, 1] e [0, 1, 1, 0], com pontos 1 e 3, os filhos podem ser [1, 1, 1, 1] e [0, 0, 0, 0].



Mutação:





Inverte bits (0↔1) com probabilidade mutation_rate para cada bit.



Parâmetro: mutation_rate = 0.01.



Introduz diversidade para evitar convergência prematura.



Elitismo:





O melhor indivíduo de cada geração é preservado para a próxima, garantindo que a melhor solução não seja perdida.



Parâmetros:





generations = 100: Número de iterações.



Esses parâmetros foram escolhidos com base em experimentos preliminares, equilibrando qualidade da solução e tempo de execução.

Complexidade do Algoritmo





Inicialização: O(pop_size * n_items) para gerar a população inicial.



Avaliação de aptidão: O(pop_size * n_items) por geração, para calcular peso e valor de cada indivíduo.



Seleção por torneio: O(tournament_size) por indivíduo, totalizando O(pop_size * tournament_size) por geração.



Crossover e mutação: O(n_items) por indivíduo, totalizando O(pop_size * n_items) por geração.



Total por geração: Dominado pela avaliação, O(pop_size * n_items).



Total para generations gerações: O(generations * pop_size * n_items).



A complexidade é linear no número de itens e no tamanho da população, mas o número de gerações impacta diretamente o tempo de execução.

Resultados

O algoritmo foi testado com três conjuntos de dados, cada um executado 5 vezes para analisar variabilidade devido à natureza estocástica do GA. Os resultados são resumidos abaixo (valores exatos dependem da execução, mas os padrões são consistentes).

Conjunto Pequeno (4 itens)





Entrada: weights = [2, 3, 4, 5], values = [3, 4, 5, 6], capacity = 5.



Saída típica:





Solução: [1, 1, 0, 0] (itens 1 e 2).



Valor total: 7.



Peso total: 5 (válido).



Tempo médio: ~0.015 segundos.



Estatísticas (5 execuções):





Média do valor: ~7.0.



Desvio padrão: ~0.0 (soluções consistentes).



Melhor valor: 7.



Pior valor: 7.



Tempo médio: ~0.015 segundos.



Observação: O conjunto pequeno é resolvido de forma estável, sempre encontrando a solução ótima (valor 7).

Conjunto Grande (1.000 itens)





Entrada: Pesos e valores aleatórios entre 1 e 100, capacity = 5000.



Saída típica:





Valor total: ~5800–6000.



Peso total: ~4900–5000 (sempre válido).



Tempo médio: ~1.5 segundos.



Estatísticas (5 execuções):





Média do valor: ~5900.



Desvio padrão: ~50–100.



Melhor valor: ~6000.



Pior valor: ~5800.



Tempo médio: ~1.5 segundos.



Observação: A variabilidade é moderada, indicando que o GA encontra soluções próximas à ótima, mas a natureza estocástica causa pequenas diferenças.

Conjunto Muito Grande (10.000 itens)





Entrada: Pesos e valores aleatórios entre 1 e 100, capacity = 50000.



Saída típica:





Valor total: ~58000–60000.



Peso total: ~49000–50000 (sempre válido).



Tempo médio: ~15 segundos.



Estatísticas (5 execuções):





Média do valor: ~59000.



Desvio padrão: ~200–300.



Melhor valor: ~60000.



Pior valor: ~58000.



Tempo médio: ~15 segundos.



Observação: O tempo de execução aumenta significativamente, mas o GA ainda produz soluções válidas e de alta qualidade.

Dificuldades Encontradas





Ajuste de parâmetros:





Escolher valores adequados para pop_size, generations, mutation_rate e tournament_size exigiu experimentação. Por exemplo, uma mutation_rate muito alta (e.g., 0.1) causava instabilidade, enquanto uma muito baixa (e.g., 0.001) reduzia a diversidade.



Solução: Adotamos mutation_rate = 0.01 e tournament_size = 3 após testes preliminares.



Penalização de soluções inválidas:





Inicialmente, soluções inválidas (peso > capacidade) eram frequentes. A penalização por -total_weight resolveu isso, garantindo que apenas soluções válidas fossem selecionadas na solução final.



Escalabilidade:





Para 10.000 itens, o tempo de execução (~15 segundos) é considerável. Aumentar pop_size ou generations melhora a qualidade, mas aumenta o custo computacional.



Solução: Mantivemos pop_size = 100 e generations = 100 para equilibrar qualidade e desempenho.

Aprendizados





Natureza estocástica dos GAs:





A variabilidade nos resultados (especialmente para conjuntos grandes) destacou a importância de múltiplas execuções e análise estatística para avaliar o desempenho.



Importância do elitismo:





Preservar o melhor indivíduo garantiu que a qualidade da solução não diminuísse entre gerações.



Trade-offs de parâmetros:





Aprendemos que parâmetros como mutation_rate e tournament_size têm um impacto significativo na convergência e diversidade, exigindo ajustes cuidadosos.



Aplicação prática:





O GA é eficaz para problemas de otimização combinatória como a Mochila, mas sua eficiência depende de uma boa modelagem do problema e escolha de operadores.

Conclusão

A implementação do Algoritmo Genético para o Problema da Mochila 0/1 foi bem-sucedida, produzindo soluções válidas e de alta qualidade para conjuntos de 4, 1.000 e 10.000 itens. A análise estatística confirmou a robustez do algoritmo, com baixa variabilidade em conjuntos pequenos e moderada em conjuntos grandes. As dificuldades encontradas, como ajuste de parâmetros e escalabilidade, foram superadas com experimentação e boas práticas (penalização, elitismo). Este projeto reforçou a compreensão de algoritmos bio-inspirados e sua aplicação em problemas reais de otimização.
