import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os
import ctypes
import webbrowser  # Add this import for opening URLs

class TodoWallpaper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Todo Wallpaper By Amoy Technology")
        self.root.geometry("480x600")
        
        # Default settings
        self.text_color = "#666666"
        self.bg_color = "#eeeeee"
        self.font_size = 16
        self.margin = 120
        
        # Try to load font that supports Chinese
        try:
            self.font_path = "msyh.ttc"  # Microsoft YaHei
            self.font = ImageFont.truetype(self.font_path, self.font_size)
        except:
            self.font = ImageFont.load_default()

        self.setup_ui()
        
    def setup_ui(self):
        # Text editor
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.text_widget = tk.Text(self.text_frame, font=("Microsoft YaHei", 12))
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        
        # Load existing todo.txt
        if os.path.exists("todo.txt"):
            with open("todo.txt", "r", encoding="utf-8") as f:
                self.text_widget.insert("1.0", f.read())
                
        # Buttons frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5, padx=10, fill=tk.X)
        
        # Color chooser buttons
        tk.Button(self.button_frame, text="Text Color", 
                 command=self.choose_text_color).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Background Color", 
                 command=self.choose_bg_color).pack(side=tk.LEFT, padx=5)
        # Add Amoy Technology button
        tk.Button(self.button_frame, text="AmoyTechnology", 
                 command=self.open_amoy_website).pack(side=tk.LEFT, padx=5)
        
        # Save and apply button
        tk.Button(self.button_frame, text="Save&Apply", 
                 command=self.save_and_apply).pack(side=tk.RIGHT, padx=5)


    def open_amoy_website(self):
        webbrowser.open("https://amoy-tech.com")

    def choose_text_color(self):
        color = colorchooser.askcolor(self.text_color)[1]
        if color:
            self.text_color = color

    def choose_bg_color(self):
        color = colorchooser.askcolor(self.bg_color)[1]
        if color:
            self.bg_color = color

    def save_and_apply(self):
        # Save text content
        text_content = self.text_widget.get("1.0", tk.END)
        with open("todo.txt", "w", encoding="utf-8") as f:
            f.write(text_content)
            
        # Create wallpaper
        self.create_wallpaper()
        
    def create_wallpaper(self):
        # Load background image
        try:
            bg_image = Image.open("background.png")
        except:
            # Create blank background if image not found
            bg_image = Image.new('RGB', (1920, 1080), 'white')
            
        # Create drawing object
        draw = ImageDraw.Draw(bg_image)
        
        # Calculate text position
        screen_width = bg_image.width
        
        # Create semi-transparent background for text
        text_lines = self.text_widget.get("1.0", tk.END).splitlines()
        max_line_width = max([self.font.getlength(line) for line in text_lines])
        text_height = len(text_lines) * (self.font_size + 4)
        
        # Draw rounded rectangle background
        x1 = screen_width - max_line_width - self.margin - 40
        y1 = self.margin
        x2 = screen_width - self.margin
        y2 = y1 + text_height + 40
        
        # Draw rounded rectangle with alpha
        overlay = Image.new('RGBA', bg_image.size, (0,0,0,0))
        draw_overlay = ImageDraw.Draw(overlay)
        draw_overlay.rounded_rectangle([x1, y1, x2, y2], radius=12, 
                                    fill=self.bg_color + "E6")
        bg_image = Image.alpha_composite(bg_image.convert('RGBA'), overlay)
        draw = ImageDraw.Draw(bg_image)
        
        # Draw text
        y = self.margin + 20
        for line in text_lines:
            draw.text((x1 + 20, y), 
                     line, font=self.font, fill=self.text_color)
            y += self.font_size + 4
            
        # Save and set as wallpaper
        bg_image.save("wallpaper.png")
        self.set_wallpaper("wallpaper.png")
        
    def set_wallpaper(self, image_path):
        abs_path = os.path.abspath(image_path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TodoWallpaper()
    app.run()
