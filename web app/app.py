from flask import Flask, render_template, request, jsonify
import secrets
import string
import os
from datetime import datetime

app = Flask(__name__)

def generate_password(length):
    """Generate a secure password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """API endpoint to generate password"""
    try:
        data = request.json
        length = int(data.get('length', 12))
        
        # Validation
        if length < 8 or length > 20:
            return jsonify({'error': 'Length must be between 8 and 20'}), 400
        
        password = generate_password(length)
        return jsonify({'password': password, 'success': True})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save', methods=['POST'])
def save_password():
    """Save password to file"""
    try:
        data = request.json
        name = data.get('name', 'Password')
        password = data.get('password', '')
        
        if not password:
            return jsonify({'error': 'No password provided'}), 400
        
        # Create passwords directory if it doesn't exist
        if not os.path.exists('saved_passwords'):
            os.makedirs('saved_passwords')
        
        filename = 'saved_passwords/Password.txt'
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"[{timestamp}] {name}: {password}\n")
        
        return jsonify({'success': True, 'message': 'Password saved successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
