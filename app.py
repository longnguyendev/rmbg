from flask import Flask, request, render_template, send_file
import os
from rembg import remove

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    input_path = os.path.join('uploads', file.filename)
    output_path = os.path.join('uploads', 'no_bg_' + file.filename)

    # Lưu file tải lên
    file.save(input_path)

    # Xóa nền bằng rembg
    with open(input_path, 'rb') as inp, open(output_path, 'wb') as out:
        input_data = inp.read()
        output_data = remove(input_data)
        out.write(output_data)

    # Xóa file gốc sau khi xử lý
    os.remove(input_path)

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
