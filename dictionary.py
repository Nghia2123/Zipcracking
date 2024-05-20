from pyzipper import *
from tkinter import *

"""@description
@library: pyzipper, tkinter
    * pyzipper: để sử dụng hàm extractall() để giải nén file zip
    * tkinter: để tạo giao diện
"""

def dictionary(passlist, file, extractpath):
    """@description
    Hàm dictionary() dùng để tìm kiếm password trong wordlist
    @param:
        * passlist: file wordlist chứa các password
        * file: file zip cần giải nén
        * extractpath: đường dẫn giải nén file zip
    @result:
        * Hiển thị kết quả trên giao diện
    """

    """Tạo cửa sổ mới để hiển thị kết quả"""
    windows = Tk()
    windows.title('Result')
    windows.geometry('500x100')

    """Tạo label để hiển thị dòng 'Current:' để hiển thị 
       password hiện tại đang được duyệt trong wordlist"""
    Label(windows, text='Current:').place(relx=0, rely=0.15)

    """Tạo label để hiển thị dòng 'Password is:' để hiển thị kết quả là password tìm được"""
    Label(windows, text='Password is:').place(relx=0, rely=0.5)

    """Tạo entry để hiển thị kết quả"""
    result = Entry(windows, justify='center', state='readonly', width=60)
    result.place(relx=0.15, rely= 0.52)
    
    """Tạo label để hiển thị password hiện tại đang được duyệt trong wordlist"""
    pwd = Label(windows, text="")
    pwd.place(x=50, rely=0.15)

    """Mở file wordlist và tìm kiếm password"""
    with open(passlist, 'rb') as fi:
        """Duyệt từng dòng trong wordlist và đưa vào list passwords"""
        passwords = [line.strip() for line in fi]

    for password in passwords:
        """Hiển thị password hiện tại đang được duyệt"""
        pwd.config(text=password)
        windows.update()
        try:
            """Thử giải nén file zip với password hiện tại đang được duyệt bằng hàm extractall()"""
            file.extractall(extractpath, pwd=password)
            
            """Nếu không có lỗi thì hiển thị password tìm được lên entry result và kết thúc vòng lặp"""
            result.config(state='normal')
            result.insert(0, password.decode())
            result.config(state='readonly')
            break
        except:
            """Nếu có lỗi thì tiếp tục vòng lặp để tìm password khác"""
            continue
    
    """Nếu không tìm thấy password thì xóa entry result và hiển thị thông báo 'No password found in list'"""
    if result.get() == "":
        result.destroy()        
        Label(windows, text='No password found in list').place(relx=0, rely=0.5)
    
    """Duy trì cửa sổ hiển thị kết quả"""
    windows.mainloop()