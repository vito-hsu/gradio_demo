import gradio as gr
from transformers import pipeline

classifier      = pipeline("text-classification")

text_generator  = pipeline("text-generation")

summarizer      = pipeline("summarization")          # default model="t5-base"

def classify_text(text):
    result = classifier(text)
    label = result[0]['label']
    score = result[0]['score']
    return f"Label: {label}, Confidence: {score:.4f}"


def generate_text(prompt):
    generated_text = text_generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    return generated_text


def summarize_text(text):
    summarized_text = summarizer(text)[0]['summary_text']
    return summarized_text


def combind(text1, prompt, text2):
    return classify_text(text1), generate_text(prompt), summarize_text(text2)


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input1 = gr.Text(label="Input Area for Classification")
            output1 = gr.Text(label="Output Area for Classification")
        with gr.Column():
            input2 = gr.Text(label="Input Area for Generation")
            output2 = gr.Text(label="Output Area for Generation")
        with gr.Column():
            input3 = gr.Text(label="Input Area for Summarization")
            output3 = gr.Text(label="Output Area for Summarization")
    btn = gr.Button("Start")
    btn.click(combind, inputs=[input1, input2, input3], outputs=[output1, output2, output3])


demo.launch()

# git config --global user.email "garraypierce@gmail.com"
# git config --global user.name "Vito Hsu"
# git init
# git remote add origin https://github.com/vito-hsu/gradio_demo.git
# git add .
# git commit -m "for_gradio"
# git push origin main