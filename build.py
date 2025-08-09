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

# --- ADDED: Define a route for the services page ---
@app.route("/services")
def services():
    return render_template("services.html")

# --- ADDED: Define a route for the contact page ---
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    # The output directory for the static files
    output_dir = "dist" 
    os.makedirs(output_dir, exist_ok=True)

    with app.test_request_context():
        # --- UPDATED: Add the new pages to the build list ---
        # The list now includes all four pages
        # Format: (URL path, output filename)
        routes_to_build = [
            ("/", "index.html"),
            ("/about", "about.html"),
            ("/services", "services.html"),
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
    os.system("cp -r static dist/")
    
    print(f"✅ Site built successfully in the '{output_dir}/' directory!")
