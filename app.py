from flask import Flask, render_template, url_for,jsonify
import plotly.express as px
import plotly.io as pio
import json

app = Flask(__name__, static_folder='static',  template_folder='templates') 

@app.route('/', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')

# Sample data for Plotly chart
user_data = {"username": "JohnDoe"}
def create_plot():
    # Sample data
    data = {
        "x": ["Jan", "Feb", "Mar", "Apr", "May"],
        "y": [10, 15, 7, 12, 18]
    }
    fig = px.line(x=data["x"], y=data["y"], labels={"x": "Month", "y": "Usage"})
    
    # Convert to JSON format
    return pio.to_json(fig) # Correct way to serialize Plotly figures


@app.route('/dashboard')
def dashboard():
    plot_json = create_plot()
    return render_template('dashboard.html', plot_json=plot_json, user=user_data)

@app.route('/rewards')
def rewards():
    return "Rewards page"

@app.route('/insurance')
def insurance():
    return "Insurance page"

@app.route('/profile')
def profile():
    return "Profile page"  # Ensure this template exists

if __name__ == '__main__':
    app.run(debug=True)
