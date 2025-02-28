from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuring the mail settings
app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_DEFAULT_SENDER'] = ''

mail = Mail(app)

@app.route("/send_email", methods=["POST"])
def send_email():
    if request.method == "POST":
        subject = "NSP PHP Bootcamp Alert"
        recipients = request.form["recipient"]
        
        # Split the recipients string and create a list of email addresses
        emails = [email.strip() for email in recipients.split(",")]  # Clean up email addresses
        
        # Loop through each email and send the email
        for email in emails:
            body = render_template("welcome_email_template.html", user=email)  # Pass individual email to template
            
            # Create the message
            msg = Message(subject, recipients=[email])  # Send to one recipient at a time
            msg.html = body  # Set the HTML body content
            
            try:
                # Send the email
                mail.send(msg)
            except Exception as e:
                return f"Error sending email to {email}: {str(e)}"
        
        return "HTML Email sent successfully to all recipients!"

    return render_template("index.html")

@app.route("/")
def index():
    return render_template('index.html')  # Default route when accessed directly

if __name__ == "__main__":
    app.run(debug=True)
