import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM

# Load Fine-tuned model
model_path = "./models/finetuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForMaskedLM.from_pretrained(model_path)
fill = pipeline("fill-mask", model=model, tokenizer=tokenizer)

# Prediction function
def predict(prompt):
    if "[MASK]" not in prompt:
        return "⚠️ Please include [MASK] somewhere in your sentence."
    
    results = fill(prompt)
    output = "\n\n".join([
        f"🔹 **Prediction:** {r['sequence']}\n🔹 **Confidence:** {r['score']*100:.2f}%"
        for r in results
    ])
    return output

# Gradio Interface
with gr.Blocks(title="MaskMind: Financial Mask-Filler MLM") as demo:
    gr.Markdown(
        """
        # <div align="center">🧠 MaskMind: Financial Mask-Filler MLM</div>

        <div align="center">Fine-tuned exclusively on <b>Apple's SEC 10-K Annual Reports</b>.</div><br><br>

        <div align="center">
        🔹 <b>Instructions:</b><br>
        Enter a financial sentence containing <b>[MASK]</b> where you want the model to predict the missing information.<br>
        Example: <i>"Apple's net income for 2023 was [MASK] billion dollars."</i><br>
        Then click <b>Generate Prediction</b> to see the results!
        </div>
        """
    )

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                label="Prompt",
                placeholder="Example: Apple's revenue for 2023 was [MASK] billion dollars."
            )
        with gr.Column():
            output = gr.Textbox(
                label="Output",
                placeholder="Your prediction results will appear here after you click Generate Prediction.",
                interactive=False  # Makes it readonly like a display box
            )

    with gr.Row():
        clear_btn = gr.Button("Clear")
        submit_btn = gr.Button("Generate Prediction")
    
    submit_btn.click(predict, inputs=[prompt], outputs=[output])
    clear_btn.click(lambda: ("", ""), inputs=[], outputs=[prompt, output])

    # Two-column layout: Suggested Examples + Expected Outputs
    with gr.Row():
        with gr.Column():
            gr.Markdown(
                """
                ## 📚 Suggested Example Prompts:

                - "Apple reported an operating [MASK] margin of 30% for the fiscal year."
                - "Revenue from [MASK] products increased significantly compared to last year."
                - "Net [MASK] for Apple in 2023 was $99.8 billion."
                - "The company’s cash [MASK] from operations was over $100 billion."
                - "Apple expects continued strong growth in [MASK] services."
                """
            )
        with gr.Column():
            gr.Markdown(
                """
                ## 📜 Expected Outputs:

                When using the examples, the model intelligently fills in the [MASK] based on Apple's 10-K data:

                - **Operating margin** → "gross", "operating", "profit", etc.
                - **Revenue from [MASK] products** → "iPhone", "Mac", "Services", "Wearables"
                - **Net [MASK]** → "income", "profit", "earnings"
                - **Cash [MASK] from operations** → "flow", "flows"
                - **Growth in [MASK] services** → "App Store", "iCloud", "Music", etc.
                """
            )

    # Centered Confidence Score Explanation
    gr.Markdown(
        """
        <div align="center">

        ## 📈 Understanding Confidence Scores:

        Each prediction comes with a **confidence score**, shown as a percentage.

        - A **higher confidence** (e.g., 80%-90%) means the model is **very certain** about its prediction.<br>
        - A **lower confidence** (e.g., 5%-15%) means the model is **less sure**, but the prediction might still make sense.<br><br>

        Confidence is calculated based on the model’s probability of choosing that particular masked word among many possibilities.

        </div>
        """,
        elem_id="centered_confidence"
    )

# Launch app
if __name__ == "__main__":
    demo.launch()
