from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    output_dir = "dist"
    os.makedirs(output_dir, exist_ok=True)

    with app.test_request_context():
        for route in [("/", "index.html"), ("/about", "about.html")]:
            path, filename = route
            html = app.test_client().get(path).data.decode("utf-8")
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(html)

    os.system("cp -r static dist/")
    print(f"✅ Site built in {output_dir}/")
