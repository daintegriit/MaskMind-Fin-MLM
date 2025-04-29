from transformers import (
    AutoModelForMaskedLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments
)
from datasets import load_from_disk
import torch
from transformers import DataCollatorForLanguageModeling


# === Config ===
model_checkpoint = "bert-base-uncased"  # change to distilbert-base-uncased or roberta-base if needed
tokenized_path = "notebooks/data/tokenized/sec_apple_10k"
output_dir = "models/finetuned_model"

# === Load dataset ===
print("📦 Loading tokenized dataset...")
dataset = load_from_disk(tokenized_path)

# === Load model and tokenizer ===
print("🧠 Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)

# === (Optional) Metrics Function ===
def compute_metrics(eval_pred):
    # Can be extended for accuracy, loss, perplexity, etc.
    logits, labels = eval_pred
    predictions = torch.argmax(torch.tensor(logits), dim=-1)
    return {}

# === Training Arguments ===
training_args = TrainingArguments(
    output_dir=output_dir,
    evaluation_strategy="epoch",
    learning_rate=2e-5,                      # 🔥 Good starting LR for BERTs
    per_device_train_batch_size=8,          # ⛽ Fits well on most GPUs
    per_device_eval_batch_size=8,
    num_train_epochs=3,                     # 🧠 Enough to fine-tune, not overfit
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    save_total_limit=2,
    push_to_hub=False,
    report_to="tensorboard",                       # Change to "tensorboard" if using it
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=True,
    mlm_probability=0.15,
)

# === Trainer ===
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    eval_dataset=dataset,                  # You can split train/test later
    compute_metrics=compute_metrics,
    data_collator=data_collator
)

# === Train ===
print("🚀 Training started...")
trainer.train()

# === Save final model and tokenizer ===
print("💾 Saving model...")
trainer.save_model(output_dir)
tokenizer.save_pretrained(output_dir)
print(f"✅ Finetuned model saved to: {output_dir}")
