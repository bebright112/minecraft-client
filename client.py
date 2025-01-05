import os
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import webbrowser

CONFIG_FILE = "launcher_config.txt"


# 서버정보

SERVER_IP = "여기에 작성"  # 서버 IP 주소
PORT = "0"  # 포트 번호 (생략할 경우 0으로 작성)
DISCORD_LINK = "https://discord.gg/example"  # 디스코드 링크
TUTORIAL_LINK = "https://example.com/tutorial"  # 튜토리얼 링크 (사이트 추천)


#스크립트 구문 "" 사이의 글자만 수정

def load_launcher_path():
    """저장된 Minecraft 런처 경로를 불러옵니다."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return file.read().strip()
    return None
def save_launcher_path(path):
    """Minecraft 런처 경로를 저장합니다."""
    with open(CONFIG_FILE, "w") as file:
        file.write(path)
def select_launcher_path():
    """사용자가 Minecraft 런처 파일 경로를 선택하도록 합니다."""
    path = filedialog.askopenfilename(
        title="Minecraft 런처 파일 선택",
        filetypes=[("실행 파일", "*.exe"), ("모든 파일", "*.*")]
    )
    if path:
        save_launcher_path(path)
        messagebox.showinfo("경로 저장 완료", f"Minecraft 런처 경로가 저장되었습니다:\n{path}")
    else:
        messagebox.showwarning("경로 선택 취소", "런처 경로가 선택되지 않았습니다.")
def join_server():
    """서버 참가 기능"""
    launcher_path = load_launcher_path()
    if not launcher_path or not os.path.exists(launcher_path):
        messagebox.showerror("오류", "Minecraft 런처 경로가 설정되지 않았거나 잘못되었습니다.\n먼저 런처 경로를 설정하세요.")
        return
    if PORT == 0:
        command = f'"{launcher_path}" --server {SERVER_IP}'
    else:
        command = f'"{launcher_path}" --server {SERVER_IP}:{PORT}'
    try:
        subprocess.Popen(command, shell=True)
        messagebox.showinfo("서버 참가", f"서버 {SERVER_IP}:{PORT if PORT != 0 else 25565}에 접속 중...")
    except Exception as e:
        messagebox.showerror("오류", f"서버 접속 중 오류 발생: {e}")
def open_tutorial():
    """튜토리얼 열기"""
    webbrowser.open(TUTORIAL_LINK)
def open_discord():
    """디스코드 열기"""
    webbrowser.open(DISCORD_LINK)
root = tk.Tk()
root.title("Minecraft Custom Client")
root.geometry("500x400")
root.configure(bg="#1E1E1E")
title_label = tk.Label(root, text="커스텀 기초 클라이언트", font=("Arial", 20, "bold"), bg="#1E1E1E", fg="white")
title_label.pack(pady=20)
button_style = {
    "font": ("Arial", 14),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45A049",
    "width": 20,
    "height": 2,
}
select_button = tk.Button(root, text="런처 경로 설정", command=select_launcher_path, **button_style)
select_button.pack(pady=10)
join_button = tk.Button(root, text="서버 참가", command=join_server, **button_style)
join_button.pack(pady=10)
tutorial_button = tk.Button(root, text="튜토리얼 보기", command=open_tutorial, **button_style)
tutorial_button.pack(pady=10)
discord_button = tk.Button(root, text="디스코드 열기", command=open_discord, **button_style)
discord_button.pack(pady=10)
footer_label = tk.Label(root, text="© 2025 Minecraft Custom Client", font=("Arial", 10), bg="#1E1E1E", fg="gray")
footer_label.pack(side="bottom", pady=10)
root.mainloop()
