from app import app
import os 
if __name__ == 'main':
    port = int(os.getenv("port"), '5000')
    app.run(host = '0.0.0.0' , port = port )