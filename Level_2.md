#Writeup Redtiger Level1
<img src="http://i.imgur.com/miyIg23.png">
- Dựa vào gợi ý là dùng điều kiện, ta có để đoán Level này sử dụng kiểu tấn công vượt qua kiểm tra lúc đăng nhập.
- Giả sử ta có tài khoản admin/123456 thì khi đăng nhập, câu truy vấn sẽ là `SELECT * FROM users WHERE username="admin" and password="123456"`.
- Nếu ta sử dụng `'or '1'='1` làm giá trị của username và password, câu truy vấn sẽ là `SELECT * FROM users WHERE username = ' ' or '1'='1' and password=  ' ' or '1'='1'`. Nghĩa là nó sẽ chọn tất cả bởi vì có điều kiện '1'='1' là điều kiện luôn đúng.
- Kết quả thu được:
<img src="http://i.imgur.com/I93tso0.png">
