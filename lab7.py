import tkinter as tk
from tkinter import scrolledtext
from itertools import permutations


class StaffingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Подбор персонала IT-компании")
        self.root.geometry("600x500")


        self.candidates = ['A', 'B', 'C', 'D']


        self.create_widgets()

    def create_widgets(self):

        input_frame = tk.LabelFrame(self.root, text="Ввод опыта кандидатов", padx=10, pady=10)
        input_frame.pack(pady=10, fill="x", padx=10)


        self.experience_entries = {}
        for i, candidate in enumerate(self.candidates):
            tk.Label(input_frame, text=f"Кандидат {candidate}:").grid(row=i, column=0, sticky="e")
            entry = tk.Entry(input_frame)
            entry.grid(row=i, column=1, sticky="w")
            entry.insert(0, "1")
            self.experience_entries[candidate] = entry


        calc_button = tk.Button(self.root, text="Рассчитать варианты", command=self.calculate)
        calc_button.pack(pady=10)


        output_frame = tk.LabelFrame(self.root, text="Результаты", padx=10, pady=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)


        self.output_text = scrolledtext.ScrolledText(output_frame, width=70, height=15, wrap=tk.WORD)
        self.output_text.pack(fill="both", expand=True)

    def calculate(self):
        experience = {}
        for candidate in self.candidates:
            try:
                exp = int(self.experience_entries[candidate].get())
                experience[candidate] = exp
            except ValueError:
                self.output_text.insert(tk.END, f"Ошибка: для кандидата {candidate} введено нечисловое значение\n")
                return

        self.output_text.delete(1.0, tk.END)

        self.output_text.insert(tk.END, "=== Все возможные варианты ===\n")
        self.show_all_permutations()

        self.output_text.insert(tk.END, "\n=== Оптимальные варианты ===\n")
        self.find_optimal_solutions(experience)

    def show_all_permutations(self):
        """Вывод всех возможных перестановок"""
        all_perms = permutations(self.candidates, 4)
        for i, perm in enumerate(all_perms, 1):
            pj1, pj2, sr1, sr2 = perm
            self.output_text.insert(tk.END, f"{i}. PJ1={pj1}, PJ2={pj2}, SR1={sr1}, SR2={sr2}\n")

    def find_optimal_solutions(self, experience):
        """Поиск оптимальных решений с ограничениями"""
        max_avg_exp = -1
        best_distributions = []
        total_valid = 0

        for perm in permutations(self.candidates, 4):
            pj1, pj2, sr1, sr2 = perm

            if (pj1 == pj2) or (sr1 == sr2):
                continue

            if ('A' == sr1) or ('A' == sr2):
                continue

            total_valid += 1

            avg_exp = (experience[sr1] + experience[sr2]) / 2

            if avg_exp > max_avg_exp:
                max_avg_exp = avg_exp
                best_distributions = [(pj1, pj2, sr1, sr2)]
            elif avg_exp == max_avg_exp:
                best_distributions.append((pj1, pj2, sr1, sr2))

        self.output_text.insert(tk.END, f"\nНайдено {total_valid} валидных вариантов\n")
        self.output_text.insert(tk.END, f"Максимальный средний опыт SR: {max_avg_exp}\n")
        self.output_text.insert(tk.END, "Лучшие распределения:\n")

        for dist in best_distributions:
            self.output_text.insert(tk.END, f"PJ1={dist[0]}, PJ2={dist[1]}, SR1={dist[2]}, SR2={dist[3]}\n")



root = tk.Tk()
app = StaffingApp(root)
root.mainloop()