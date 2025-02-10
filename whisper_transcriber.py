import whisper
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def transcribe_audio(audio_path):
    try:
        print(f"\n🔹 Transcrevendo o áudio: {audio_path}")  # Debug no console
        model = whisper.load_model("small")  # Carregar modelo
        result = model.transcribe(audio_path)
        print("\n✅ Transcrição concluída!\n")  # Debug
        print(result["text"])  # Exibir a transcrição no console
        return result["text"]
    except Exception as e:
        print(f"\n❌ Erro ao transcrever: {e}")  # Exibir erro no console
        return None

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.m4a;*.ogg")])

    if not file_path:
        print("\n⚠ Nenhum arquivo foi selecionado.")  # Debug no console
        return
    
    print("\n⏳ Transcrição iniciada...")  # Mensagem no console

    transcription = transcribe_audio(file_path)

    if transcription:
        # Salvar transcrição na mesma pasta do áudio
        output_file = file_path + ".txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcription)

        messagebox.showinfo("Sucesso", f"✅ Transcrição salva em:\n{output_file}")
        print(f"\n✅ Transcrição salva com sucesso em: {output_file}")  # Debug no console
    else:
        messagebox.showerror("Erro", "❌ A transcrição falhou.")
        print("\n❌ Erro ao transcrever o arquivo.")  # Debug no console

if __name__ == "__main__":
    select_file()
