import tkinter as tk
import csv
import pandas as pd
from tkinter import scrolledtext
from tkcalendar import Calendar
from difflib import SequenceMatcher
import datetime

def window_interact(csv_file, konto, kata):

    def show_last_input():
        df = pd.read_csv(csv_file)
        sorted_df = df.sort_values(by=['Konto', 'Datum'])
        last_input = sorted_df.groupby('Konto').tail(1)
        top = tk.Toplevel(window)
        text_box = scrolledtext.ScrolledText(top, width=80, height=10)
        text_box.insert(tk.INSERT, last_input)
        text_box.configure(state='disabled')
        text_box.pack()

    def select_date():

        def save_date():
            date = cal.selection_get()
            date_str = date.strftime('%Y-%m-%d')
            date_label.config(text=date_str)
            top.destroy()
            return date_str

        current_date = datetime.datetime.now()
        year = current_date.year
        month = current_date.month
        day = current_date.day
        top = tk.Toplevel(window)
        cal = Calendar(top, selectmode='day', year=year, month=month, day=day)
        cal.pack()
        save_button = tk.Button(top, text="保存", command=save_date)
        save_button.pack()

    def save_data():
        date = date_label.cget('text')
        konto = konto_entry.get()
        art = art_entry.get()
        betrag = betrag_entry.get()
        kata = kata_entry.get()
        beschrei = beschrei_entry.get()
        with open(csv_file, 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, konto, art, betrag, kata, beschrei])
        betrag_entry.delete(0, 'end')
        beschrei_entry.delete(0, 'end')

    def find_similar_values(csv_file, column_name, search_text):
        similar_values = set()  
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cell_value = row[column_name]
                similarity = SequenceMatcher(None, cell_value, search_text).ratio()
                if similarity >= 0.5:  
                    similar_values.add(cell_value) 
        return list(similar_values)

    def on_entry_change(event):
        current_text = beschrei_entry.get()
        similar_values = find_similar_values(csv_file, 'Beschreibung', current_text)
        hint_var.set('')
        hint_listbox.delete(0, tk.END)
        if similar_values:
            hint_listbox.insert(tk.END, *similar_values)
            hint_listbox.select_set(0)
            hint_var.set(similar_values[0])
        else:
            hint_listbox.insert(tk.END, '无匹配!')
        window.update()

    def on_hint_select(event):
        selected_hint = hint_listbox.get(hint_listbox.curselection())
        beschrei_entry.delete(0, tk.END)
        beschrei_entry.insert(tk.END, selected_hint)
        hint_var.set('')


    window = tk.Tk()

    date_button = tk.Button(window, text='选择日期', command=select_date)
    date_button.grid(row=0, column=0)
    date_label = tk.Label(window, text='')
    date_label.grid(row=0, column=1)

    konto_label = tk.Label(window, text='银行账户:')
    konto_label.grid(row=1, column=0)
    konto_entry = tk.StringVar(window)
    konto_entry.set(konto[0])
    konto_menu = tk.OptionMenu(window, konto_entry, *konto)
    konto_menu.config(anchor='center')
    konto_menu.grid(row=1, column=1)

    art_label = tk.Label(window, text='收支:')
    art_label.grid(row=2, column=0)
    art = ['收入', '支出', '退款']
    art_entry = tk.StringVar(window)
    art_entry.set(art[1])
    art_menu = tk.OptionMenu(window, art_entry, *art)
    art_menu.config(anchor='center')
    art_menu.grid(row=2, column=1)

    betrag_label = tk.Label(window, text="金额:")
    betrag_label.grid(row = 3, column = 0)
    betrag_entry = tk.Entry(window, justify='center')
    betrag_entry.grid(row = 3, column = 1)

    kata_label = tk.Label(window, text='类别:')
    kata_label.grid(row=4, column=0)
    kata_entry = tk.StringVar(window)
    kata_entry.set('选择类别')
    kata_menu = tk.OptionMenu(window, kata_entry, *kata)
    kata_menu.config(anchor='center')
    kata_menu.grid(row=4, column=1)

    beschrei_label = tk.Label(window, text="备注:")
    beschrei_label.grid(row = 5, column = 0)
    beschrei_entry = tk.Entry(window, justify='center')
    beschrei_entry.grid(row = 5, column = 1)

    hint_var = tk.StringVar()

    hint_listbox = tk.Listbox(window)
    hint_listbox.grid(row=6, column=1, columnspan=2)
    hint_listbox.bind('<Button-1>', on_hint_select)

    save_button = tk.Button(window, text='保存', command=save_data)
    save_button.grid(row=7, column=0)

    info_button = tk.Button(window, text="提示", command=show_last_input)
    info_button.grid(row=7, column=1)

    beschrei_entry.bind('<KeyRelease>', on_entry_change)

    window.mainloop()
    

