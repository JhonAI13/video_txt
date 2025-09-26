import os
import subprocess
import whisper
from whisper.utils import get_writer
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

def extrair_audio(video_path, audio_path):
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vn',
        '-ac', '1',
        '-ar', '16000',
        '-f', 'wav',
        audio_path
    ]
    subprocess.run(command, check=True, capture_output=True)

def processar_video(caminho_video, model):
    pasta_base = os.path.dirname(caminho_video)
    nome_arquivo = os.path.basename(caminho_video)
    nome_base = os.path.splitext(nome_arquivo)[0]
    
    # Criar pastas de saída
    pasta_legendas = os.path.join(pasta_base, 'Legendas')
    os.makedirs(pasta_legendas, exist_ok=True)
    
    # Caminhos temporários
    audio_temp = os.path.join(pasta_base, f"temp_{nome_base}.wav")
    
    try:
        # Extrair áudio
        print(f"[{nome_base}] Extraindo áudio...")
        extrair_audio(caminho_video, audio_temp)
        
        # Transcrever
        print(f"[{nome_base}] Transcrevendo...")
        resultado = model.transcribe(
            audio_temp,
            language='pt',
            fp16=False  # Força uso de CPU
        )
        
        # Gerar arquivos
        print(f"[{nome_base}] Salvando resultados...")
        writer = get_writer("all", pasta_legendas)
        writer(resultado, nome_base)
        
    finally:
        # Limpar temporários
        if os.path.exists(audio_temp):
            os.remove(audio_temp)

def main():
    # Configurações
    pasta_videos = r"C:\Users\jonat\Documents\GitHub\video_txt\videos - Copia - Copia"
    modelo = 'tiny'  # Use 'tiny' para CPU
    
    # Carregar modelo
    print("Carregando modelo Whisper...")
    model = whisper.load_model(modelo)
    
    # Processar vídeos
    for video in os.listdir(pasta_videos):
        if video.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
            caminho = os.path.join(pasta_videos, video)
            processar_video(caminho, model)
            print(f"\n{'-'*40}\n")

if __name__ == "__main__":
    main()