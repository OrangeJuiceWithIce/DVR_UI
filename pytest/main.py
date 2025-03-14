from flask import Flask, request, jsonify
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)