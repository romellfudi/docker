from speechbrain.pretrained import SpeakerRecognition
from typing import Dict
import base64
import bentoml

def speaker_recognition_score(input_list: Dict[str, str]) -> Dict[str, str]:
    verification = SpeakerRecognition.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir="pretrained_models/spkrec-ecapa-voxceleb",
    )

    with open("audio1.wav", "wb") as binary_file:
        binary_file.write(base64.b64decode(input_list["audio1"]))
    with open("audio2.wav", "wb") as binary_file:
        binary_file.write(base64.b64decode(input_list["audio2"]))
    score_match, person = verification.verify_files("audio1.wav", "audio2.wav")
    return {"score": score_match.numpy()[0], "same_person": person.numpy()[0]}


if __name__ == "__main__":
    saved_model = bentoml.picklable_model.save_model(
        "speaker_recognition_score",
        speaker_recognition_score,
        signatures={"__call__": {"batchable": True}},
    )
    print(f"Model saved: {saved_model}")
