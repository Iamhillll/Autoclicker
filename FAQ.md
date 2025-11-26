# ❓ Autoclicker - Frequently Asked Questions (FAQ)

## General Questions

### Q: What is an autoclicker?
**A:** An autoclicker is a tool that automatically clicks your mouse at a specified rate. You set the speed (clicks per second) and it will continuously click for you.

### Q: Is it legal to use an autoclicker?
**A:** Autoclickers themselves are legal, but how you use them matters. Using them to:
- Automate your own legitimate tasks: ✅ Legal
- Violate website Terms of Service: ❌ Illegal
- Cheat in online games: ❌ Illegal (and bannable)
- Violate platform policies: ❌ Illegal

Always check the terms of service before using.

### Q: Will it work on every website?
**A:** Mostly, but not always:
- **Web Version**: Limited by browser security (works on most sites, may fail on some with bot protection)
- **Python Version**: Works system-wide (better for resistant sites)
- **Some websites**: Actively block automation - you'll need to test

### Q: Can I get banned for using this?
**A:** Potentially, yes. Websites and games actively detect bots:
- Some ban accounts permanently
- Some block your IP address
- Some use legal action
- Always use responsibly and only where permitted

### Q: How fast can it click?
**A:**
- **Web Version**: Up to 100 CPS (clicks per second)
- **Python Version**: Up to 1000+ CPS
- Most tasks: 5-50 CPS is plenty

---

## Installation & Setup

### Q: Do I need to install anything for the web version?
**A:** No! Just open `index.html` in your browser. That's it!

### Q: What do I need for the Python version?
**A:** Just Python 3.6+ and one package:
```bash
pip install pynput
```

### Q: Which version should I choose?
**A:** 
- **Web Version**: Easy, no setup, works in browser
- **Python Version**: More powerful, system-wide, faster
- Start with web, upgrade to Python if needed

### Q: Do I need administrator access?
**A:**
- **Web Version**: No
- **Python Version**: Recommended for best results
- Some systems require it for system-wide clicking

### Q: How do I install on Windows?
**A:** For Python version:
1. Download Python from python.org
2. Run `setup.bat` file
3. Run `python autoclicker.py`

### Q: How do I install on Mac?
**A:** For Python version:
1. Python usually pre-installed
2. Run `setup.sh` or manually: `pip3 install pynput`
3. Run `python3 autoclicker.py`

### Q: How do I install on Linux?
**A:** For Python version:
1. Install Python3: `sudo apt install python3`
2. Run `setup.sh` or manually: `pip3 install pynput`
3. Run `python3 autoclicker.py`

---

## Usage Questions

### Q: How do I start the autoclicker?
**A:** 
- **Web Version**: Click the "Start" button
- **Python Version**: Click "Start" button or press F6
- **Bookmarklet**: Click the bookmark

### Q: How do I stop it?
**A:**
- **Web Version**: Click "Stop" button
- **Python Version**: Click "Stop" button or press F6
- **Bookmarklet**: Click the bookmark again

### Q: What's the difference between the modes?
**A:**
- **Repeat Click**: Standard clicking pattern
- **Hold & Click**: Continuous clicking (experimental)

### Q: Can I use it while doing other things?
**A:** 
- **Web Version**: No, must keep window focused
- **Python Version**: Yes, works in background

### Q: How do I know how many times it clicked?
**A:** Check the counter in the interface. It updates in real-time.

### Q: Can I set a specific number of clicks?
**A:** Yes! Set the "Number of Clicks" field to the desired amount. Set to 0 for infinite.

### Q: Can I change the click speed while running?
**A:** 
- **Web Version**: No, must stop first
- **Python Version**: No, must stop first

### Q: What mouse buttons can I use?
**A:** Left, Right, and Middle click options available.

---

## Performance & Speed

### Q: What's a good click speed to start with?
**A:** Start with 5-10 CPS and increase if needed. Most tasks don't need more than 20 CPS.

### Q: Why is it clicking slowly?
**A:**
1. Check your CPS setting (higher = faster)
2. Close unnecessary programs
3. Try Python version (faster than web)
4. Check system performance

### Q: Why is it clicking too fast?
**A:**
1. Lower the CPS value
2. Set a click limit so it stops
3. Be faster with your stop button
4. Use Pause/Break key if available

### Q: Does click speed affect accuracy?
**A:** Yes, higher speeds are less accurate. Test speeds before using on important tasks.

### Q: Which version is faster?
**A:** Python version is significantly faster and more reliable.

---

## Troubleshooting

### Q: It's not clicking anything. What's wrong?
**A:** Try these in order:
1. Click on your target first
2. Ensure the window is focused
3. Lower the click speed (try 1-2 CPS)
4. Use Python version instead
5. Check if the website blocks automation

### Q: I get an error when running Python version?
**A:**
1. Install pynput: `pip install pynput`
2. Use Python 3.6 or newer: `python --version`
3. Try running as administrator/sudo
4. Check internet connection (for pip)

### Q: The hotkey (F6) doesn't work?
**A:**
1. Use web version (no hotkey)
2. Close other programs that use F6
3. Run Python version as administrator
4. Some systems reserve F6
5. Try web version buttons instead

### Q: Browser keeps crashing?
**A:**
1. Lower the CPS value
2. Set a click limit
3. Close other browser tabs
4. Use Python version
5. Restart your browser

### Q: It works but clicks in the wrong place?
**A:**
1. Make sure window is focused
2. Position mouse where you want
3. Lower the click speed
4. Some websites interfere with clicking
5. Use Python version for better precision

### Q: Permission denied errors?
**A:** Run with administrator/sudo:
- Windows: Right-click → Run as Administrator
- Mac/Linux: `sudo python3 autoclicker.py`

---

## Website & Platform Specific

### Q: Will it work on Google?
**A:** Web version: Limited. Python version: Yes.

### Q: Can I use it on YouTube?
**A:** Technically yes, but YouTube may detect automation. Use responsibly.

### Q: What about Facebook?
**A:** Facebook actively blocks bots. May not work or account may be flagged.

### Q: Can I use it on games?
**A:** Technically possible, but:
- Most games detect and ban bots
- Terms of Service usually prohibit it
- You risk permanent ban
- Not recommended

### Q: What about Steam games?
**A:** Not recommended. Steam actively detects and bans bots. Use at your own risk.

### Q: Can I use it on Discord?
**A:** You shouldn't. Discord bans bot users. Use official bots instead.

---

## Advanced Questions

### Q: Can I customize the hotkey?
**A:** 
- **Web Version**: No customization (use buttons)
- **Python Version**: You can edit the code to change it

### Q: Can I create a macro/combo?
**A:** Not built-in, but:
- Use multiple instances
- Set different click limits
- Run sequentially

### Q: Can it move the mouse?
**A:** No, only clicks. It clicks where the mouse currently is.

### Q: Can I use multiple autoclickers at once?
**A:** Yes, but it can be unpredictable. Not recommended.

### Q: What about click patterns (not just repetitive)?
**A:** Current version supports repetitive clicks only. Patterns would need custom code.

### Q: Can I automate it with scripts?
**A:** Python version can be integrated into Python scripts. Web version cannot.

---

## Security & Privacy

### Q: Is my data safe?
**A:** Yes, everything runs locally. No data is sent anywhere.

### Q: Does it collect any information?
**A:** No. No analytics, no tracking, no data collection.

### Q: Is it open source?
**A:** Yes, all source code is available to review.

### Q: Can I use it offline?
**A:** 
- **Web Version**: Yes, completely offline
- **Python Version**: Yes, completely offline
- No internet connection required

### Q: Is it safe to download from the internet?
**A:** Yes, this is open source and safe. You can review the code yourself.

---

## Downloading & Distribution

### Q: Can I share this with others?
**A:** Yes! It's free to share. Just include the documentation.

### Q: Can I modify it?
**A:** Yes! It's open source. Feel free to fork and modify.

### Q: Can I use it commercially?
**A:** Check the license, but generally for personal use only.

### Q: How do I stay updated?
**A:** Check the GitHub repository for new versions.

---

## Errors & Fixes

### Error: "ModuleNotFoundError: No module named 'pynput'"
**Fix:** Run `pip install pynput`

### Error: "Python is not recognized"
**Fix:** 
1. Install Python from python.org
2. Add to PATH during installation
3. Restart terminal/command prompt

### Error: "Permission denied" (Mac/Linux)
**Fix:** Run with sudo: `sudo python3 autoclicker.py`

### Error: "No suitable driver found"
**Fix:** Different hardware, usually not a real issue. Try anyway.

---

## Tips & Tricks

### 💡 Pro Tips
1. Start with low speeds and increase slowly
2. Always set a click limit when testing
3. Test on non-critical tasks first
4. Use Python version for reliability
5. Keep the window/application focused
6. Close unnecessary programs first
7. Update to latest version
8. Read website ToS before using

### 🎯 Best Practices
1. Use responsibly and ethically
2. Respect website terms of service
3. Don't use for cheating
4. Test thoroughly first
5. Keep backups of important data
6. Monitor your account after using
7. Use only where permitted
8. Report issues if you find them

---

## Getting Help

### Where to find answers?
1. **This FAQ** - Check here first
2. **GETTING_STARTED.md** - Step-by-step guide
3. **README.md** - Full documentation
4. **Console errors** - F12 in browser
5. **GitHub Issues** - Report problems

### How to report a bug?
1. Describe what happened
2. Show error messages
3. Include your OS and Python version
4. State which version you're using
5. Provide steps to reproduce

### How to suggest a feature?
1. Explain what you want
2. Why you need it
3. How it should work
4. Submit as GitHub issue

---

## Quick Reference

| Task | Web Version | Python Version |
|------|-------------|-----------------|
| Installation | None | `pip install pynput` |
| Start | Click button | Click button or F6 |
| Speed | 1-100 CPS | 1-1000 CPS |
| Hotkey | No | F6 |
| Background | No | Yes |
| Gaming | Not recommended | Not recommended |
| Web forms | Yes | Yes |
| Accessibility | Yes | Yes |

---

**Can't find your answer?** Check the documentation files or submit an issue!

**Questions?** Feel free to ask in the comments or issues section.

**Remember: Use responsibly!** 🖱️
