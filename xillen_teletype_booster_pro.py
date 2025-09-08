import os
import subprocess
import time
import socket
import pychrome
import threading
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

def find_chrome():
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        rf"C:\Users\{os.getenv('USERNAME')}\AppData\Local\Google\Chrome\Application\chrome.exe"
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

def is_port_open(port):
    s = socket.socket()
    try:
        s.settimeout(0.5)
        s.connect(('127.0.0.1', port))
        s.close()
        return True
    except:
        return False

def start_chrome():
    chrome = find_chrome()
    if not chrome:
        print('Chrome not found')
        exit(1)
    subprocess.Popen([
        chrome,
        '--remote-debugging-port=9222',
        '--user-data-dir=C:/chrome-profile-xillen',
        '--no-first-run',
        '--no-default-browser-check',
        '--disable-popup-blocking',
        '--disable-extensions',
        '--disable-background-networking',
        '--disable-sync',
        '--disable-translate',
        '--disable-background-timer-throttling',
        '--disable-renderer-backgrounding',
        '--disable-device-discovery-notifications',
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(60):
        if is_port_open(9222):
            return
        time.sleep(0.5)
    print('Chrome did not start')
    exit(1)

class XillenTeletypeBoosterPro:
    def __init__(self):
        self.is_running = False
        self.tabs = []
        self.cycles = 0
        self.stats = {'views_sent': 0}
    def print_banner(self):
        art_path = os.path.join(os.path.dirname(__file__), 'art.txt')
        try:
            with open(art_path, encoding='utf-8') as f:
                art_lines = [line.rstrip('\n') for line in f]
        except Exception:
            art_lines = ["(ascii art not found)"]
        info_lines = [
            " XILLEN TELEtype BOOSTER PRO",
            " Быстрая накрутка просмотров только в Chrome",
            " Автор: @BengaminButton",
            " GitHub: github.com/BengaminButton",
            " Telegram: t.me/Bengamin_Button",
            " t.me/XillenAdapter",
            " Запусти GUI для управления!",
        ]
        fill = '░▒▓█'
        info_width = max(len(line) for line in info_lines) + 2
        top = '┌' + '─' * info_width + '┐'
        bot = '└' + '─' * info_width + '┘'
        info_box = [top]
        for i in range(max(len(art_lines), len(info_lines))):
            art = art_lines[i] if i < len(art_lines) else ''
            if i < len(info_lines):
                info = info_lines[i]
                info_box.append('│' + info.ljust(info_width) + '│')
            else:
                pattern = ''.join([fill[(i+j)%len(fill)] for j in range(info_width)])
                info_box.append('│' + pattern + '│')
        info_box.append(bot)
        for idx in range(len(info_box)):
            art = art_lines[idx] if idx < len(art_lines) else ''
            print(f'{art:<40} {info_box[idx]}')
    def open_tabs(self, url, count):
        print(f"[INFO] Открываю {count} вкладок для {url}")
        browser = pychrome.Browser(url="http://127.0.0.1:9222")
        self.tabs = []
        for i in range(count):
            tab = browser.new_tab()
            tab.start()
            tab.Page.navigate(url=url, _timeout=10)
            self.tabs.append(tab)
            self.stats['views_sent'] += 1
            print(f"[INFO] Вкладка {i+1}/{count} открыта")
            time.sleep(0.01)
        print(f"[SUCCESS] Все {count} вкладок успешно открыты")
    def reload_tabs(self, delay):
        self.cycles = 0
        while self.is_running:
            self.cycles += 1
            print(f"[INFO] Цикл {self.cycles}: обновляю {len(self.tabs)} вкладок")
            for i, tab in enumerate(self.tabs):
                try:
                    tab.Page.reload()
                    print(f"[INFO] Вкладка {i+1} обновлена")
                except Exception as e:
                    print(f"[ERROR] Ошибка обновления вкладки {i+1}: {e}")
            print(f"[INFO] Ожидание {delay} секунд до следующего цикла")
            time.sleep(delay)
    def start(self, url, count, delay):
        self.is_running = True
        self.open_tabs(url, count)
        self.reload_tabs(delay)
    def stop(self):
        self.is_running = False
class XillenGUI:
    def __init__(self):
        self.booster = XillenTeletypeBoosterPro()
        self.root = tk.Tk()
        self.setup_gui()
    def setup_gui(self):
        self.root.title("Xillen Teletype Booster Pro")
        self.root.geometry("900x750")
        self.root.configure(bg='#0d1117')
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', background='#0d1117', foreground='#ffffff', font=('Minecraft Title Cyrillic', 18, 'bold'))
        style.configure('Subtitle.TLabel', background='#0d1117', foreground='#8b949e', font=('Minecraft Title Cyrillic', 12))
        style.configure('Warning.TLabel', background='#0d1117', foreground='#f85149', font=('Minecraft Title Cyrillic', 10))
        style.configure('Custom.TButton', background='#21262d', foreground='#ffffff', font=('Minecraft Title Cyrillic', 11, 'bold'))
        style.configure('Success.TButton', background='#238636', foreground='#ffffff', font=('Minecraft Title Cyrillic', 11, 'bold'))
        style.configure('Danger.TButton', background='#da3633', foreground='#ffffff', font=('Minecraft Title Cyrillic', 11, 'bold'))
        style.configure('Info.TButton', background='#0969da', foreground='#ffffff', font=('Minecraft Title Cyrillic', 11, 'bold'))
        style.configure('Custom.TEntry', background='#21262d', foreground='#ffffff', font=('Minecraft Title Cyrillic', 11))
        title_frame = tk.Frame(self.root, bg='#0d1117')
        title_frame.pack(fill='x', padx=20, pady=15)
        title_label = tk.Label(title_frame, text="XILLEN TELEtype BOOSTER PRO", font=('Minecraft Title Cyrillic', 18, 'bold'), fg='#ffffff', bg='#0d1117')
        title_label.pack()
        subtitle_label = tk.Label(title_frame, text="Быстрая накрутка через Chrome браузер", font=('Minecraft Title Cyrillic', 12), fg='#8b949e', bg='#0d1117')
        subtitle_label.pack()
        warning_label = tk.Label(title_frame, text="⚡ Открывает вкладки и обновляет только их!", font=('Minecraft Title Cyrillic', 10), fg='#f85149', bg='#0d1117')
        warning_label.pack()
        main_frame = tk.Frame(self.root, bg='#0d1117')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        url_frame = tk.Frame(main_frame, bg='#0d1117')
        url_frame.pack(fill='x', pady=10)
        tk.Label(url_frame, text="Ссылка на Teletype:", bg='#0d1117', fg='#ffffff', font=('Minecraft Title Cyrillic', 12, 'bold')).pack(anchor='w')
        self.url_entry = tk.Entry(url_frame, width=70, bg='#21262d', fg='#ffffff', insertbackground='#ffffff', font=('Minecraft Title Cyrillic', 11), relief='flat', bd=5)
        self.url_entry.pack(fill='x', pady=5)
        self.url_entry.insert(0, "https://teletype.in/@bengamin_button/XillenKillersPrice")
        params_frame = tk.Frame(main_frame, bg='#0d1117')
        params_frame.pack(fill='x', pady=10)
        params_grid = tk.Frame(params_frame, bg='#0d1117')
        params_grid.pack(fill='x')
        views_frame = tk.Frame(params_grid, bg='#0d1117')
        views_frame.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
        tk.Label(views_frame, text="Количество вкладок:", bg='#0d1117', fg='#ffffff', font=('Minecraft Title Cyrillic', 11)).pack(anchor='w')
        self.views_var = tk.StringVar(value="20")
        views_entry = tk.Entry(views_frame, textvariable=self.views_var, width=15, bg='#21262d', fg='#ffffff', font=('Minecraft Title Cyrillic', 11), relief='flat', bd=3)
        views_entry.pack(anchor='w', pady=2)
        delay_frame = tk.Frame(params_grid, bg='#0d1117')
        delay_frame.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        tk.Label(delay_frame, text="Задержка (сек):", bg='#0d1117', fg='#ffffff', font=('Minecraft Title Cyrillic', 11)).pack(anchor='w')
        self.delay_var = tk.StringVar(value="2")
        delay_entry = tk.Entry(delay_frame, textvariable=self.delay_var, width=15, bg='#21262d', fg='#ffffff', font=('Minecraft Title Cyrillic', 11), relief='flat', bd=3)
        delay_entry.pack(anchor='w', pady=2)
        params_grid.columnconfigure(0, weight=1)
        params_grid.columnconfigure(1, weight=1)
        buttons_frame = tk.Frame(main_frame, bg='#0d1117')
        buttons_frame.pack(fill='x', pady=15)
        buttons_row1 = tk.Frame(buttons_frame, bg='#0d1117')
        buttons_row1.pack(fill='x', pady=5)
        self.chrome_btn = tk.Button(buttons_row1, text="ОТКРЫТЬ И ОБНОВЛЯТЬ", command=self.start_chrome_boost, bg='#238636', fg='#ffffff', font=('Minecraft Title Cyrillic', 12, 'bold'), relief='flat', bd=8, height=2)
        self.chrome_btn.pack(side='left', padx=5, fill='x', expand=True)
        self.stop_btn = tk.Button(buttons_row1, text="ОСТАНОВИТЬ", command=self.stop_boost, bg='#da3633', fg='#ffffff', font=('Minecraft Title Cyrillic', 12, 'bold'), relief='flat', bd=8, height=2, state='disabled')
        self.stop_btn.pack(side='left', padx=5, fill='x', expand=True)
        stats_frame = tk.Frame(main_frame, bg='#0d1117')
        stats_frame.pack(fill='x', pady=10)
        self.stats_label = tk.Label(stats_frame, text="Статистика: Вкладок: 0 | Циклов: 0", bg='#0d1117', fg='#238636', font=('Minecraft Title Cyrillic', 11, 'bold'))
        self.stats_label.pack()
        log_frame = tk.Frame(main_frame, bg='#0d1117')
        log_frame.pack(fill='both', expand=True, pady=10)
        tk.Label(log_frame, text="Лог выполнения:", bg='#0d1117', fg='#ffffff', font=('Minecraft Title Cyrillic', 11, 'bold')).pack(anchor='w')
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, bg='#21262d', fg='#ffffff', insertbackground='#ffffff', font=('Consolas', 9), relief='flat', bd=3)
        self.log_text.pack(fill='both', expand=True)
        author_frame = tk.Frame(self.root, bg='#0d1117')
        author_frame.pack(fill='x', padx=20, pady=10)
        author_label = tk.Label(author_frame, text="Автор: @BengaminButton | GitHub: https://github.com/BengaminButton", font=('Minecraft Title Cyrillic', 8), fg='#8b949e', bg='#0d1117')
        author_label.pack()
        telegram_label = tk.Label(author_frame, text="Telegram: t.me/Bengamin_Button | t.me/XillenAdapter", font=('Minecraft Title Cyrillic', 8), fg='#8b949e', bg='#0d1117')
        telegram_label.pack()
    def update_stats(self):
        stats_text = f"Статистика: Вкладок: {self.booster.stats['views_sent']} | Циклов: {self.booster.cycles}"
        self.stats_label.config(text=stats_text)
    def start_chrome_boost(self):
        url = self.url_entry.get().strip()
        try:
            views = int(self.views_var.get())
            delay = float(self.delay_var.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Проверьте правильность введенных значений!")
            return
        
        print(f"[START] Запуск бустера для {url}")
        print(f"[PARAMS] Вкладок: {views}, Задержка: {delay}с")
        
        self.booster.is_running = True
        self.chrome_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        
        def boost_thread():
            if not is_port_open(9222):
                print("[INFO] Запускаю Chrome с отладкой...")
                start_chrome()
                print("[SUCCESS] Chrome запущен")
            else:
                print("[INFO] Chrome уже запущен")
            
            self.booster.open_tabs(url, views)
            while self.booster.is_running:
                self.booster.reload_tabs(delay)
                self.update_stats()
            print("[STOP] Бустер остановлен")
            self.chrome_btn.config(state='normal')
            self.stop_btn.config(state='disabled')
        threading.Thread(target=boost_thread, daemon=True).start()
    def stop_boost(self):
        self.booster.is_running = False
    def run(self):
        self.booster.print_banner()
        self.root.mainloop()
def main():
    app = XillenGUI()
    app.run()
if __name__ == "__main__":
    main()
