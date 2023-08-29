
import os
import tkinter as tk
from tkinter import filedialog
from subprocess import check_call
folder_path = None

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def folder_choose_button():
    global folder_path
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        directory_label.config(text=f"已选择文件夹: {selected_directory}")
        folder_path = selected_directory
    else:
        directory_label.config(text="未选择文件夹")
        folder_path = None

def run():
    global folder_path
    if folder_path is not None:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".mp4") and not file.endswith("_out.mp4"):
                    videofile = os.path.join(root, file)
                    videofile_out = videofile.replace('.mp4', '_out.mp4')
                    check_call("ffmpeg.exe -i {} -c:v libx264 -crf 23 -c:a aac -b:a 128k {}"\
                               .format(videofile, videofile_out), shell=True)

root = tk.Tk()
root.title("极简视频压缩工具")
folder_choose_button = tk.Button(root, text="选择文件夹", command=folder_choose_button)
folder_choose_button.pack(fill=tk.BOTH, expand=True)
directory_label = tk.Label(root, text="")
directory_label.pack()
run_button = tk.Button(root, text="压缩生成", command=run)
run_button.pack(fill=tk.BOTH, expand=True)

window_width = 480
window_height = 80
center_window(root, window_width, window_height)

root.mainloop()
