import itertools
from pyzipper import *
from tkinter import Tk, Label, Entry
'''@description
@library: pyzipper, itertools, tkinter
    * pyzipper: để sử dụng hàm extractall() để giải nén file zip
    * itertools: để tạo các chỉnh hợp lặp chập k(length) từ charset
    * tkinter: để tạo giao diện
'''

def brute(file, charset: str, init_size: int, max_size: int, extractpath):
    """@description
    Hàm brute() dùng để tìm kiếm password bằng cách thử tất cả các ký tự trong charset từ init_size đến max_size với init_size là độ dài password tối thiểu, max_size là độ dài password tối đa
    @param: 
        * file: file zip cần giải nén
        * charset: tập ký tự sẽ thử
        * init_size: độ dài password tối thiểu
        * max_size: độ dài password tối đa
        * extractpath: đường dẫn giải nén file zip
    @result:
        * Hiển thị kết quả trên giao diện
    """

    """Tạo cửa sổ mới để hiển thị kết quả"""
    window = Tk()
    window.title('Result')
    window.geometry('500x100')

    """Tạo label để hiển thị dòng 'Current:' để hiển thị password hiện tại đang được duyệt"""
    Label(window, text='Current:').place(relx=0, rely=0.15)

    """Tạo label để hiển thị dòng 'Password is:' để hiển thị kết quả là password tìm được"""
    Label(window, text='Password is:').place(relx=0, rely=0.5)

    """Tạo entry result để hiển thị kết quả"""
    result = Entry(window, justify='center', state='readonly', width=60)
    result.place(relx=0.15, rely=0.52)

    """Tạo label để hiển thị password hiện tại đang được thử"""
    pwd = Label(window, text="")
    pwd.place(x=50, rely=0.15)

    """Duyệt từng độ dài password từ init_size đến max_size"""
    check = 0
    for length in range(init_size, max_size + 1):

        """Tạo các chỉnh hợp lặp chập k(length) từ charset với hàm product() của itertools"""
        for passwords in itertools.product(charset, repeat=length):
            """Nối các ký tự trong passwords để tạo password"""
            password = ''.join(passwords)

            """Hiển thị password hiện tại đang được thử"""
            pwd.config(text=password)

            """Cập nhật giao diện để hiển thị password hiện tại đang được thử"""
            window.update()
            
            try:
                """Thử giải nén file zip với password hiện tại đang được thử bằng hàm extractall()"""
                file.extractall(extractpath, pwd=password.encode())
                
                """Nếu không có lỗi thì hiển thị password tìm được lên entry result và kết thúc vòng lặp"""
                result.config(state='normal')
                result.insert(0, password)
                result.config(state='readonly')
                check = 1
                break
            except:
                """Nếu có lỗi thì tiếp tục vòng lặp để tìm password khác"""
                continue
        if check == 1:
            break

    """Nếu không tìm thấy password thì xóa entry result"""
    if result.get() == "":
        result.destroy()
        """Hiển thị dòng 'No password found' trên giao diện"""
        Label(window, text='No password found', font='Arial 10 bold').place(relx=0, rely=0.5)

    """Duy trì cửa sổ hiển thị kết quả"""
    window.mainloop()
