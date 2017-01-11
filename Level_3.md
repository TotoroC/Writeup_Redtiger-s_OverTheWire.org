#Writeup Redtiger Level 3
- Đầu tiên, ta xem phần gợi ý có đoạn "Try to get an Error". Vậy là phải tìm được một lỗi trong web này.
- Bấm vào TheCow, ta được chuyển đến page có đường dẫn như sau: `http://redtiger.labs.overthewire.org/level3.php?usr=MDYzMjIzMDA2MTU2MTQxMjU0`
- Ta thêm [] vào trước dấu bằng nghĩa là  `usr[]=MDYzMjIzMDA2MTU2MTQxMjU0`.  Giờ usr trở thành một mảng chứ không còn là một biến nữa.
- Ta nhận được lỗi như sau:
<img src="http://i.imgur.com/yVwIdVM.png">

- Ta truy cập vào file `urcrypt.inc` và xem source của nó, ta sẽ được một đoạn code mã hóa viết bằng php.
<img src="http://i.imgur.com/nSNajIf.png">
<img src="http://i.imgur.com/l68xGfb.png">

- Có nhiều cách để chạy file php, có thể chạy online hoặc chạy bằng xampp. Với xampp, ta đưa file .php vào thư mục `htdocs`, sau đó khởi động xampp là truy cập vào file php đó theo đúng đường dẫn. Ví dụ, trong thư mục `htdocs` mình tạo 1 folder tên là php để chứa file php, thì đường dẫn mở file đó là `localhost/php/file.php`
- Ta sử dụng đoạn code đó để encrypt các câu lệnh SQL. Mã hóa câu lệnh `' order by 7-- -` thì thấy bình thường nhưng khi `' order by 8-- -` thì nó bị lỗi. Nên ta dùng lệnh `'union select 1,2,3,4,5,6,7-- -'` và mã hóa nó rồi truyền vào tham số usr, ta thu được:
<img src="http://i.imgur.com/WFAVpq7.png">

- Sau đó, ta dùng gợi ý thứ 2 là tablename: `level3_users`. Mã hóa câu lệnh `' union select 1,password,3,4,5,6,7 from level3_users where username='Admin'`. Ta thêm điều kiện `username='Admin'` vì ta đang cần tìm mật khẩu của tài khoản đó.
<img src="http://i.imgur.com/W86bDFq.png">
<img src="http://i.imgur.com/94XekSw.png">

- Khi truyền tham số đã được mã hóa xong, ta thu được kết quả:
<img src="http://i.imgur.com/pjMlHQJ.png">

- Password chính là `thisisaverysecurepasswordEEE5rt`. !!!