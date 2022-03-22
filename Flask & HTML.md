     1. 將HTML檔案放在templates目錄下
      
     2. from flask import Flask, render_template

        app = Flask(__name__, static_url_path="/static2", static_folder="./test")  
        # static_folder可以指定圖檔放的位置，static_url_path將原本圖檔的位置改成這個名子，在程式碼內使用static2/圖檔名稱.圖檔副檔名

        @app.route("/")
        def home():
        return render_template('index.html')

        if __name__ == "__main__":
            app.run(debug=True, host="0.0.0.0", port=5001)
