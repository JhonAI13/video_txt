import os

def remover_linhas_consecutivas_duplicadas(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        # Filtra linhas consecutivas duplicadas
        linhas_filtradas = []
        linha_anterior = None
        for linha in linhas:
            if linha != linha_anterior:
                linhas_filtradas.append(linha)
                linha_anterior = linha
        
        # Verifica se houve alterações
        if len(linhas_filtradas) == len(linhas):
            return False, None  # Nenhuma alteração necessária
        
        # Sobrescreve o arquivo com as alterações
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.writelines(linhas_filtradas)
        
        return True, None
    
    except Exception as e:
        return False, str(e)

def main():
    diretorio = r'C:\Users\jonat\Documents\GitHub\video_txt\Legendas'
    
    if not os.path.isdir(diretorio):
        print("Diretório inválido ou não encontrado.")
        return
    
    # Listar todos os arquivos .txt
    arquivos_txt = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.txt'):
                caminho_completo = os.path.join(raiz, arquivo)
                arquivos_txt.append(caminho_completo)
    
    if not arquivos_txt:
        print("Nenhum arquivo .txt encontrado.")
        return
    
    print(f"Encontrados {len(arquivos_txt)} arquivos .txt.")
    confirmacao = input("Deseja remover linhas duplicadas consecutivas? (s/n): ").strip().lower()
    
    if confirmacao != 's':
        print("Operação cancelada.")
        return
    
    # Processar arquivos
    modificados = 0
    erros = 0
    inalterados = 0
    
    for arquivo in arquivos_txt:
        alterado, erro = remover_linhas_consecutivas_duplicadas(arquivo)
        if erro:
            print(f"Erro em {arquivo}: {erro}")
            erros += 1
        else:
            if alterado:
                print(f"Modificado: {arquivo}")
                modificados += 1
            else:
                inalterados += 1
    
    print(f"\nConcluído: {modificados} arquivos modificados | {inalterados} inalterados | {erros} erros.")

if __name__ == "__main__":
    main()