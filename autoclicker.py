#!/usr/bin/env python3
"""
Autoclicker - Customizable Click Speed Tool
A Python-based autoclicker with GUI support
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key

class Autoclicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Autoclicker - Customizable Click Speed")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Set icon color
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.is_clicking = False
        self.click_thread = None
        self.total_clicks = 0
        self.start_time = None
        self.mouse = Controller()
        
        # Create UI
        self.create_ui()
        
        # Hotkey listener
        self.listener = Listener(on_press=self.on_key_press)
        self.listener.start()
    
    def create_ui(self):
        """Create the user interface"""
        # Title
        title = tk.Label(
            self.root,
            text="🖱️ Autoclicker",
            font=("Arial", 24, "bold"),
            bg='#f0f0f0',
            fg='#333'
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Customizable automatic clicking tool",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666'
        )
        subtitle.pack()
        
        # Status
        self.status_label = tk.Label(
            self.root,
            text="🔴 Idle",
            font=("Arial", 12, "bold"),
            bg='#ffebee',
            fg='#c62828',
            relief=tk.RIDGE,
            padx=20,
            pady=10
        )
        self.status_label.pack(fill=tk.X, padx=20, pady=15)
        
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Click Speed
        ttk.Label(main_frame, text="Click Speed (Clicks per Second)").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.speed_var = tk.IntVar(value=10)
        speed_frame = ttk.Frame(main_frame)
        speed_frame.grid(row=1, column=0, sticky=tk.EW, pady=5)
        ttk.Scale(speed_frame, from_=1, to=100, variable=self.speed_var, orient=tk.HORIZONTAL).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(speed_frame, text="CPS", width=5).pack(side=tk.LEFT, padx=5)
        self.speed_entry = ttk.Entry(speed_frame, textvariable=self.speed_var, width=5)
        self.speed_entry.pack(side=tk.LEFT)
        
        # Mouse Button
        ttk.Label(main_frame, text="Mouse Button").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.button_var = tk.StringVar(value="left")
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, sticky=tk.EW, pady=5)
        ttk.Combobox(button_frame, textvariable=self.button_var, values=["left", "right", "middle"], state="readonly").pack(fill=tk.X, expand=True)
        
        # Click Count
        ttk.Label(main_frame, text="Number of Clicks (0 = infinite)").grid(row=4, column=0, sticky=tk.W, pady=10)
        self.count_var = tk.IntVar(value=0)
        ttk.Entry(main_frame, textvariable=self.count_var).grid(row=5, column=0, sticky=tk.EW, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, sticky=tk.EW, pady=20)
        
        self.start_btn = ttk.Button(button_frame, text="Start (F6)", command=self.start_clicking)
        self.start_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.stop_btn = ttk.Button(button_frame, text="Stop (F6)", command=self.stop_clicking, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Stats
        stats_frame = ttk.LabelFrame(main_frame, text="Statistics")
        stats_frame.grid(row=7, column=0, sticky=tk.EW, pady=15)
        
        ttk.Label(stats_frame, text="Total Clicks:").pack(side=tk.LEFT, padx=10, pady=10)
        self.clicks_label = ttk.Label(stats_frame, text="0", font=("Arial", 12, "bold"))
        self.clicks_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        ttk.Label(stats_frame, text="Elapsed Time:").pack(side=tk.LEFT, padx=10, pady=10)
        self.time_label = ttk.Label(stats_frame, text="0s", font=("Arial", 12, "bold"))
        self.time_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Info
        info_text = tk.Text(main_frame, height=4, width=50, bg='#e3f2fd', fg='#1976d2', relief=tk.FLAT, font=("Arial", 9))
        info_text.grid(row=8, column=0, sticky=tk.EW, pady=10)
        info_text.insert(tk.END, "💡 Tips:\n• Press F6 to toggle on/off\n• Use responsibly\n• Works on any website or application")
        info_text.config(state=tk.DISABLED)
    
    def start_clicking(self):
        """Start the autoclicker"""
        if self.is_clicking:
            return
        
        self.is_clicking = True
        self.total_clicks = 0
        self.start_time = time.time()
        
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_label.config(text="🟢 Clicking...", bg='#c8e6c9', fg='#2e7d32')
        
        self.click_thread = threading.Thread(target=self.click_loop, daemon=True)
        self.click_thread.start()
        
        self.update_stats()
    
    def stop_clicking(self):
        """Stop the autoclicker"""
        self.is_clicking = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="🔴 Idle", bg='#ffebee', fg='#c62828')
    
    def click_loop(self):
        """Main clicking loop"""
        cps = self.speed_var.get()
        interval = 1.0 / cps
        button_name = self.button_var.get()
        max_clicks = self.count_var.get()
        
        # Map button names
        button_map = {
            'left': Button.left,
            'right': Button.right,
            'middle': Button.middle
        }
        button = button_map.get(button_name, Button.left)
        
        click_count = 0
        
        while self.is_clicking:
            if max_clicks > 0 and click_count >= max_clicks:
                self.is_clicking = False
                break
            
            self.mouse.click(button)
            self.total_clicks += 1
            click_count += 1
            time.sleep(interval)
    
    def update_stats(self):
        """Update statistics display"""
        self.clicks_label.config(text=str(self.total_clicks))
        
        if self.start_time:
            elapsed = int(time.time() - self.start_time)
            self.time_label.config(text=f"{elapsed}s")
        
        if self.is_clicking:
            self.root.after(100, self.update_stats)
    
    def on_key_press(self, key):
        """Handle keyboard events"""
        try:
            if key == Key.f6:
                if self.is_clicking:
                    self.stop_clicking()
                else:
                    self.start_clicking()
        except AttributeError:
            pass
    
    def __del__(self):
        """Clean up"""
        if hasattr(self, 'listener'):
            self.listener.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Autoclicker(root)
    root.mainloop()
