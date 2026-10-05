import calendar
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle

# --- FUTURISTIC NEON THEME COLORS ---
# Background: Deep Space Black
Window.clearcolor = get_color_from_hex("#0B0C10") 
COLOR_CARD = "#1F2833"     # Dark Grey boxes
COLOR_NEON = "#66FCF1"     # Glowing Cyan (Futuristic)
COLOR_MUTED = "#45A29E"    # Muted Cyan for text
COLOR_WEEKEND = "#FF4C4C"  # Red for Sat/Sun

class ModernDayButton(Button):
    """Futuristic Round Edges wala Button Custom Class"""
    def __init__(self, is_today=False, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0) # Default background transparent
        self.is_today = is_today
        
        # Agar aaj ka din hai, toh text ka color dark, warna neon
        self.color = get_color_from_hex(COLOR_NEON) if not is_today else get_color_from_hex("#0B0C10")
        self.bold = True
        self.font_size = '20sp'
        
        # Button ka design (Canvas drawing)
        with self.canvas.before:
            if self.is_today:
                Color(rgba=get_color_from_hex(COLOR_NEON)) # Aaj ki tareekh par Neon Glow
            else:
                Color(rgba=get_color_from_hex(COLOR_CARD)) # Normal din par Dark Grey
            
            # Rounded Corners (Radius 15)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
        
        # Jab mobile screen resize ho toh buttons khud ko adjust karein
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MicrosoftCalendarApp(App):
    def build(self):
        # Current Date Setup
        self.current_date = datetime.date.today()
        self.year = self.current_date.year
        self.month = self.current_date.month

        # Main Layout (Poori screen ka structure)
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # 1. HEADER (Previous, Month-Year, Next)
        header = BoxLayout(size_hint=(1, 0.15), spacing=10)
        
        prev_btn = Button(text="<", font_size='30sp', bold=True, background_normal='', background_color=get_color_from_hex(COLOR_CARD), color=get_color_from_hex(COLOR_MUTED))
        prev_btn.bind(on_press=self.prev_month)
        
        self.month_year_label = Label(text="", font_size='26sp', bold=True, color=get_color_from_hex(COLOR_NEON))
        
        next_btn = Button(text=">", font_size='30sp', bold=True, background_normal='', background_color=get_color_from_hex(COLOR_CARD), color=get_color_from_hex(COLOR_MUTED))
        next_btn.bind(on_press=self.next_month)

        header.add_widget(prev_btn)
        header.add_widget(self.month_year_label)
        header.add_widget(next_btn)
        
        self.main_layout.add_widget(header)

        # 2. WEEKDAYS NAME (Mon, Tue, Wed...)
        days_layout = GridLayout(cols=7, size_hint=(1, 0.1))
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            text_color = COLOR_WEEKEND if i >= 5 else "#C5C6C7"
            days_layout.add_widget(Label(text=day, font_size='16sp', bold=True, color=get_color_from_hex(text_color)))
        
        self.main_layout.add_widget(days_layout)

        # 3. CALENDAR GRID (Tareekhein)
        self.grid_layout = GridLayout(cols=7, spacing=8, size_hint=(1, 0.75))
        self.main_layout.add_widget(self.grid_layout)

        # Calendar load karna
        self.update_calendar()
        
        return self.main_layout

    # --- LOGIC SECTIONS ---

    def update_calendar(self):
        # Pehle purana data clear karein
        self.grid_layout.clear_widgets()
        
        # Header update karein (e.g., "October 2024")
        month_name = calendar.month_name[self.month]
        self.month_year_label.text = f"{month_name} {self.year}"
        
        # Mahine ka data (0 means empty day)
        cal_data = calendar.monthcalendar(self.year, self.month)
        
        for week in cal_data:
            for day in week:
                if day == 0:
                    # Khali box
                    self.grid_layout.add_widget(Label(text=""))
                else:
                    # Check karein agar yeh aaj ka din hai
                    is_today = (self.year == self.current_date.year and 
                                self.month == self.current_date.month and 
                                day == self.current_date.day)
                    
                    # Custom button create karein
                    btn = ModernDayButton(text=str(day), is_today=is_today)
                    self.grid_layout.add_widget(btn)

    def prev_month(self, instance):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.update_calendar()

    def next_month(self, instance):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.update_calendar()

# App yahan se start hogi
if __name__ == "__main__":
    MicrosoftCalendarApp().run()
    
   