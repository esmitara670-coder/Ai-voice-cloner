import gradio as gr
from TTS.api import TTS
import os

# GPU te XTTS v2 (Advanced Voice Cloning) model load kora hocche
print("AI Model Load hocche, ektu shomoy lagbe...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

def generate_voice(dialogue, reference_audio, emotion):
    # Emotion jure dewa hocche (AI eta pore bujhte parbe kemon tone hobe)
    prompt_text = f"[{emotion}] {dialogue}"
    output_filename = "final_dialogue.wav"
    
    # AI ke diye voice generate kora
    tts.tts_to_file(
        text=prompt_text,
        file_path=output_filename,
        speaker_wav=reference_audio,
        language="hi" # 'hi' mane Hindi/Hinglish support korbe. English er jonno 'en' dite paro.
    )
    return output_filename

# Mobile er jonno UI (User Interface) toiri kora
ui = gr.Interface(
    fn=generate_voice,
    inputs=[
        gr.Textbox(lines=3, label="Dialogue likho (Hinglish/Hindi)", placeholder="Tumi ki jano er porinam ki hote pare?"),
        gr.Audio(type="filepath", label="Reference Voice (Tomar golar 10 second MP3)"),
        gr.Dropdown(choices=["Normal", "Angry", "Whispering", "Sad", "Suspenseful", "Excited"], label="Emotion/Tone", value="Normal")
    ],
    outputs=gr.Audio(type="filepath", label="Generated Audio File"),
    title="Atom Stickman - Voice Cloner Studio",
    description="Tomar reference audio upload koro, dialogue likho, aar emotion select koro."
)

# share=True thakle Colab theke tomar phone e public link asbe
ui.launch(share=True)
