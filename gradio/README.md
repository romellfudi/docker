# Gradio
docker build . -t streamlit_gradio
docker run -it -p 7000:7000 streamlit_gradio
docker run --rm -it -p 7000:7000 streamlit_gradio