import tkinter as tk
from tkinter import messagebox
import random

# --- CẤU HÌNH TRÒ CHƠI ---
# Định nghĩa các loại cây trồng có trong game
# growth_time: thời gian phát triển (tính bằng giây)
# harvest_value: số tiền nhận được khi thu hoạch
PLANTS = {
    "Cà rốt": {"seed_cost": 5, "growth_time": 10, "harvest_value": 15},
    "Bắp cải": {"seed_cost": 15, "growth_time": 20, "harvest_value": 40},
    "Dâu tây": {"seed_cost": 30, "growth_time": 45, "harvest_value": 80},
    "Đậu thần": {"seed_cost": 100, "growth_time": 100, "harvest_value": 820},
}

# Kích thước khu vườn (ví dụ: 3x3 = 9 ô đất)
GARDEN_ROWS = 6
GARDEN_COLS = 6

# --- LỚP CHÍNH CỦA ỨNG DỤNG ---
class GardenGame:
    def __init__(self, root):
        """Hàm khởi tạo giao diện và trạng thái game"""
        self.root = root
        self.root.title("Trò chơi Trồng Vườn")
        self.root.resizable(False, False) # Không cho phép thay đổi kích thước cửa sổ

        # Khởi tạo trạng thái ban đầu của game
        self.money = 100
        self.plots = []
        for _ in range(GARDEN_ROWS * GARDEN_COLS):
            # Mỗi ô đất là một dictionary lưu trạng thái
            self.plots.append({
                "state": "trống",  # các trạng thái: trống, đã gieo, trưởng thành
                "plant_type": None,
                "growth": 0
            })

        # Biến lưu trữ loại hạt giống người chơi đang chọn
        self.selected_seed = tk.StringVar(value=list(PLANTS.keys())[0])

        # --- Tạo các thành phần giao diện ---
        # Khung chính
        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack()

        # Khung hiển thị thông tin (tiền)
        info_frame = tk.Frame(main_frame)
        info_frame.pack(pady=5)
        self.money_label = tk.Label(info_frame, text=f"Tiền: ${self.money}", font=("Arial", 14, "bold"))
        self.money_label.pack()

        # Khung khu vườn
        garden_frame = tk.Frame(main_frame, bd=2, relief=tk.RIDGE)
        garden_frame.pack(pady=10)
        
        self.plot_buttons = []
        for i in range(GARDEN_ROWS * GARDEN_COLS):
            # Tạo nút cho mỗi ô đất
            button = tk.Button(garden_frame, text="Đất trống", width=12, height=4,
                               command=lambda index=i: self.on_plot_click(index))
            button.grid(row=i // GARDEN_COLS, column=i % GARDEN_COLS, padx=5, pady=5)
            self.plot_buttons.append(button)

        # Khung điều khiển và cửa hàng
        control_frame = tk.Frame(main_frame)
        control_frame.pack(pady=5)
        
        tk.Label(control_frame, text="Chọn hạt giống:").pack(side=tk.LEFT, padx=5)
        
        # Menu chọn hạt giống
        seed_option_menu = tk.OptionMenu(control_frame, self.selected_seed, *PLANTS.keys())
        seed_option_menu.pack(side=tk.LEFT)

        # Nút mua hạt giống
        buy_button = tk.Button(control_frame, text="Gieo hạt", command=self.plant_seed)
        buy_button.pack(side=tk.LEFT, padx=10)

        # Bắt đầu vòng lặp cập nhật game
        self.update_game()

    def on_plot_click(self, index):
        """Xử lý sự kiện khi người chơi nhấp vào một ô đất"""
        plot = self.plots[index]

        if plot["state"] == "trống":
            # Nếu đất trống, gợi ý gieo hạt
            messagebox.showinfo("Thông báo", "Ô đất này đang trống. Hãy chọn hạt giống và nhấn 'Gieo hạt' để trồng cây.")
        elif plot["state"] == "đã gieo":
            # Nếu đã gieo, tưới nước để cây lớn
            self.water_plant(index)
        elif plot["state"] == "trưởng thành":
            # Nếu cây đã lớn, thu hoạch
            self.harvest(index)

    def plant_seed(self):
        """Gieo hạt giống đã chọn vào một ô đất trống ngẫu nhiên"""
        seed_name = self.selected_seed.get()
        cost = PLANTS[seed_name]["seed_cost"]

        if self.money < cost:
            messagebox.showerror("Lỗi", "Không đủ tiền để mua hạt giống này!")
            return

        # Tìm một ô đất trống
        empty_plots_indices = [i for i, plot in enumerate(self.plots) if plot["state"] == "trống"]
        if not empty_plots_indices:
            messagebox.showwarning("Thông báo", "Tất cả các ô đất đã được sử dụng!")
            return
        
        # Chọn một ô ngẫu nhiên để gieo
        plot_index = random.choice(empty_plots_indices)
        
        self.money -= cost
        self.plots[plot_index]["state"] = "đã gieo"
        self.plots[plot_index]["plant_type"] = seed_name
        self.plots[plot_index]["growth"] = 0
        
        self.update_display()
        messagebox.showinfo("Thành công", f"Đã gieo {seed_name}!")

    def water_plant(self, index):
        """Bắt đầu quá trình phát triển của cây sau khi tưới"""
        plot = self.plots[index]
        if plot["growth"] == 0:
            # Chỉ bắt đầu tăng trưởng nếu cây chưa được tưới
            plot["growth"] = 1 # Bắt đầu quá trình lớn lên
            plant_name = plot["plant_type"]
            messagebox.showinfo("Tưới cây", f"Bạn đã tưới nước cho {plant_name}. Cây sẽ bắt đầu lớn lên.")
            self.update_display()

    def harvest(self, index):
        """Thu hoạch cây đã trưởng thành để kiếm tiền"""
        plot = self.plots[index]
        plant_name = plot["plant_type"]
        value = PLANTS[plant_name]["harvest_value"]

        self.money += value
        
        # Reset ô đất về trạng thái ban đầu
        plot["state"] = "trống"
        plot["plant_type"] = None
        plot["growth"] = 0
        
        messagebox.showinfo("Thu hoạch", f"Bạn đã thu hoạch {plant_name} và nhận được ${value}!")
        self.update_display()
        
    def update_game(self):
        """Hàm cập nhật trạng thái của tất cả cây trồng sau mỗi giây"""
        for i, plot in enumerate(self.plots):
            if plot["state"] == "đã gieo" and plot["growth"] > 0:
                plant_info = PLANTS[plot["plant_type"]]
                if plot["growth"] < plant_info["growth_time"]:
                    plot["growth"] += 1 # Tăng trưởng
                else:
                    plot["state"] = "trưởng thành" # Cây đã lớn
        
        self.update_display()
        # Lên lịch để hàm này được gọi lại sau 1000ms (1 giây)
        self.root.after(1000, self.update_game)

    def update_display(self):
        """Cập nhật giao diện (văn bản, màu sắc) để phản ánh trạng thái game"""
        self.money_label.config(text=f"Tiền: ${self.money}")

        for i, button in enumerate(self.plot_buttons):
            plot = self.plots[i]
            state = plot["state"]
            
            if state == "trống":
                button.config(text="Đất trống", bg="#A0522D") # Màu nâu
            elif state == "đã gieo":
                plant_name = plot["plant_type"]
                plant_info = PLANTS[plant_name]
                progress = (plot["growth"] / plant_info["growth_time"]) * 100
                button.config(text=f"{plant_name}\n({int(progress)}%)", bg="#89CFF0") # Màu xanh da trời
            elif state == "trưởng thành":
                plant_name = plot["plant_type"]
                button.config(text=f"{plant_name}\nSẵn sàng\nThu hoạch", bg="#90EE90") # Màu xanh lá cây

# --- KHỞI CHẠY GAME ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GardenGame(root)
    root.mainloop()
