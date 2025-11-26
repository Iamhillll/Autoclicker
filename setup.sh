#!/bin/bash
# Setup script for Autoclicker Python version

echo "🖱️ Autoclicker Setup"
echo "===================="
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "✓ Setup complete!"
echo ""
echo "To run the autoclicker:"
echo "  python3 autoclicker.py"
echo ""
echo "Or with administrator privileges (recommended):"
echo "  sudo python3 autoclicker.py"
echo ""
