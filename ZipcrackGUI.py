from tkinter import * 
from tkinter import filedialog 
from tkinter import ttk 
from tkinter.messagebox import showwarning
from PIL import ImageTk, Image 
from crackclass import Crack
'''@description
@library: tkinter, filedialog, ttk, showwarning, Image, Crack
    * tkinter: để tạo giao diện
    * filedialog: để mở file
    * ttk: để tạo Combobox (chọn method cracking)
    * showwarning: để hiện thông báo
    * Image: để chèn ảnh vào giao diện
    * class Crack từ file crackclass.py: để thuận tiện cho việc quản lý và sử dụng input đưa vào
@agurment
    * crack_instance: là một instance của class Crack để thực hiện cracking
'''

crack_instance = Crack()

def main():
    '''@description
    @variable
        * window: là một instance của class Tk để tạo giao diện
        * img_import: là ảnh Zipcracking.png được chèn vào giao diện
        * resize: là ảnh đã được resize để hiển thị đúng kích thước trên giao diện
        * img: là ảnh đã được chuyển sang dạng ImageTk để hiển thị lên giao diện
        * zip_entry: là entry để nhập đường dẫn file zip
        * opfilebutton: là button để mở file zip bằng hàm openFile()
        * method_entry: là Combobox để chọn method cracking
        * method: là list chứa các method cracking được hỗ trợ là Bruteforce và Dictionary
        * wordlist: là entry để nhập đường dẫn wordlist
        * wlbutton: là button để mở wordlist bằng hàm addWordlist()
        * charset: là entry để nhập charset cho Bruteforce cracking
        * init_length: là entry để nhập init length cho Bruteforce cracking
        * max_length: là entry để nhập max length cho Bruteforce cracking
        * extract_path_entry: là entry để nhập đường dẫn extract path
        * expathbutton: là button để chọn extract path bằng hàm extractPath()
        * start: là button để thực hiện cracking
    '''

    def openFile():
        '''@description
        * Hàm openFile() dùng để thêm đường dẫn của file zip với các biến:
            + filepath là đường dẫn file zip được chọn từ filedialog.askopenfilename(),
            với filetypes chỉ cho phép chọn file zip
            + Nếu filepath khác rỗng thì thêm file zip vào crack_instance và hiển thị lên giao diện
            + Nếu có lỗi trong quá trình thêm file zip thì hàm sẽ 
            bỏ qua và đường dẫn file sẽ không được thêm vào crack_instance
        '''
        filepath = filedialog.askopenfilename(initialdir=r"C:\Users", title="Open file", filetypes=(("Zip Files (*.zip)", "*.zip"), ("All Files (*.*)", '*.*')))

        if filepath != '':
            global crack_instance
            try:
                crack_instance.addzipfile(filepath)
                zip_entry.delete(0, 'end')
                zip_entry.insert(0, filepath)
            except:
                pass

    def addWordlist():
        '''@description
        * Hàm addWordlist() dùng để thêm wordlist vào crack_instance với filedialog.askopenfilename() 
        và chỉ cho filetype là file text
        '''
        wlpath = filedialog.askopenfilename(initialdir=r"C:\Users", title="Open file", filetypes=(("Text Files (*.txt)", "*.txt"), ("All Files (*.*)", '*.*')))

        '''Nếu wlpath khác rỗng thì thêm wordlist vào crack_instance'''
        if wlpath != '':
            global crack_instance
            try:
                '''Thêm wordlist vào crack_instance'''
                crack_instance.addwordlist(wlpath)

                '''Xóa đường dẫn đang được hiển thị trên giao diện của wordlist'''
                wordlist.delete(0, 'end')

                '''Chèn đường dẫn wordlist vào wordlist để hiển thị lên giao diện'''
                wordlist.insert(0, wlpath)
            except:
                '''Nếu có lỗi xảy ra thì pass, wordlist sẽ không được thêm vào crack_instance'''
                pass

    '''Hàm handle_method_selection(event) dùng để xử lý sự kiện khi chọn method cracking'''
    def handle_method_selection(event):
        '''@description
        * Hàm handle_method_selection(event) dùng để xử lý sự kiện khi chọn method cracking
            + Khi gọi hàm các biến wordlist, wlbutton, charset, start_length, end_length sẽ được disable để tránh việc nhập input vào method không được chọn
        '''
        wordlist.config(state='disabled')
        wlbutton.config(state='disabled')
        charset.config(state='disabled')
        init_length.config(state='disabled')
        max_length.config(state='disabled')

        '''selected_value là giá trị được chọn từ Combobox method_entry'''
        selected_value = method_entry.get()

        '''Nếu selected_value là Dictionary thì wordlist và wlbutton sẽ được enable để nhập input'''
        if selected_value == "Dictionary":
            wordlist.config(state='normal')
            wlbutton.config(state='active')
        
        '''Nếu selected_value là Bruteforce thì charset, start_length và end_length sẽ được enable để nhập input'''
        if selected_value == "Bruteforce": 
            charset.config(state='normal')
            init_length.config(state='normal')
            max_length.config(state='normal')

    def extractPath(): 
        '''@description
        * Hàm extractPath() dùng để chọn đường dẫn extract path với filedialog.askdirectory()
        '''
        path = filedialog.askdirectory(initialdir=r"C:\Users", title="Browse for folder")

        '''Nếu path khác rỗng thì thêm path vào crack_instance và hiển thị lên giao diện'''
        if path != '':
            global crack_instance
            try:
                '''Thêm path vào crack_instance'''
                crack_instance.addextractpath(path)
                extract_path_entry.delete(0, 'end')
                extract_path_entry.insert(0, path)
            except:
                '''Nếu có lỗi xảy ra thì pass, path sẽ không được thêm vào crack_instance'''
                pass

    def cracking():
        '''@description
        * Hàm cracking() được dùng để chạy các thuật toán được chọn từ method, các file sẽ được extract tại folder đang chứa tool
        '''
        '''method là giá trị được chọn từ Combobox method_entry'''
        method = method_entry.get()
        global crack_instance

        '''Nếu method là Dictionary thì thực hiện hàm Dictionary_attack() từ crack_instance'''
        if method == "Dictionary":
            crack_instance.Dictionary_attack()
        
        '''Nếu method là Bruteforce thì thực hiện hàm Bruteforce_attack() từ crack_instance'''
        if method == "Bruteforce":
            '''charset_value, start_length_value, end_length_value lấy giá trị từ charset, start_length, end_length'''
            charset_value = charset.get()
            init_length_value = init_length.get()
            max_length_value = max_length.get()

            '''Nếu charset_value, start_length_value, end_length_value rỗng thì hiện thông báo Warning'''
            if charset_value == '':
                showwarning('Warning', 'Please enter a charset')
                return
            if init_length_value == '':
                showwarning('Warning', 'Please enter an init length')
                return
            if max_length_value == '':
                showwarning('Warning', 'Please enter a max length')
                return
            
            '''Nếu charset_value, start_length_value, end_length_value không rỗng thì thực hiện hàm additemBruteforce() và Bruteforce_attack() từ crack_instance'''
            crack_instance.additemBruteforce(charset_value, init_length_value, max_length_value)
            crack_instance.Bruteforce_attack()


    window = Tk()

    '''Thiết lập title, kích thước và không cho resize giao diện'''
    window.title('Zip cracking')
    window.geometry('600x600')
    window.resizable(False, False)

    img_import = (Image.open("Zipcracking.png"))

    resize = img_import.resize((450, 300), Image.AFFINE)

    img = ImageTk.PhotoImage(resize)

    '''Hiển thị ảnh lên giao diện'''
    Label(window, image=img, width=500, height=200).place(relx=0.5, rely=0.2 ,anchor=CENTER)


    '''Tạo các label, entry, button để nhập input và chọn method cracking'''
    Label(window, text="File", font=("Arial 10 bold")).place(x=60, y= 240)
    zip_entry = Entry(window, width=60)
    zip_entry.place(x=90, y=243)
    opfilebutton = Button(text="Open", command=openFile)
    opfilebutton.place(x=460, y=240)

    '''Tạo Combobox method_entry để chọn method cracking'''
    Label(window, text="Method", font=("Arial 10 bold")).place(x=36, y=280)

    '''method là list chứa các method cracking được hỗ trợ là Bruteforce và Dictionary'''
    method = ["Bruteforce", "Dictionary"]
    method_entry = ttk.Combobox(window, values=method, width=30)
    method_entry.bind("<<ComboboxSelected>>", handle_method_selection)
    method_entry.place(x=90, y=283)

    '''Tạo label, entry, button để nhập wordlist và charset, start length, end length cho Bruteforce cracking'''
    Label(window, text="Wordlist", font=("Arial 10 bold")).place(x=28, y=320)
    wordlist = Entry(window, width=50, state='disabled')
    wordlist.place(x=90, y=323)
    wlbutton = Button(text="Open", state='disabled', command=addWordlist)
    wlbutton.place(x=400, y=320)

    '''Tạo label, entry để nhập charset, start length, end length cho Bruteforce cracking'''
    Label(window, text="Charset", font=("Arial 10 bold")).place(x=0, y=360)
    charset = Entry(window, width=89)

    '''Charset mặc định là các ký tự alphabet thường'''
    charset.insert(0, 'abcdefghijklmnopqrstuvwxyz')
    charset.config(state='disabled')
    charset.place(x=55, y=363)

    '''Tạo label, entry để nhập init length là độ dài password tối thiểu cho Bruteforce cracking'''
    Label(window, text="Init length", font=("Arial 10 bold")).place(x=10, y=400)
    init_length = Entry(window, width=20, state='disabled')
    init_length.place(x=85, y=403)

    '''Tạo label, entry để nhập max length là độ dài password tối đa cho Bruteforce cracking'''
    Label(window, text="Max length", font=("Arial 10 bold")).place(x=250, y=400)
    max_length = Entry(window, width=20, state='disabled')
    max_length.place(x=330, y =403)

    '''Tạo label, entry, button để nhập extract path'''
    Label(window, text="Extract path", font=("Arial 10 bold")).place(x=5, y= 440)
    extract_path_entry = Entry(window, width=60)
    extract_path_entry.place(x=90, y=443)
    expathbutton = Button(text="Browse", command=extractPath)
    expathbutton.place(x=460, y=440)

    '''Tạo button Run để thực hiện cracking'''
    start = Button(text="Run", width=10, height=1, font='Arial 10 bold', bg='gray', command=cracking)
    start.place(relx=0.4, y = 500)
   
    '''window.mainloop() để hiển thị giao diện và chờ người dùng tương tác'''
    window.mainloop()

if __name__=="__main__":
    main()