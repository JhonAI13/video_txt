import os


def main():
    # Solicitar o diretório ao usuário
    diretorio = r'C:\Users\jonat\Documents\GitHub\video_txt\Legendas'
    
    # Verificar se o diretório é válido
    if not os.path.isdir(diretorio):
        print("Diretório inválido ou não encontrado.")
        return
    
    # Listar todos os arquivos não .txt
    arquivos_para_apagar = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            extensao = os.path.splitext(arquivo)[1].lower()  # Extensão em minúsculas
            if extensao != '.txt':
                caminho_completo = os.path.join(raiz, arquivo)
                arquivos_para_apagar.append(caminho_completo)
    
    # Verificar se há arquivos para apagar
    if not arquivos_para_apagar:
        print("Nenhum arquivo não .txt encontrado.")
        return
    
    # Mostrar confirmação
    print(f"Encontrados {len(arquivos_para_apagar)} arquivos não .txt.")
    confirmacao = input("Deseja apagar todos? (s/n): ").strip().lower()
    
    if confirmacao != 's':
        print("Operação cancelada.")
        return
    
    # Apagar arquivos com tratamento de erros
    apagados = 0
    erros = 0
    
    for caminho in arquivos_para_apagar:
        try:
            os.remove(caminho)
            apagados += 1
            print(f"Apagado: {caminho}")
        except Exception as e:
            erros += 1
            print(f"Erro ao apagar {caminho}: {str(e)}")
    
    # Resumo final
    print(f"\nConcluído: {apagados} arquivos apagados, {erros} erros.")

if __name__ == "__main__":
    main()