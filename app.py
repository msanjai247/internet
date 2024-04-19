from flask import Flask, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000  # Convert to Mbps
    upload_speed = st.upload() / 1000000  # Convert to Mbps
    ping = st.results.ping
    return render_template('speedtest.html', download_speed=download_speed, upload_speed=upload_speed, ping=ping)

if __name__ == '__main__':
    app.run(debug=True)
