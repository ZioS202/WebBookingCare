# Website Booking Care
---

## Giới thiệu
- Đây là website cho phép bệnh nhân đặt lịch khám online 
- Công nghệ sử dụng : `HTML, CSS, JS, Python Django`
- Thông tin thành viên nhóm :
  
| Tên               | Mail                       |
| ----------------- | -------------------------- |
| Nguyễn Quốc Thịnh | **20521964@gm.uit.edu.vn** |
| Trần Trí Đức      | **20520454@gm.uit.edu.vn** |
| Nguyễn Ngọc Tài   | **20521858@gm.uit.edu.vn** |
| Lê Thành Đạt      | **20521169@gm.uit.edu.vn** |
| Huỳnh Thế Hào     | **20521291@gm.uit.edu.vn** |

--- 
## Setup local (trên OS linux)
- Thực hiện clone repo về máy :
`git clone https://github.com/ZioS202/WebBookingCare.git`
- Tạo và sử dụng môi trường ảo :
`sudo apt-get install python3-venv` (nếu cần)
`python3 -m venv .venv`
`source ./.venv/bin/active`
- Thực hiện cài đặt các module cần thiết :
`sudo apt-get install libmysqlclient-dev` (nếu cần)
`sudo apt-get install libpq-dev python3-dev` (nếu cần)
`pip3 install -r requirements.txt`
- Thực hiện setup database:
    - Tạo database và user quản lý database:
        `sudo mysql` để vào MySQL monitor 
        `create database booking_care;` để tạo database có tên booking_care
        `CREATE USER 'test'@'localhost' IDENTIFIED BY '123';` để tạo user `test` với password là `123`
        `GRANT ALL PRIVILEGES ON booking_care.* TO 'test'@'localhost'; ` để cấp toàn quyền trên database `booking_care` cho user `test`
    - Chỉnh sửa file setting.py tại thư mục booking_care:
        
        ```python
        DATABASES = {
            "default": 
            {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "booking_care",
                "USER": "test",
                "PASSWORD": "123",
                "HOST": "127.0.0.1",
                "PORT": "3306",
                "OPTIONS": {
                    "sql_mode": "STRICT_TRANS_TABLES",
                },
            }
        }
        ```
    - Thực hiện tạo các tables và dữ liệu cho project:
        `python3 manage.py migrate` để tạo các table cơ bản
        `sudo mysql` để vào MySQL monitor
        `use booking_care` để xác định thao tác trên database booking_care
        `source <path to file insert>/insert_data.sql` để thêm dữ liệu vào cho database.
    - Thêm host `127.0.0.1` vào phần `ALLOWED_HOSTS` trong file setting.py
- Thực hiện chạy chương trình 
    `python3 manage.py runserver`
    Sau đó truy cập url `http://127.0.0.1:8000/` 
---
## Deploy lên pythonanywhere

Vào trang web pythonanywhere tạo tài khoản và vào terminal của nó, sau đó thực hiện tương tự như các bước ở trên để đưa project lên hệ thống và đọc https://help.pythonanywhere.com/pages/DeployExistingDjangoProject hoặc xem video https://www.youtube.com/watch?v=wokG8tG6vhg&list=LL&index=3&ab_channel=PhamLuanPy để có thể thực hiện các config.

---
## Tổng quan các chức năng

| Chức năng| Mô tả | 
| -------- | ------| 
| Đăng ký  | Giúp cho bệnh nhân có thể tạo tài khoản để sử dụng hệ thống|
|Đăng nhập/ Đăng xuất|Giúp cho bệnh nhân có thể truy cập hoặc truy xuất khỏi hệ thống|
|Lấy lại mật khẩu|Sẽ thực hiện gửi mail về cho chúng ta để có thể thiết lập mật khẩu mới khi quên mật khẩu cũ|
|Search engine|Giúp tìm kiếm bác sĩ, phòng khám, chuyên khoa một cách dễ dàng|
|Profile|Giúp bệnh nhân có thể xem thông tin cá nhân, cập nhật thông tin đó, xem lịch sử khám bệnh, hoặc thay đổi avatar, password của bản thân|
|Đặt lịch khám bệnh|Thực hiện đặt lịch khám và thanh toán chi phí|
|Phân loại|Hiển thị các thông tin theo chuyên khoa, bác sĩ, hoặc cơ sở y tế|
|Sử dụng mardown|Lưu thông tin cơ sở y tế, chuyên khoa, bác sĩ bằng syntax markdown và lấy lên để sử dụng một cách dễ dàng|

---
## Tổng quan giao diện hệ thống

- Giao diện trang chủ :

    ![](https://i.imgur.com/UHMbcaK.jpg)
    
- Giao diện đăng ký:

    ![](https://i.imgur.com/xNKWl8R.png)

- Giao diện đăng nhập:

    ![](https://i.imgur.com/AA4zImp.png)

- Giao diện quên mật khẩu:
    
    ![](https://i.imgur.com/KY4nod1.png)

- Giao diện thay đổi password:

    ![](https://i.imgur.com/2eLHYV3.png)
    
- Giao diện Chuyên khoa và chi tiết một chuyên khoa:

    ![](https://i.imgur.com/LIh1HvC.png)
    
    ![](https://i.imgur.com/gmAUWQb.png)

- Giao diện Cơ sở y tế và chi tiết một cơ sở y tế:
    
    ![](https://i.imgur.com/XcVJ1oa.png)
    
    ![](https://i.imgur.com/OFieIli.png)
    
- Giao diện Bác sĩ và chi tiết một bác sĩ:

    ![](https://i.imgur.com/UCEWZgH.png)
    
    ![](https://i.imgur.com/HUfix5W.png)

- Giao diện hồ sơ cá nhân :

    ![](https://i.imgur.com/GsFeWtT.png)
    
- Giao diện đặt lịch khám:
    
    ![](https://i.imgur.com/nTodZUv.png)

- Giao diện thanh toán:

    ![](https://i.imgur.com/dkJJA8B.png)

