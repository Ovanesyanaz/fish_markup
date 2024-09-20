from flask import request
from flask import Flask
from PIL import Image
from io import BytesIO
import base64
app = Flask(__name__, static_folder='../client/build', static_url_path='/')
i = 1
j = int(input())
@app.route("/")
def index():
    return app.send_static_file('index.html')

def get_byte(number):
    with Image.open(f'photo/{number}.jpg') as img:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode("ascii")
        return img_str

@app.route("/server/test",methods=["POST"])
def sayHello():
    data = request.get_json()
    with open('txt.txt', 'r+') as f:
        f.seek(0, 2)       
        f.write("\n")
        if isinstance(data["amount"],list) == 0:
            f.write(data["amount"] + " нашлось " + data["value"] + " рыб" )
    print(data)
    if isinstance(data["amount"],list):
        return {"img" : str(get_byte(j)), "amount" : f"{j}"}
    return {"img": str(get_byte(int(data['amount']) + 1)), "amount" : str(int(data['amount']) + 1)}
if __name__ == "__main__":
    app.run(debug=True)