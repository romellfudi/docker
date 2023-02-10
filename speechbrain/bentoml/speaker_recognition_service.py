import bentoml

model_runner = bentoml.picklable_model.get(
    "speaker_recognition_score:latest"
).to_runner()

svc = bentoml.Service("voices_belong_to_same_person", runners=[model_runner])


@svc.api(input=bentoml.io.JSON(), output=bentoml.io.JSON())
async def speech_recognition(input_arr):
    return await model_runner.async_run(input_arr)
