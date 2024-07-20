import os
from PIL import Image

# Hàm quay và lưu ảnh
def rotate_images(input_dir, output_dir):
    angles = [45, 90, 135, 180, 225, 270, 315]
    
    # Tạo các thư mục cho từng góc quay nếu chưa tồn tại
    for angle in angles:
        angle_dir = os.path.join(output_dir, f'rotate_{angle}')
        if not os.path.exists(angle_dir):
            os.makedirs(angle_dir)
    
    # Duyệt qua từng ảnh trong thư mục input
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            
            # Quay và lưu ảnh vào thư mục tương ứng
            for angle in angles:
                rotated_img = img.rotate(angle, expand=True)
                output_path = os.path.join(output_dir, f'rotate_{angle}', filename)
                rotated_img.save(output_path)

# Đường dẫn tới thư mục chứa ảnh gốc
input_directory = 'path/to/your/input/directory'

# Đường dẫn tới thư mục sẽ lưu ảnh đã quay
output_directory = 'path/to/your/output/directory'

# Gọi hàm để quay ảnh
rotate_images(input_directory, output_directory)
