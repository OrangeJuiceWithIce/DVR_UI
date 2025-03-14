from flask import Flask, request, jsonify, send_file
import base64
import io
from PIL import Image
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# 模拟的图片数据
def generate_mock_image():
    # 生成一个随机的图片
    image = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
    image = Image.fromarray(image)
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

# 模拟的后端数据
@app.route('/get_exploration_results', methods=['POST'])
def get_exploration_results():
    data = request.json
    selected_number = data.get('selected_number', 4)  # 默认值为 4
    print("get_exploration_results")
    print(data)
    results = [
        {
            "id": i + 2,
            "image": "data:image/png;base64,"+generate_mock_image()
        }
        for i in range(selected_number)
    ]
    return jsonify(results)

@app.route('/get_text_style_guide_results', methods=['POST'])
def get_text_style_guide_results():
    data = request.json
    selected_number = data.get('selected_number', 4)  # 默认值为 4
    print("get_text_style_guide")
    print(data)
    results = [
        {
            "id": i + 2,
            "image": "data:image/png;base64,"+generate_mock_image()
        }
        for i in range(selected_number)
    ]
    return jsonify(results)

@app.route('/get_seperate_gaussians', methods=['POST'])
def get_seperate_gaussians():
    selected_number = 4
    data = request.json
    print("get_seperate_gaussians")
    print(data)
    results = [
        {
            "id": i + 1,
            "image": "data:image/png;base64,"+generate_mock_image()
        }
        for i in range(selected_number)
    ]
    return jsonify(results)

@app.route('/get_text_region_guide_results', methods=['POST'])
def get_text_region_guide_results():
    selected_number = 4
    data = request.json
    print("get_text_region_guide")
    print(data)
    results = [
        {
            "id": i + 2,
            "image": "data:image/png;base64,"+generate_mock_image()
        }
        for i in range(selected_number)
    ]
    return jsonify(results)

@app.route('/get_population_checkpoint', methods=['POST'])
def get_population_checkpoint():
    selected_number = 4
    data = request.json
    print("get_population_checkpoint")
    print(data)
    results = [
        {
            "id": i + 1,
            "image": "data:image/png;base64,"+generate_mock_image()
        }
        for i in range(selected_number)
    ]
    return jsonify(results)

@app.route('/filter_gaussians_by_region', methods=['POST'])
def filter_gaussians_by_region():
    data=request.json
    print("get_population_checkpoint")
    print(data)

    id_list = [1, 2, 3, 4]

    # 返回 JSON 响应
    return jsonify(id_list)
@app.route('/export_tf_video',methods=['POST'])
def export_tf_video():
    audio_path = 'C:/Users/liuha/Desktop/背景音/风居住的街道.mp3'  # 替换为你的音频文件路径

    # 使用 send_file 返回文件
    return send_file(
        audio_path,
        mimetype='audio/mpeg',  # 设置 MIME 类型为 MP3
        as_attachment=True,  # 设置为附件下载
        download_name='transfer_function_audio.mp3'  # 设置下载文件名
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)