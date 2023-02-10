import gradio as gr
from speechbrain.pretrained import SpeakerRecognition
verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")

def detect_matching(file_wav_1,file_wav_2):
  score_match, same_person = verification.verify_files(file_wav_1,file_wav_2)
  text1 = "El score que se tiene es de %.2f" % (score_match.numpy()[0]) 
  text2 = "Pertenece aa la misma persona" if same_person.numpy()[0] else "Son distintas personaas"
  return (text1,text2)

def main():
  interface = gr.Interface(fn=detect_matching, inputs=[
              gr.Audio(source="microphone", type="filepath"),
              gr.Audio(source="microphone", type="filepath"),
          ], outputs=["text","text"])
  interface.launch(server_name="0.0.0.0",server_port=7860)

if __name__ == "__main__":
  main()