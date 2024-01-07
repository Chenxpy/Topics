import pymysql
from PIL import Image
import cv2
import io

# 資料庫連線
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "test",
    "password": "12345678",
    "db": "topics",
    "charset": "utf8",
}

image_path = 'images1\ElonMusk.jpg'
image = cv2.imread(image_path)
# 將img 轉成二進制
image_bytes = cv2.imencode('.jpg', image)[1].tobytes()

try:
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        cursor = conn.cursor()

        # cursor.execute(
        # "insert into image(id, img) values(1,load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\images1\\ElonMusk.jpg'));")

        # 将图像数据插入表中，使用参数化查询
        insert_query = "INSERT INTO image (id, img) VALUES (%s,%s)"
        cursor.execute(insert_query, (1, image_bytes))

        # 儲存變更
        conn.commit()

        # 關閉連線
        conn.close()

except Exception as ex:  # 處理例外
    print(ex)
