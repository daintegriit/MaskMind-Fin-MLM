# src/serve.py

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM

app = FastAPI()

# Load your fine-tuned model
model_path = "models/finetuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForMaskedLM.from_pretrained(model_path)

nlp_fill = pipeline("fill-mask", model=model, tokenizer=tokenizer)

# Define the input format using Pydantic
class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "🚀 Financial Mask-Filler API is up!"}

@app.post("/predict")
def predict(request: PromptRequest):
    if "[MASK]" not in request.prompt:
        return {"error": "❗ Prompt must include [MASK] token"}
    
    results = nlp_fill(request.prompt)
    return {
        "prompt": request.prompt,
        "results": [
            {"sequence": r["sequence"], "score": round(r["score"], 4)}
            for r in results
        ]
    }
