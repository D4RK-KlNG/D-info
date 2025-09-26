clear

echo "📂 Setting up Termux storage..."
termux-setup-storage

echo "📦 Installing requirements..."
# Install python
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    pkg install -y python
fi

# Upgrade pip
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

# Install requirements
if [ -f requirements.txt ]; then
    python3 -m pip install -r requirements.txt --quiet
else
    echo "requirements.txt not found!"
fi

echo "Running..."
python3 start.py
