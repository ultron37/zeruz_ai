#!/bin/bash

echo "===================================="
echo " Voice AI Assistant Installer"
echo "===================================="

# ----------------------------
# Update system
# ----------------------------
echo "[1/7] Updating system..."
sudo apt update && sudo apt upgrade -y

# ----------------------------
# System dependencies
# ----------------------------
echo "[2/7] Installing system packages..."
sudo apt install -y \
    espeak-ng \
    python3 \
    python3-pip \
    portaudio19-dev \
    unzip \
    curl \
    wget

# ----------------------------
# Python dependencies
# ----------------------------
echo "[3/7] Installing Python libraries..."
pip3 install --upgrade pip
pip3 install vosk sounddevice requests

# ----------------------------
# Download Vosk model
# ----------------------------
VOSK_DIR="vosk-model-small-en-us-0.15"

if [ ! -d "$VOSK_DIR" ]; then
    echo "[4/7] Downloading Vosk model..."
    wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    unzip vosk-model-small-en-us-0.15.zip
    rm vosk-model-small-en-us-0.15.zip
else
    echo "[4/7] Vosk model already exists, skipping."
fi

# ----------------------------
# Install Ollama
# ----------------------------
if ! command -v ollama &> /dev/null; then
    echo "[5/7] Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "[5/7] Ollama already installed."
fi

# ----------------------------
# Start Ollama service
# ----------------------------
echo "[6/7] Starting Ollama service..."
ollama serve & sleep 5

# ----------------------------
# Pull AI model
# ----------------------------
echo "[7/7] Downloading AI model (phi3)..."
ollama pull phi3

echo "===================================="
echo " INSTALLATION COMPLETE 🎉"
echo "===================================="
echo "Run your assistant with:"
echo "  python3 voice_ai.py"
