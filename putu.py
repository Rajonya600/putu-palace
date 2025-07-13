from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hi, I’m Rajonya 👋</h1>
    <p>Welcome to my personal site. I'm sharing my NEET & PCOS journey to help others.</p>
    <p><a href='/neet'>My NEET Journey</a></p>
    <p><a href='/pcos'>My PCOS Story</a></p>
    <p><a href='/connect'>Connect with Me</a></p>
    """

@app.route("/neet")
def neet():
    return """
    <h1>My NEET Journey 📚</h1>
    <p>I started preparing with big dreams. Faced pressure, tears, failures — but I never gave up. I’ll share how I managed time, handled stress, and what I learned along the way.</p>
    <p><a href='/'>Back to Home</a></p>
    """

@app.route("/pcos")
def pcos():
    return """
    <h1>My PCOS Story 🌸</h1>
    <p>I was diagnosed with PCOS and it hit me hard. I’ll talk about symptoms, treatment, diet, and how I didn’t let it break me. You're not alone!</p>
    <p><a href='/'>Back to Home</a></p>
    """

@app.route("/connect")
def connect():
    return """
    <h1>Connect with Me 💌</h1>
    <p>If this story helped you, I’d love to hear from you.</p>
    <p>Email: your-email@example.com</p>
    <p><a href='/'>Back to Home</a></p>
    """

if __name__ == "__main__":
    import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
