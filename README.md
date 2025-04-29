🧠 MaskMind: Financial Mask-Filler MLM
Fine-tuned exclusively on Apple's SEC 10-K annual reports.

🎯 Problem Statement
Companies today generate thousands of pages of financial documents — 10-Ks, reports, filings — but finding a specific fact is painfully slow.
What if you could simply ask a financial question… and have an AI answer instantly, trained only on your company's own data?

💡 Solution
MaskMind fine-tunes powerful language models on private financial documents, creating a personalized, secure, and scalable financial chatbot.
Companies can deploy this system internally to control their own financial AI, without relying on public services.

✅ Private, secure, local deployment
✅ Fast retraining when new documents arrive
✅ No data leaks — full ownership of the AI knowledge
✅ Specialized financial language understanding

🛠️ How It Was Built
Step............................Description
Data............................Downloaded real SEC 10-K filings (Apple Inc.)
Preprocessing...................Chunked and tokenized the financial text
Base Model......................Started from BERT fine-tuned on SQuAD (general QA knowledge)
Custom Fine-tuning..............Further trained only on Apple’s financials for private domain expertise
Mask-Filler Model...............Trained specifically to predict missing financial terms using masked language modeling
Deployment......................Built an interactive Gradio app for local/private testing

🚀 Live Demo Flow
Users enter a financial sentence containing [MASK] where they want the model to predict missing information.

Example Input:
"Apple’s net [MASK] increased by 10% compared to last year."

Model Output:
"Apple’s net income increased by 10% compared to last year."
(with a confidence score!)

This is NOT ChatGPT — it's a custom fine-tuned model that understands real financial reports.

📚 Suggested Example Prompts
Example Prompt......................What It Tests
"Apple reported an operating [MASK] margin of 30% for the fiscal year." Profit margin recognition

"Revenue from [MASK] products increased significantly compared to last year." Product category prediction

"Net [MASK] for Apple in 2023 was $99.8 billion." Earnings vs profit vs income

"The company’s cash [MASK] from operations was over $100 billion." Cash flow prediction

"Apple expects continued strong growth in [MASK] services." App Store, iCloud, Apple Music, etc.

📋 Expected Outputs
Mask...............................Likely Completions
Operating margin..................."gross", "operating", "profit"
Revenue from [MASK]................"iPhone", "Mac", "Wearables", "Services"
Net [MASK]........................."income", "profit", "earnings"
Cash [MASK]........................"flow", "flows"
Growth in [MASK]...................services "App Store", "iCloud", "Music"

📈 Understanding Confidence Scores
Each prediction comes with a confidence score, shown as a percentage.

A higher confidence (e.g., 80%-90%) means the model is very certain.

A lower confidence (e.g., 5%-15%) means the model is less sure, but the output might still make sense.

Confidence is based on the model’s internal probability of choosing that particular masked word among many possibilities.

🧠 CS Fundamentals Behind the Build
Topic..............................How It Was Used
Sorting Algorithms.................Organized token sequences for model input
Stacks / Queues....................Batching and managing text chunks
Graphs.............................Attention mechanisms in Transformers
Dynamic Programming................Sequence alignment in hidden layers
Discrete Math......................Set theory and mappings during tokenization

📈 Scaling Potential
MaskMind isn't just for Apple —
The same system can be applied to:

Healthcare records
Legal filings
Scientific publications
Any company-specific documents!
Simply upload a new dataset → fine-tune → deploy.

💼 Future Vision
"The future demands private, customized AI.
MaskMind empowers companies to own their AI future — safely, securely, and intelligently."

🛠 Tech Stack
Python 3.12
Huggingface Transformers
Gradio
SEC 10-K filings (Apple)
Custom fine-tuning scripts
Docker-ready for deployment

## 🔥 Download the Fine-Tuned Model

To run this app locally, you must request access to the fine-tuned model checkpoint.

Request access here: [Request Access to MaskMind Fine-Tuned Model (Google Drive)]
(https://drive.google.com/drive/folders/1h-R9n9TesthL4IPXbdxs1E18W06PoNE6?usp=sharing)

**Important:**

- After your access is approved, download `models.zip`.
- Extract `models.zip`.
- Place the extracted `finetuned_model/` folder inside your project's `models/` directory.
- Make sure the app can find `models/finetuned_model/` when running.

🚀 Then you're ready to launch `chatbot_gradio.py` and start using MaskMind!
