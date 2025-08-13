from flask import Flask, render_template,request
from qrcode import QRCode
import io
import base64
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        qr = QRCode()
        data = request.form['data']
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return render_template('qrcode.html', img_str = img_str)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)