# Getting Started Guide - Autoclicker

## 🚀 Quick Start (30 seconds)

### Method 1: Web Version (Easiest) ⭐

1. Download `index.html`
2. Open it in your web browser
3. Set click speed
4. Click "Start" button
5. Done! Your autoclicker is running

### Method 2: Python Version (Most Powerful)

```bash
# Step 1: Install dependencies
pip install pynput

# Step 2: Run the autoclicker
python autoclicker.py
```

---

## 📱 Step-by-Step: Web Version

### Windows, Mac, or Linux

1. **Download**: Right-click on `index.html` and save
2. **Open**: Double-click the file (opens in your default browser)
3. **Configure**:
   - Slide or type the number of clicks per second (1-100 recommended)
   - Choose which mouse button (usually "Left Click")
4. **Start**: Click the blue "Start" button
5. **Stop**: Click the red "Stop" button or press F6

### Advanced Settings

- **Repeat Click Mode**: Standard clicking pattern
- **Hold & Click Mode**: Click continuously while holding
- **Mouse Button**: Left, Right, or Middle click
- **Speed**: Adjust for your needs

---

## 🐍 Step-by-Step: Python Version

### Prerequisites
- Python 3.6+
- Administrator/sudo access (may be required)

### Installation

#### Windows
```batch
# Open Command Prompt as Administrator
# Run:
pip install pynput
python autoclicker.py
```

#### macOS/Linux
```bash
# Open Terminal
# Run:
pip3 install pynput
sudo python3 autoclicker.py
```

### Usage
1. Window appears - set your preferences
2. Click "Start" or press F6
3. Clicks will start automatically
4. Press F6 to stop

---

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| F6 | Toggle autoclicker on/off |

---

## 📊 Performance Tips

### For Best Results

1. **Start Slow**: Begin with 5-10 CPS, increase if needed
2. **Test First**: Always test on a non-critical task
3. **Use Click Limit**: Set a limit to prevent accidents
4. **Close Background Apps**: Improves reliability
5. **Use Administrator Mode**: Python version works better with elevated permissions

### Click Speed Reference

| Speed | Best For | CPS Range |
|-------|----------|-----------|
| Slow | Accessibility, testing | 1-5 |
| Normal | Web browsing, forms | 5-15 |
| Fast | Gaming, rapid clicks | 15-50 |
| Very Fast | Extreme tasks | 50+ |

---

## 🔧 Troubleshooting

### "The autoclicker won't click anything"
**Solution**: 
- Make sure you click on your target window first
- Try lowering the click speed
- Try the Python version instead (more reliable)

### "I'm getting an error opening the Python version"
**Solution**:
- Install pynput: `pip install pynput`
- Try running with administrator/sudo access
- Make sure Python 3.6+ is installed

### "F6 hotkey isn't working"
**Solution**:
- Use the web version (no hotkey issues)
- Some programs intercept F6 - close them
- Run Python version as administrator/sudo

### "Clicks register too slowly"
**Solution**:
- The Python version is faster
- Close unnecessary programs
- Lower the number of clicks per second first, then increase gradually
- Try increasing CPS value

---

## 💡 Use Cases

### ✅ Good Uses
- Accessibility automation
- Repetitive form filling
- Testing websites
- Automation of your own tasks
- Accessibility needs

### ❌ Avoid These
- Cheating in online games
- Bot detection will ban you
- Violating website terms of service
- Competing in multiplayer games
- Unauthorized account access

---

## 📥 Download Information

### What You Get

- `index.html` - Web version (just open in browser)
- `autoclicker.py` - Python version (run with python)
- `requirements.txt` - Python dependencies
- `setup.sh` - macOS/Linux setup script
- `setup.bat` - Windows setup script
- `README.md` - Full documentation

### How to Download

1. Go to the repository
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the folder
5. Open `index.html` or run `python autoclicker.py`

---

## 🎯 Common Scenarios

### Scenario 1: Click a Button 100 Times
1. Speed: 5 CPS
2. Clicks: 100
3. Button: Left Click
4. Action: Start, let it run

### Scenario 2: Spam Click as Fast as Possible
1. Speed: 50 CPS
2. Clicks: 0 (unlimited)
3. Button: Left Click
4. Action: Start, stop when done

### Scenario 3: Slow Right-Clicks for Menu Clicking
1. Speed: 2 CPS
2. Clicks: 50
3. Button: Right Click
4. Action: Position mouse, start

---

## 🆘 Getting Help

1. Check this guide first
2. Look at the README.md file
3. Review console errors (F12)
4. Try the other version (web vs Python)
5. Test with default settings

---

## 📝 Remember

- Use responsibly
- Respect website terms of service
- Check before using on any platform
- Don't use for cheating
- Report issues if you find them

**Happy clicking!** 🖱️
