import pyttsx3
from PyPDF2 import PdfReader
from tkinter import filedialog

# Select PDF file
book = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])

# Initialize PDF reader
pdf_reader = PdfReader(book)
pages = len(pdf_reader.pages)

# Initialize TTS engine
player = pyttsx3.init()

# ---- Voice Configuration ----
voices = player.getProperty('voices')
player.setProperty('voice', voices[0].id)   # 0 for male, 1 for female (varies by system)
player.setProperty('rate', 100)             # Speech speed (default ~200)
player.setProperty('volume', 1.0)           # Volume (0.0 to 1.0)

# ---- Pitch Control ----
# ⚠️ pyttsx3 doesn’t have a direct 'pitch' property,
# but you can simulate pitch by changing the speech rate or using engine-specific SSML tags.

def set_pitch(pitch_value: int):
    """
    Adjusts pitch using SSML (works best with Windows SAPI5 voices).
    pitch_value: int (range -10 to +10)
    """
    player.say(f'<pitch middle="{pitch_value}">Pitch adjusted</pitch>', name='pitch_change')

# Example: Set pitch manually before reading
# Note: SSML pitch works only if your TTS voice supports it (Windows SAPI5 usually does)
pitch_value = 5  # Higher value → higher pitch, lower → deeper voice

# Loop through all pages
for num in range(pages):
    page = pdf_reader.pages[num]
    text = page.extract_text()
    if text:
        player.say(f'<pitch middle="{pitch_value}">{text}</pitch>', name=f'page_{num}')

player.runAndWait()










