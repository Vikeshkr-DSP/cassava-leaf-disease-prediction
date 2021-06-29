from __future__ import division,print_function
import numpy as np
import sys
import os

from PIL import Image
sys.modules['Image'] = Image 

from flask import Flask,render_template,request
from werkzeug.utils import secure_filename


from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app=Flask(__name__)
model=load_model('cassava_leaf.h5')

def model_predict(img_path,model):
    img=image.load_img(img_path,target_size=(420,420),color_mode='rgb')
    x=image.img_to_array(img)
    x=preprocess_input(img)
    x=np.expand_dims(x, axis=0)
    
    preds=np.argmax(model.predict(x))
    if preds == 0:
        preds='Plant is infected by Cassava Bacterial Blight (CBB).'
    elif preds==1:
        preds='Plant is infected by Cassava Brown Streak Disease (CBSD).'
    elif preds==2:
        preds='Plant is infected by Cassava Green Mottle (CGM).'
    elif preds==3:
        preds='Plant is infectd by Cassava Mosaic Disease (CMD).'
    else:
        preds="Leaf's are healthy"
    return preds

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['file']
        
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(basepath,'uploads',secure_filename(f.filename))
        f.save(file_path)
        
        preds=model_predict(file_path,model)
        result=preds
        return result
    return None

if __name__=='__main__':
    app.run(debug=True)

