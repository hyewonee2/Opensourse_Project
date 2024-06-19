import tkinter as tk
import os

# 글로벌 변수로 checked_list 선언
checked_list = []

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("알고먹자")
        self.geometry("400x400+100+100")

        # 체크되면 TRUE를 가짐
        self.hindu_checked = tk.BooleanVar()
        self.muslim_checked = tk.BooleanVar()
        self.allergies_checked = tk.BooleanVar()

        # 이미지 로드
        image_hindu_path = "ImageFile/hindu.png"
        image_muslim_path = "ImageFile/muslim.png"

        self.image_hindu = tk.PhotoImage(file=image_hindu_path)
        self.image_muslim = tk.PhotoImage(file=image_muslim_path)

        # 체크박스 생성 및 이미지 삽입
        tk.Checkbutton(self, text="Hindu", image=self.image_hindu, variable=self.hindu_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Muslim", image=self.image_muslim, variable=self.muslim_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Allergies", variable=self.allergies_checked).pack(anchor=tk.W)

        # 확인 버튼 생성
        button = tk.Button(self, text="확인", command=self.show_checked)
        button.pack(pady=10)

    # 확인 버튼 클릭 시 체크박스 상태를 확인하고 함수를 호출하는 함수
    def show_checked(self):
        global checked_list
        # checked_list 초기화
        checked_list.clear()

        if self.hindu_checked.get():
            checked_list.append('hindu')

        if self.muslim_checked.get():
            checked_list.append('muslim')

        if self.allergies_checked.get():
            checked_list.append('allergies')

# 알러지 리스트 반환
def get_checked_list():
    return checked_list

#def allergy_check(): #복붙지점
#유진님이 만든 페이지자체를 allergy_check()라는 함수로 묶을 생각이었음

#def pyqt(): #복붙지점
# pyqt 페이지자체를 pyqt()라는 함수로 묶을 생각이었음

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    selected_list = get_checked_list()

    if selected_list == ['allergies']:
        allergy_check() # 연결지점
    elif selected_list == ['muslim'] or selected_list == ['hindu']:
        pyqt() # 연결지점
    else:
        print("선택된 항목이 없습니다.")
