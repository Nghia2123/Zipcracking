from pyzipper import *
from dictionary import dictionary
from bruteforce import brute
from tkinter import messagebox

"""@description
@library: pyzipper, dictionary, bruteforce, tkinter
    * pyzipper: để sử dụng hàm AESZipFile để thao tác với file zip
    * dictionary(): từ file dictionary.py để sử dụng hàm dictionary()
    * brute(): từ file bruteforce.py để sử dụng hàm brute()
    * messagebox: từ tkinter để hiện thông báo
"""


class Crack:
    """
    Class Crack dùng để quản lý việc giải mã file zip
    @function: __init__, addzipfile, addwordlist, addextractpath, additemBruteforce, Dictionary_attack, Bruteforce_attack
        * __init__: dùng để khởi tạo các biến cần thiết cho việc giải mã file zip
        * addzipfile(filepath): dùng để thêm file zip vào crack_instance
        * addwordlist(wordlist): dùng để thêm wordlist vào crack_instance để sử dụng cho dictionary attack
        * addextractpath(path): dùng để thêm đường dẫn giải nén vào crack_instance
        * additemBruteforce(charset, start, end): dùng để thêm charset, start, end vào crack_instance để sử dụng cho dictionary attack
        * Dictionary_attack(): dùng để thực hiện dictionary attack
        * Bruteforce_attack(): dùng để thực hiện bruteforce attack
    """

    def __init__(self):
        """Khởi tạo các biến cần thiết cho việc giải mã file zip"""
        self.__zipfile = None # file zip
        self.__wlist = None # wordlist
    
    """addzipfile() dùng để thêm file zip vào crack_instance"""
    def addzipfile(self, filepath):
        """Kiểm tra xem đã có file zip nào được thêm vào trước đó chưa, nếu có thì đóng file zip đó lại, để mở file zip mới"""
        if type(self.__zipfile) == AESZipFile: 
            self.__zipfile.close()

        """Mở file zip với hàm AESZipFile() để theo tác"""
        self.__zipfile = AESZipFile(filepath, 'r')
    
    def addwordlist(self, wordlist):
        """addwordlist() dùng để thêm wordlist vào crack_instance để sử dụng cho dictionary attack"""
        self.__wlist = wordlist

    def addextractpath(self, path = ""):
        """addextractpath() dùng để thêm đường dẫn giải nén vào crack_instance"""
        self.__extractpath = path
    
    def additemBruteforce(self, charset, start, end):
        """additemDictionary() dùng để thêm charset, start, end vào crack_instance để sử dụng cho dictionary attack"""
        self.__charset = charset
        self.__start_length = int(start)
        self.__end_length = int(end)

    def Dictionary_attack(self):
        """Dictionary_attack() dùng để thực hiện dictionary attack"""

        """Kiểm tra xem đã chọn file zip chưa, nếu chưa thì hiện thông báo Warning"""
        if self.__zipfile == None:
            messagebox.showwarning('Warning', 'Please select a zip file')
            return
        
        """Kiểm tra xem đã chọn wordlist chưa, nếu chưa thì hiện thông báo Warning"""
        if self.__wlist == None:
            messagebox.showwarning('Warning', 'Please select a wordlist')
            return
        
        """Thực hiện dictionary attack bằng hàm dictionary()"""
        dictionary(self.__wlist, self.__zipfile, self.__extractpath)
    
    def Bruteforce_attack(self):
        """Bruteforce_attack() dùng để thực hiện bruteforce attack"""
        """Kiểm tra xem đã chọn file zip chưa, nếu chưa thì hiện thông báo Warning"""
        if self.__zipfile == None:
            messagebox.showwarning('Warning', 'Please select a zip file')
            return
        
        """Thực hiện bruteforce attack bằng hàm brute()"""
        brute(self.__zipfile, self.__charset, self.__start_length, self.__end_length, self.__extractpath)
        



