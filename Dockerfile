# Use official PyTorch + CUDA base image
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y git
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Force PyTorch-only mode
ENV USE_TF=0

# Default command
CMD ["python", "src/train.py"]
