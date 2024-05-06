from flask import Flask, request, abort, render_template

#======python的函數庫==========
import  os
import time
#======python的函數庫==========

def index():
    return render_template("./index.html")

        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
