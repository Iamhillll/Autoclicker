# 🖱️ Autoclicker

A customizable, easy-to-use autoclicker with adjustable click speed. Perfect for repetitive clicking tasks across any website or application.

## Features

✨ **Customizable Click Speed** - Set anywhere from 1 to 1,000 clicks per second
🖱️ **Multiple Mouse Buttons** - Click with left, right, or middle mouse button
🔢 **Click Limits** - Set a specific number of clicks or run infinitely
⌨️ **Keyboard Hotkey** - Press F6 to toggle the autoclicker on/off
📊 **Real-time Statistics** - Track total clicks and elapsed time
🌐 **Works Anywhere** - Functions on any website or application
📥 **Easy Download** - Get it as a standalone HTML file or Python script
🎯 **User-Friendly UI** - Clean, intuitive interface

## Quick Start

### Option 1: Web Version (Recommended) ⭐

1. **Download** the `index.html` file
2. **Open** the file in any web browser
3. **Set your preferences**:
   - Adjust click speed (clicks per second)
   - Choose mouse button (left, right, middle)
   - Optionally set a click limit
4. **Click "Start"** or press **F6** to begin
5. **Click "Stop"** or press **F6** again to stop

**Advantages:**
- No installation required
- Works on Windows, Mac, Linux
- Works in any modern browser
- Bookmarklet version for on-the-fly use

### Option 2: Python Version (Advanced)

Requires Python 3.6+ and dependencies:

```bash
# Install required packages
pip install pynput

# Run the autoclicker
python autoclicker.py
```

**Advantages:**
- Works system-wide (not just browsers)
- More reliable clicking
- Lower latency
- Better compatibility with games and applications

### Option 3: Bookmarklet (Browser-based Quick Start)

1. Open `index.html` in your browser
2. Click "Copy Bookmarklet Code"
3. Create a new bookmark in your browser
4. Paste the code into the bookmark's URL field
5. Click the bookmark on any website to activate

## Usage Examples

### Example 1: Fast Clicking Game
- **Speed:** 20 CPS (clicks per second)
- **Button:** Left Click
- **Clicks:** 0 (infinite)
- **Use:** Gaming, form filling, rapid interactions

### Example 2: Precise Clicking
- **Speed:** 2 CPS
- **Button:** Left Click
- **Clicks:** 100
- **Use:** Measured interactions, specific task count

### Example 3: Right-Click Menu
- **Speed:** 1 CPS
- **Button:** Right Click
- **Clicks:** 50
- **Use:** Right-click triggered actions

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **F6** | Toggle autoclicker on/off |

## Files Included

- `index.html` - Web-based autoclicker (open in browser)
- `autoclicker.py` - Python desktop version
- `README.md` - Documentation

## System Requirements

### Web Version
- Any modern web browser (Chrome, Firefox, Safari, Edge)
- JavaScript enabled
- No installation required
- Windows, Mac, or Linux

### Python Version
- Python 3.6 or higher
- Windows, macOS, or Linux
- Required package: `pynput`
- Administrator/sudo access may be required for system-wide clicks

## Installation & Setup

### For Web Version
1. Download `index.html`
2. Open it in your web browser
3. That's it! Ready to use.

### For Python Version

```bash
# Install Python (if not already installed)
# Then install the required package
pip install pynput

# Run the autoclicker
python autoclicker.py
```

On some systems, you may need elevated permissions:
```bash
sudo python3 autoclicker.py
```

## Advanced Configuration

### Adjusting Click Speed

- **1-5 CPS**: Slow, precise clicking (accessibility, testing)
- **5-15 CPS**: Normal clicking speed (web browsing, forms)
- **15-50 CPS**: Fast clicking (gaming, rapid tasks)
- **50+ CPS**: Very fast clicking (extreme tasks, use with caution)

### Performance Tips

1. **Close unnecessary programs** - Improves overall responsiveness
2. **Lower click speed** - More reliable on slower systems
3. **Test first** - Always test with low speeds before increasing
4. **Use administrator mode** - Python version may need elevated permissions
5. **Check browser permissions** - Some browsers restrict JavaScript automation

## ⚠️ Important Disclaimers

**Please read carefully before using:**

1. **Website Terms of Service** - Using an autoclicker may violate website TOS. Use responsibly and only on websites you own or have permission to automate.
2. **Game Restrictions** - Many games and platforms actively detect and ban bots and automated tools. Use at your own risk.
3. **Not for Cheating** - This tool is intended for accessibility, automation of legitimate tasks, and testing purposes - NOT for competitive advantage in games.
4. **Legal Responsibility** - Users are fully responsible for ensuring their use complies with:
   - Local and national laws
   - Website terms of service
   - Platform policies
   - Copyright and intellectual property laws
5. **Detection Risk** - Automated clicking is often detectable; platforms may:
   - Ban your account
   - Block your IP address
   - Take legal action
   - Detect and stop the automation
6. **Ethical Use** - Use this tool ethically and responsibly

## Troubleshooting

### Web Version Not Working on a Website

**Problem:** Clicks don't register or tool doesn't work
- **Solution 1:** Some websites block automated interactions for security
- **Solution 2:** Check browser console (F12) for JavaScript errors
- **Solution 3:** Try the Python version instead for system-wide clicking
- **Solution 4:** Check if the website requires special permissions

### Python Version Won't Start

**Problem:** "ModuleNotFoundError: No module named 'pynput'"
- **Solution:** Install the required package:
  ```bash
  pip install pynput
  ```

**Problem:** Permission denied or no effect
- **Solution:** Run with administrator/sudo:
  ```bash
  sudo python3 autoclicker.py
  ```

### Clicks Not Registering

- **Ensure the application is focused** - Click on the target window first
- **Try lower click speeds** - Faster speeds may be skipped
- **Check mouse permissions** - Some systems require permissions
- **Test with Python version** - More reliable than browser version

### Hotkey (F6) Not Working

- **Try the web version** - Less hotkey issues (but web-based)
- **Check other programs** - F6 may be captured by other applications
- **Run as administrator** - Some systems require elevated permissions
- **Try different key** - Some systems reserve F6 for other uses

### Browser Crashes or Freezes

- **Reduce click speed** - Very high CPS can cause browser issues
- **Set a click limit** - Prevent infinite clicking that freezes the browser
- **Use Python version** - Better performance for high-speed clicking
- **Close other programs** - Free up system resources

## Performance & Limitations

### Web Version Limitations
- May not work on all websites (security restrictions)
- Limited to browser window
- May have higher latency
- Some websites actively block automation

### Python Version Advantages
- Works system-wide
- Lower latency
- Better reliability
- Requires elevated permissions on some systems

## Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation
- Test on different systems

## License

This project is provided as-is for educational and accessibility purposes. Use responsibly and in compliance with applicable laws and platform policies.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review console errors (F12 in browser)
3. Test with default settings first
4. Try the alternative version (web vs Python)
5. Create an issue on GitHub

## Version History

### v1.0.0
- ✅ Initial release
- ✅ Web-based version (HTML/JavaScript)
- ✅ Python desktop version
- ✅ Customizable click speed (1-1000 CPS)
- ✅ Multiple mouse button support (left, right, middle)
- ✅ Real-time click counter and timer
- ✅ Keyboard hotkey control (F6)
- ✅ Bookmarklet support
- ✅ One-click download feature
- ✅ Responsive UI design

---

**Remember:** Use this tool responsibly and ethically. Respect website terms of service, platform policies, and applicable laws. This tool is for legitimate automation and accessibility purposes only.

**Made with ❤️ for accessibility and automation**
