import warnings

warnings.simplefilter("ignore")
import gradio as gr
from speechbrain.pretrained import SpeakerRecognition

verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec-ecapa-voxceleb",
)


def detect_matching(file_wav_1, file_wav_2):
    score_match, same_person = verification.verify_files(file_wav_1, file_wav_2)
    text1 = "El score que se tiene es de %.2f" % (score_match.numpy()[0])
    text2 = (
        "Pertenece a la misma persona"
        if same_person.numpy()[0]
        else "Son distintas personas"
    )
    return (text1, text2)


def main():
    interface = gr.Interface(
        fn=detect_matching,
        inputs=[
            gr.Audio(label="Canal 1 de Audio", source="microphone", type="filepath"),
            gr.Audio(label="Canal 2 de Audio", source="microphone", type="filepath"),
        ],
        outputs=[
            gr.Text(label="Score"),
            gr.Text(label="Ambos audio pertenecen a la misma persona?"),
        ],
        allow_flagging="never",
        css="footer {visibility: hidden}",
    )
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        auth=("romell", "romell"),
        favicon_path="favicon.ico",
        auth_message="Ingresar Credenciales proporcionadas por BOOSTTAG",
    )


if __name__ == "__main__":
    main()
