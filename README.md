# Hướng dẫn sử dụng
Đầu tiên tải các file từ github về (**Lưu ý**: nếu file **rockyou.txt** không đủ *133 MB* thì tải raw file về)

Sau khi tải các file về, bạn hãy click vào file **ZipcrackGUI.exe** để chạy ứng dụng
![image](https://hackmd.io/_uploads/BJ2tfD670.png)


(Bạn có thể xem source code từ các file: **ZipcrackGUI.py**, **crackclass.py**, **bruteforce.py** và **dictionary.py**)

Cửa sổ ứng dụng hiện lên
![image](https://hackmd.io/_uploads/SkuamD670.png)

Ý nghĩa các mục trên ứng dụng:
1. **File**: để chọn file zip cần crack
2. **Method**: dùng để chọn phương pháp crack gồm 2 kĩ thuật:
    + **Bruteforce**: tạo và sử dụng các password từ chuỗi charset để crack file zip.
    + **Dictionary**: sử dụng file list bao gồm các password phổ biến được tạo ra trước để crack file zip.
3. **Wordlist** (sử dụng cho **Dictionary**): dùng để chọn file list password. (Repository đã cung cấp file list password là `rockyou.txt`)
4. **Charset** (sử dụng cho **Bruteforce**): là chuỗi kí tự để tạo ra password bruteforce.
5. **Init length** và **Max length** (sử dụng cho **Bruteforce**): lần lượt là độ dài ban đầu của password được tạo ra và độ dài lớn nhất của password được tạo.
6. **Extract path**: là đường dẫn đến folder mà bạn muốn extract file ra.

## Demo
![image](https://hackmd.io/_uploads/ByHM2DTm0.png)

![image](https://hackmd.io/_uploads/r1Zo2wTm0.png)
