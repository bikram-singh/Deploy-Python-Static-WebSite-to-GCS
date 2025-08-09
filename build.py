from flask import Flask, render_template
import os
import shutil

app = Flask(__name__)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# The "/about" route has been deleted.

# Define a route for the contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    # The output directory for the static files
    output_dir = "dist" 
    os.makedirs(output_dir, exist_ok=True)

    with app.test_request_context():
        # --- UPDATED: The "about.html" page has been removed from the build list. ---
        routes_to_build = [
            ("/", "index.html"),
            ("/contact", "contact.html")
        ]

        # Loop through the list to generate each page
        for route in routes_to_build:
            path, filename = route
            html = app.test_client().get(path).data.decode("utf-8")
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(html)

    # Copy the static assets (CSS, images) to the output directory
    static_source = "static"
    static_dest = os.path.join(output_dir, "static")
    if os.path.exists(static_source):
        if os.path.exists(static_dest):
            shutil.rmtree(static_dest)
        shutil.copytree(static_source, static_dest)
    
    print(f"✅ Site built successfully in the '{output_dir}/' directory!")
