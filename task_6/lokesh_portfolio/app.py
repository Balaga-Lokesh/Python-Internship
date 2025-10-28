from flask import Flask, render_template, request

app = Flask(__name__)

projects = [
    {
        "title": "SAVR Smart Value-Based Retail Delivery System",
        "tech": "React, Django, MySQL, REST API, Docker, Razorpay",
        "desc": [
            "Full-stack retail delivery platform optimizing order fulfillment and routing.",
            "Role-based authentication: Admin, Customer, Agent with OTP & JWT.",
            "Responsive dashboards and secure real-time order and delivery management."
        ]
    },
    {
        "title": "Facial Emotion and Cognitive State Detection System",
        "tech": "Python, TensorFlow, OpenCV, MediaPipe, Tkinter",
        "desc": [
            "Real-time FER system with 80% validation accuracy.",
            "Automated batch analysis and reporting.",
            "Robust GUI for video and image processing."
        ]
    },
    {
        "title": "SPELLL 2025 Conference Website",
        "tech": "HTML, CSS, JavaScript, Bootstrap",
        "desc": [
            "Developed responsive event website for national conference at IIIT Kottayam.",
            "Integrated custom UI, schedules, and speaker profiles."
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        content = request.form.get('content')
        message = f"Thank you for reaching out, {name}!"
    return render_template('contact.html', message=message)

@app.route('/project/<int:pid>')
def project(pid):
    if 0 <= pid < len(projects):
        proj = projects[pid]
        return render_template('project.html', project=proj)
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
