def text_to_markdown(flashcard_text):
    """
    Converts flashcard text format to Markdown format.

    Args:
        flashcard_text: A string containing the flashcard text.

    Returns:
        A string containing the flashcard text formatted in Markdown.
    """
    markdown_output = ""
    flashcards = flashcard_text.strip().split("Flashcard ")
    for i in range(1, len(flashcards)):  # Start from 1 to skip the empty string before the first flashcard
        flashcard_content = flashcards[i].strip()
        if not flashcard_content:
            continue

        lines = flashcard_content.split('\n')
        sections = {}
        current_section = None
        for line in lines:
            line = line.strip()
            if line.startswith('('): # Skip the level indicator like "(Básico)"
                continue
            if line == 'Front':
                current_section = 'Front'
                sections[current_section] = []
            elif line == 'Input:':
                current_section = 'Input'
                sections[current_section] = []
            elif line == 'Back':
                current_section = 'Back'
                sections[current_section] = []
            elif line == 'python':
                current_section = 'python'
                sections[current_section] = []
            elif line == 'Output:':
                current_section = 'Output'
                sections[current_section] = []
            elif line == 'Explicação:':
                current_section = 'Explicação'
                sections[current_section] = []
            elif current_section:
                sections[current_section].append(line)

        flashcard_header = f"## Flashcard {i} "
        level = ""
        if "(" in flashcard_content and ")" in flashcard_content and flashcard_content.find("(") < flashcard_content.find(")"):
            start_index = flashcard_content.find("(") + 1
            end_index = flashcard_content.find(")")
            level = flashcard_content[start_index:end_index]
            flashcard_header += f"({level}) "

        markdown_output += flashcard_header.strip() + "\n\n"

        if 'Front' in sections and sections['Front']:
            markdown_output += "### Front\n" + "\n".join(sections['Front']).strip() + "\n\n"
        if 'Input' in sections and sections['Input']:
            markdown_output += "### Input\n" + "```markdown\n" + "\n".join(sections['Input']).strip() + "\n```\n\n"
        if 'Back' in sections and sections['Back']:
            markdown_output += "### Back\n" + "\n".join(sections['Back']).strip() + "\n\n"
        if 'python' in sections and sections['python']:
            markdown_output += "### python\n" + "```python\n" + "\n".join(sections['python']).strip() + "\n```\n\n"
        if 'Output' in sections and sections['Output']:
            markdown_output += "### Output\n" + "```markdown\n" + "\n".join(sections['Output']).strip() + "\n```\n\n"
        if 'Explicação' in sections and sections['Explicação']:
            markdown_output += "### Explicação\n" + "\n".join(sections['Explicação']).strip() + "\n\n"
        markdown_output += "---\n\n" # Separator between flashcards

    return markdown_output.strip()

# Example usage (assuming your provided text is in a string variable called `flashcard_text_input`)
flashcard_text_input = """Flashcard 1 (Básico)
Front
Questão: Como contar quantos produtos existem por categoria?

Input:

markdown
Copiar
Editar
|Categoria|Produto|
|---|---|
|A|Teclado|
|A|Mouse|
|A|Monitor|
Back
python
Copiar
Editar
df.groupby('Categoria').size()
Output:

markdown
Copiar
Editar
|Categoria|Count|
|---|---|
|A|3|
|B|2|
Explicação: size() conta o número total de linhas em cada grupo.

Flashcard 2 (Intermediário)
Front
Questão: Como calcular a média e a soma de vendas por categoria?

Input:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|100|
|A|200|
|B|150|
|B|250|
Back
python
Copiar
Editar
df.groupby('Categoria')['Vendas'].agg(['mean', 'sum'])
Output:

markdown
Copiar
Editar
|Categoria|mean|sum|
|---|---|---|
|A|150|300|
|B|200|400|
Explicação: A função agg() permite aplicar múltiplas funções estatísticas de uma vez.

Flashcard 3 (Intermediário)
Front
Questão: Como exibir o total de vendas sem que o índice seja alterado?

Input:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|100|
|A|200|
|B|150|
|B|250|
Back
python
Copiar
Editar
df.groupby('Categoria', as_index=False)['Vendas'].sum()
Output:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|300|
|B|400|
Explicação: as_index=False evita que a coluna de agrupamento vire índice, mantendo a estrutura original do DataFrame.

Flashcard 4 (Avançado)
Front
Questão: Como calcular a média móvel de vendas dentro de cada categoria?

Input:

markdown
Copiar
Editar
|Categoria|Data|Vendas|
|---|---|---|
|A|2024-01-01|100|
|A|2024-01-02|200|
|A|2024-01-03|300|
|B|2024-01-01|150|
|B|2024-01-02|250|
Back
python
Copiar
Editar
df['Média_Móvel'] = df.groupby('Categoria')['Vendas'].transform(lambda x: x.rolling(2).mean())
Output:

markdown
Copiar
Editar
|Categoria|Data|Vendas|Média_Móvel|
|---|---|---|---|
|A|2024-01-01|100|NaN|
|A|2024-01-02|200|150.0|
|A|2024-01-03|300|250.0|
|B|2024-01-01|150|NaN|
|B|2024-01-02|250|200.0|
Explicação: rolling(2).mean() calcula a média dos dois últimos valores em cada grupo.

Flashcard 5 (Básico)
Front
Questão: Como contar quantos pedidos cada cliente fez?

Input:

markdown
Copiar
Editar
|Cliente|Pedido|
|---|---|
|Ana|P1|
|Ana|P2|
|Bruno|P3|
|Ana|P4|
|Carlos|P5|
Back
python
Copiar
Editar
df.groupby('Cliente').size().reset_index(name='Total_Pedidos')
Output:

markdown
Copiar
Editar
|Cliente|Total_Pedidos|
|---|---|
|Ana|3|
|Bruno|1|
|Carlos|1|
Explicação: size() conta o número de ocorrências por grupo, e reset_index() transforma o resultado em DataFrame.

Flashcard 6 (Intermediário)
Front
Questão: Como calcular a venda máxima e mínima por categoria?

Input:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|100|
|A|200|
|B|150|
|B|250|
Back
python
Copiar
Editar
df.groupby('Categoria')['Vendas'].agg(['max', 'min'])
Output:

markdown
Copiar
Editar
|Categoria|max|min|
|---|---|---|
|A|200|100|
|B|250|150|
Explicação: agg(['max', 'min']) retorna os valores máximo e mínimo de cada grupo.

Flashcard 7 (Intermediário)
Front
Questão: Como calcular o número total de vendas por categoria, incluindo categorias sem vendas registradas?

Input:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|100|
|A|200|
|B|150|
|B|250|
|C|NaN|
Back
python
Copiar
Editar
df.groupby('Categoria', dropna=False)['Vendas'].count()
Output:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|2|
|B|2|
|C|0|
Explicação: count() ignora valores NaN por padrão, mas todas as categorias são mantidas com dropna=False.

Flashcard 8 (Avançado)
Front
Questão: Como encontrar a primeira venda de cada cliente?

Input:

markdown
Copiar
Editar
|Cliente|Data|Vendas|
|---|---|---|
|Ana|2024-01-02|100|
|Bruno|2024-01-01|150|
|Ana|2024-01-01|200|
|Carlos|2024-01-03|250|
|Ana|2024-01-03|300|
Back
python
Copiar
Editar
df.groupby('Cliente').apply(lambda x: x.nsmallest(1, 'Data'))
Output:

markdown
Copiar
Editar
|Cliente|Data|Vendas|
|---|---|---|
|Ana|2024-01-01|200|
|Bruno|2024-01-01|150|
|Carlos|2024-01-03|250|
Explicação: nsmallest(1, 'Data') retorna a menor data de cada grupo.

Flashcard 9 (Avançado)
Front
Questão: Como calcular a participação percentual de cada venda dentro da categoria?

Input:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|100|
|A|200|
|B|150|
|B|250|
Back
python
Copiar
Editar
df['Percentual'] = df.groupby('Categoria')['Vendas'].transform(lambda x: x / x.sum() * 100)
Output:

markdown
Copiar
Editar
|Categoria|Vendas|Percentual|
|---|---|---|
|A|100|33.3|
|A|200|66.7|
|B|150|37.5|
|B|250|62.5|
Explicação: transform() aplica a operação dentro de cada grupo, mantendo a estrutura original do DataFrame.

Flashcard 10 (Básico)
Front
Questão: Como calcular o total de vendas por mês?

Input:

markdown
Copiar
Editar
|Mês|Vendas|
|---|---|
|Jan|100|
|Jan|200|
|Fev|150|
|Fev|250|
Back
python
Copiar
Editar
df.groupby('Mês')['Vendas'].sum().reset_index()
Output:

markdown
Copiar
Editar
|Mês|Vendas|
|---|---|
|Jan|300|
|Fev|400|
Explicação: sum() calcula o total por grupo e reset_index() transforma o resultado em DataFrame.

Flashcard 11 (Intermediário)
Front
Questão: Como obter a média e a contagem de vendas por categoria?

Input:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|100|
|A|200|
|B|150|
|B|250|
Back
python
Copiar
Editar
df.groupby('Categoria')['Vendas'].agg(['mean', 'count']).reset_index()
Output:

markdown
Copiar
Editar
|Categoria|mean|count|
|---|---|---|
|A|150|2|
|B|200|2|
Explicação: agg(['mean', 'count']) retorna múltiplas estatísticas de cada grupo.

Flashcard 12 (Intermediário)
Front
Questão: Como filtrar categorias cuja soma de vendas seja maior que 300?

Input:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|100|
|A|250|
|B|150|
|B|200|
|C|50|
Back
python
Copiar
Editar
df_filtrado = df.groupby('Categoria')['Vendas'].sum().reset_index()
df_filtrado[df_filtrado['Vendas'] > 300]
Output:

markdown
Copiar
Editar
|Categoria|Vendas|
|---|---|
|A|350|
|B|350|
Explicação: O groupby().sum() calcula o total por categoria, e depois aplicamos um filtro (> 300).

Flashcard 13 (Avançado)
Front
Questão: Como calcular a diferença entre a venda de cada produto e a média de sua categoria?

Input:

markdown
Copiar
Editar
|Categoria|Produto|Vendas|
|---|---|---|
|A|P1|100|
|A|P2|200|
|B|P3|150|
|B|P4|250|
Back
python
Copiar
Editar
df['Diferença'] = df['Vendas'] - df.groupby('Categoria')['Vendas'].transform('mean')
Output:

markdown
Copiar
Editar
|Categoria|Produto|Vendas|Diferença|
|---|---|---|---|
|A|P1|100|-50|
|A|P2|200|50|
|B|P3|150|-50|
|B|P4|250|50|
Explicação: transform('mean') calcula a média dentro de cada grupo, permitindo a subtração elemento a elemento.

Flashcard 14 (Avançado)
Front
Questão: Como criar uma coluna de ranking dentro de cada categoria com base nas vendas?

Input:

markdown
Copiar
Editar
|Categoria|Produto|Vendas|
|---|---|---|
|A|P1|100|
|A|P2|200|
|B|P3|150|
|B|P4|250|
Back
python
Copiar
Editar
df['Ranking'] = df.groupby('Categoria')['Vendas'].rank(ascending=False)
Output:

markdown
Copiar
Editar
|Categoria|Produto|Vendas|Ranking|
|---|---|---|---|
|A|P2|200|1.0|
|A|P1|100|2.0|
|B|P4|250|1.0|
|B|P3|150|2.0|
Explicação: rank(ascending=False) cria um ranking dentro de cada grupo, atribuindo 1 ao maior valor.

Flashcard 15 (Avançado)
Front
Questão: Como calcular a soma acumulada das vendas por categoria?

Input:

markdown
Copiar
Editar
|Categoria|Produto|Vendas|
|---|---|---|
|A|P1|100|
|A|P2|200|
|A|P3|150|
|B|P4|250|
|B|P5|100|
Back
python
Copiar
Editar
df['Vendas_Acumuladas'] = df.groupby('Categoria')['Vendas'].cumsum()
Output:

markdown
Copiar
Editar
|Categoria|Produto|Vendas|Vendas_Acumuladas|
|---|---|---|---|
|A|P1|100|100|
|A|P2|200|300|
|A|P3|150|450|
|B|P4|250|250|
|B|P5|100|350|
Explicação: cumsum() calcula a soma acumulada dentro de cada categoria."""

markdown_output = text_to_markdown(flashcard_text_input)
print(markdown_output)