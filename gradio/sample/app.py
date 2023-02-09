import gradio as gr

def greet(your_name):
  return "Hello " + your_name + "!"

def main():
  interface = gr.Interface(fn=greet, inputs="text", outputs="text")
  interface.launch(server_name="0.0.0.0",server_port=7000)
  
if __name__ == "__main__":
  main()