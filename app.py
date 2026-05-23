from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Prevent caching
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("phishing_vectorizer.pkl")


# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    email = ""

    if request.method == "POST":

        email = request.form["email"].strip()
        
        # Validate that email is not empty
        if not email:
            result = "⚠️ Please enter an email to analyze"
        else:
            cleaned_email = clean_text(email)
            
            # Check if cleaned email has meaningful content
            if not cleaned_email.strip():
                result = "⚠️ No meaningful content found. Please enter actual email text."
            else:
                # Vectorize the cleaned email
                email_vectorized = vectorizer.transform([cleaned_email])

                prediction = model.predict(email_vectorized)[0]

                if prediction == 1:
                    result = "🚨 Phishing Email"
                else:
                    result = "✅ Safe Email"

    return render_template("index.html", result=result, email=email)


if __name__ == "__main__":
    app.run(debug=True)