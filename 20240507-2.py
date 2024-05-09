import gradio as gr
from transformers import pipeline

# Load Model
classifier = pipeline("text-classification", model="distilbert-base-uncased")

def classify_text(text):
    result = classifier(text)
    label = result[0]['label']
    score = result[0]['score']
    return f"Label: {label}, Confidence (0-1): {score:.4f}"

iface = gr.Interface(
    fn=classify_text,
    inputs=gr.Textbox(lines=5, max_lines=100, label="Enter Your Text here !!"),
    outputs="text",
    title="text classification",
    description="positive / negative",
    theme="compact"
)

iface.launch()

