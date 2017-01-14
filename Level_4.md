#Writeup Redtiger Level 4
- Level này, ta tìm hiểu về Blind SQL Injection 
- Blind SQL Injection là kiểu tấn công yêu cầu cơ sở dữ liệu câu hỏi đúng sai và xác định câu trả lời dựa trên đáp ứng của ứng dụng.
- Vì đề bài đã cho sẵn tên cột là `keyword` và tên bảng là `level4_users` nên ta sử dụng câu lệnh SQL sau:
`and ascii(substring((select concat(keyword) FROM level4_secret)x,1))=y-- -"%(a,b)` với x,y là số ta cần thay đổi.
- Hàm ascii() để chuyển đổi chữ hoặc số trong bảng mã ascii
- Hàm substring(chuỗi,vị trí,độ dài) với tham số vị trí, độ dài, hàm sẽ lại lại cho ta ký tự hoặc 1 cụm ký tự trong chuỗi sao cho phù hợp với điều kiện.
- x ở câu lệnh sql trên chính là vị trí kết quả câu lệnh select và y tham số dùng để so sánh với  kết quả của hàm ascii, nếu đúng thì web sẽ hiện thị `Query returned 1 rows.` còn nếu sai thì sẽ trả lại `Query returned 0 rows.`
- Trong kết quả trả lại là đúng thì ta sẽ đổi kết quả của y sang ký tự trong bảng mã ascii.

[Giải bằng python](https://github.com/TotoroC/Writeup_Redtiger-s_OverTheWire.org/blob/master/level4.py)