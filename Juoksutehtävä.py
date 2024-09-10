import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
import random
import time

# Maailmanennätysajat
world_records = {
    1912: {"time": 10.6, "athlete": "Donald Lippincott"},
    1936: {"time": 10.2, "athlete": "Jesse Owens"},
    1968: {"time": 9.95, "athlete": "Jim Hines"},
    1988: {"time": 9.79, "athlete": "Ben Johnson"},
    2009: {"time": 9.58, "athlete": "Usain Bolt"},

}

# Leijonien juoksunopeudet
lions = {
    "Simba": {"speed": 8.0},  # m/s
    "Nala": {"speed": 7.5},
    "Mufasa": {"speed": 8.2},
    "Scar": {"speed": 7.8},
    "Sarabi": {"speed": 7.6},
    "Kovu": {"speed": 8.1},
    "Kiara": {"speed": 7.4},
    "Zira": {"speed": 7.7},
    "Vitani": {"speed": 7.9},
    "Nuka": {"speed": 7.3},
}

# Luodaan Tkinter-ikkuna
root = tk.Tk()
root.title("Ernestin ja Kernestin juoksu")
root.geometry("1200x800")
root.configure(bg="#f0f0f0")

# Luodaan kehys pelille ja graafille
frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RIDGE)
frame.pack(side=tk.LEFT, padx=20, pady=20)

# Luodaan Canvas-komponentti peliä varten
canvas = tk.Canvas(frame, width=700, height=400, bg="#e0ffe0")
canvas.pack(padx=10, pady=10)

# Lisätään lähtö- ja maaliviivat
canvas.create_line(50, 0, 50, 400, fill="black", width=2)
canvas.create_line(650, 0, 650, 400, fill="black", width=2)

# Lisätään Ernestin ja Kernestin juoksijat
ernesti = canvas.create_oval(40, 50, 60, 70, fill="#1f77b4")
kernesti = canvas.create_oval(40, 90, 60, 110, fill="#ff7f0e")

# Lisätään leijonat juoksijoiksi
lion_colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff", "#800000", "#008000", "#000080", "#808000"]
lion_runners = []
for i, (lion_name, lion_data) in enumerate(lions.items()):
    lion_runners.append(canvas.create_oval(40, 130 + i * 30, 60, 150 + i * 30, fill=lion_colors[i]))

# Lisätään maailmanennätysjuoksijat
record_runners = []
for i, (year, record) in enumerate(world_records.items()):
    record_runners.append(canvas.create_oval(40, 430 + i * 30, 60, 450 + i * 30, fill="#000000"))

def run_ernesti(training=False):
    duration = random.uniform(10, 15)
    start_time = time.time()
    distance = 50
    
    while distance < 650:
        distance += random.uniform(8, 12)
        canvas.coords(ernesti, distance - 10, 50, distance + 10, 70)
        root.update()
        if training:
            time.sleep(0.001)  # Nopeutetaan aikaa harjoittelussa
        else:
            time.sleep(0.1)  # Normaalinopeus
    
    return duration

def run_kernesti(training=False):
    duration = random.uniform(12, 18)
    start_time = time.time()
    distance = 50
    
    while distance < 650:
        distance += random.uniform(6, 10)
        canvas.coords(kernesti, distance - 10, 90, distance + 10, 110)
        root.update()
        if training:
            time.sleep(0.001)  # Nopeutetaan aikaa harjoittelussa
        else:
            time.sleep(0.1)  # Normaalinopeus
    
    return duration

def yhteislahto():
    ernesti_duration = random.uniform(10, 15)
    kernesti_duration = random.uniform(12, 18)
    
    ernesti_start_time = time.time()
    kernesti_start_time = ernesti_start_time
    
    ernesti_distance = kernesti_distance = 50
    
    while ernesti_distance < 650 or kernesti_distance < 650:
        if ernesti_distance < 650:
            ernesti_distance += random.uniform(8, 12)
            canvas.coords(ernesti, ernesti_distance - 10, 50, ernesti_distance + 10, 70)
        
        if kernesti_distance < 650:
            kernesti_distance += random.uniform(6, 10)
            canvas.coords(kernesti, kernesti_distance - 10, 90, kernesti_distance + 10, 110)
        
        root.update()
        time.sleep(0.1)  # Normaalinopeus
    
    result_label.config(text=f"Voittaja: {'Ernesti' if ernesti_duration < kernesti_duration else 'Kernesti'}\nErnesti: {ernesti_duration:.2f} s\nKernesti: {kernesti_duration:.2f} s")

def run_all():
    lion_durations = [100 / lion["speed"] for lion in lions.values()]
    record_durations = [record["time"] for record in world_records.values()]
    
    start_time = time.time()
    
    distances = [50] * (len(lion_runners) + len(record_runners) + 2)
    
    while any(distance < 650 for distance in distances):
        for i in range(len(lion_runners)):
            if distances[i] < 650:
                distances[i] += (600 / lion_durations[i]) / len(lion_runners)
                canvas.coords(lion_runners[i], distances[i] - 10, 130 + i * 30, distances[i] + 10, 150 + i * 30)
        
        for i in range(len(record_runners)):
            if distances[len(lion_runners) + i] < 650:
                distances[len(lion_runners) + i] += (600 / record_durations[i]) / len(record_runners)
                canvas.coords(record_runners[i], distances[len(lion_runners) + i] - 10, 430 + i * 30, distances[len(lion_runners) + i] + 10, 450 + i * 30)
        
        if distances[-2] < 650:
            distances[-2] += random.uniform(8, 12)
            canvas.coords(ernesti, distances[-2] - 10, 50, distances[-2] + 10, 70)
        
        if distances[-1] < 650:
            distances[-1] += random.uniform(6, 10)
            canvas.coords(kernesti, distances[-1] - 10, 90, distances[-1] + 10, 110)
        
        root.update()
        time.sleep(0.1)  # Normaalinopeus

def close_game():
    root.destroy()

# Lisätään painikkeet
button_style = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "#ffffff", "activebackground": "#45a049"}

run_button_ernesti = tk.Button(frame, text="Lähetä Ernesti juoksemaan", command=run_ernesti, **button_style)
run_button_ernesti.pack(pady=5)

run_button_kernesti = tk.Button(frame, text="Lähetä Kernesti juoksemaan", command=run_kernesti, **button_style)
run_button_kernesti.pack(pady=5)

yhteislahto_button = tk.Button(frame, text="Yhteislähtö", command=yhteislahto, **button_style)
yhteislahto_button.pack(pady=5)

run_all_button = tk.Button(frame, text="Juokse kaikki", command=run_all, **button_style)
run_all_button.pack(pady=5)

close_button = tk.Button(frame, text="Sulje peli", command=close_game, **button_style)
close_button.pack(pady=5)

# Lisätään tuloslabel
result_label = tk.Label(frame, text="", font=("Helvetica", 12), bg="#ffffff")
result_label.pack(pady=5)

# Harjoittelutoiminnot
ernesti_times = []
kernesti_times = []

def harjoittele(paivat):
    for _ in range(paivat):
        ernesti_time = run_ernesti()
        kernesti_time = run_kernesti()
        ernesti_times.append(ernesti_time)
        kernesti_times.append(kernesti_time)
        time.sleep(0.001)

def harjoittele_1_paiva():
    harjoittele(1)
    plot_progress()

def harjoittele_1_kuukausi():
    harjoittele(30)
    plot_progress()

def harjoittele_1_vuosi():
    harjoittele(365)
    plot_progress()

def plot_progress():
    plt.figure(figsize=(10, 5))
    plt.plot(ernesti_times, label="Ernesti")
    plt.plot(kernesti_times, label="Kernesti")
    plt.xlabel("Harjoituskerrat")
    plt.ylabel("Aika (s)")
    plt.title("Ernestin ja Kernestin juoksukehitys")
    plt.legend()
    plt.show()

# Lisätään painikkeet harjoittelulle
harjoittele_1_paiva_button = tk.Button(frame, text="Harjoittele 1 päivä", command=harjoittele_1_paiva, **button_style)
harjoittele_1_paiva_button.pack(pady=5)

harjoittele_1_kuukausi_button = tk.Button(frame, text="Harjoittele 1 kuukausi", command=harjoittele_1_kuukausi, **button_style)
harjoittele_1_kuukausi_button.pack(pady=5)

harjoittele_1_vuosi_button = tk.Button(frame, text="Harjoittele 1 vuosi", command=harjoittele_1_vuosi, **button_style)
harjoittele_1_vuosi_button.pack(pady=5)

# Luodaan kehys graafille ja taulukolle
graph_frame = tk.Frame(root)
graph_frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Graafi maailmanennätysajoista
fig, ax = plt.subplots()
years = list(world_records.keys())
times = [record["time"] for record in world_records.values()]

ax.plot(years, times, marker='o')
ax.set_xlabel('Vuosi')
ax.set_ylabel('Aika (s)')
ax.set_title('100 metrin maailmanennätysajan kehittyminen')
ax.invert_yaxis()  # Käännetään y-akseli, jotta pienemmät ajat ovat ylempänä

# Näytetään graafi Tkinterissä
canvas_graph = FigureCanvasTkAgg(fig, master=graph_frame)
canvas_graph.draw()
canvas_graph.get_tk_widget().pack()

# Taulukko maailmanennätysajoista
columns = ("year", "time", "athlete")
treeview = ttk.Treeview(graph_frame, columns=columns, show="headings")
treeview.heading("year", text="Vuosi")
treeview.heading("time", text="Aika (s)")
treeview.heading("athlete", text="Juoksija")

for year, record in world_records.items():
    treeview.insert("", "end", values=(year, record["time"], record["athlete"]))

treeview.pack()

# Käynnistetään Tkinter-silmukka
root.mainloop()
