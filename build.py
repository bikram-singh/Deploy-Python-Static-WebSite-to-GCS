from flask import Flask, render_template
import os

app = Flask(__name__)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Define a route for the about page
@app.route("/about")
def about():
    return render_template("about.html")

# Define a route for the contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    # The output directory for the static files
    output_dir = "dist" 
    os.makedirs(output_dir, exist_ok=True)

    with app.test_request_context():
        # --- UPDATED: The services page has been removed from the build list. ---
        # The list now includes the remaining three pages.
        # Format: (URL path, output filename)
        routes_to_build = [
            ("/", "index.html"),
            ("/about", "about.html"),
            ("/contact", "contact.html")
        ]

        # Loop through the list to generate each page
        for route in routes_to_build:
            path, filename = route
            # Simulate a request to the page
            html = app.test_client().get(path).data.decode("utf-8")
            # Write the generated HTML to a file
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(html)

    # Copy the static assets (CSS, images) to the output directory
    # Using shutil.copytree is a more cross-platform compatible way than 'cp'
    if os.path.exists("static"):
        if os.path.exists(os.path.join(output_dir, "static")):
            import shutil
            shutil.rmtree(os.path.join(output_dir, "static"))
        os.system("cp -r static dist/")
    
    print(f"✅ Site built successfully in the '{output_dir}/' directory!")
