from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import hashlib
import secrets
import json
from datetime import datetime
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Manual CORS handling
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

DATABASE = 'tissue_salts.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Sessions table for login persistence
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Assessments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            service_type TEXT NOT NULL,
            age_group TEXT NOT NULL,
            answers TEXT NOT NULL,
            results TEXT NOT NULL,
            order_number TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_session_token():
    return secrets.token_urlsafe(32)

# Initialize database on startup
init_db()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        password_hash = hash_password(password)
        cursor.execute('INSERT INTO users (email, password_hash) VALUES (?, ?)', 
                      (email, password_hash))
        user_id = cursor.lastrowid
        
        # Create session token
        token = create_session_token()
        cursor.execute('INSERT INTO sessions (user_id, token) VALUES (?, ?)', 
                      (user_id, token))
        
        conn.commit()
        
        return jsonify({
            'success': True,
            'token': token,
            'email': email,
            'user_id': user_id
        })
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already registered'}), 400
    finally:
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    
    password_hash = hash_password(password)
    cursor.execute('SELECT id, email FROM users WHERE email = ? AND password_hash = ?', 
                  (email, password_hash))
    user = cursor.fetchone()
    
    if not user:
        conn.close()
        return jsonify({'error': 'Invalid credentials'}), 401
    
    # Create new session token
    token = create_session_token()
    cursor.execute('INSERT INTO sessions (user_id, token) VALUES (?, ?)', 
                  (user['id'], token))
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'token': token,
        'email': user['email'],
        'user_id': user['id']
    })

@app.route('/api/verify-session', methods=['POST'])
def verify_session():
    data = request.json
    token = data.get('token')
    
    if not token:
        return jsonify({'error': 'Token required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT u.id, u.email 
        FROM sessions s 
        JOIN users u ON s.user_id = u.id 
        WHERE s.token = ?
    ''', (token,))
    user = cursor.fetchone()
    conn.close()
    
    if not user:
        return jsonify({'error': 'Invalid session'}), 401
    
    return jsonify({
        'success': True,
        'email': user['email'],
        'user_id': user['id']
    })

@app.route('/api/save-assessment', methods=['POST'])
def save_assessment():
    data = request.json
    token = data.get('token')
    
    if not token:
        return jsonify({'error': 'Authentication required'}), 401
    
    conn = get_db()
    cursor = conn.cursor()
    
    # Verify session
    cursor.execute('SELECT user_id FROM sessions WHERE token = ?', (token,))
    session = cursor.fetchone()
    
    if not session:
        conn.close()
        return jsonify({'error': 'Invalid session'}), 401
    
    user_id = session['user_id']
    
    # Save assessment
    cursor.execute('''
        INSERT INTO assessments 
        (user_id, service_type, age_group, answers, results, order_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        user_id,
        data.get('service_type'),
        data.get('age_group'),
        json.dumps(data.get('answers')),
        json.dumps(data.get('results')),
        data.get('order_number')
    ))
    
    assessment_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'assessment_id': assessment_id
    })

@app.route('/api/get-assessments', methods=['POST'])
def get_assessments():
    data = request.json
    token = data.get('token')
    
    if not token:
        return jsonify({'error': 'Authentication required'}), 401
    
    conn = get_db()
    cursor = conn.cursor()
    
    # Verify session and get assessments
    cursor.execute('''
        SELECT a.* 
        FROM assessments a
        JOIN sessions s ON a.user_id = s.user_id
        WHERE s.token = ?
        ORDER BY a.created_at DESC
    ''', (token,))
    
    assessments = []
    for row in cursor.fetchall():
        assessments.append({
            'id': row['id'],
            'service_type': row['service_type'],
            'age_group': row['age_group'],
            'answers': json.loads(row['answers']),
            'results': json.loads(row['results']),
            'order_number': row['order_number'],
            'created_at': row['created_at']
        })
    
    conn.close()
    
    return jsonify({
        'success': True,
        'assessments': assessments
    })

@app.route('/api/logout', methods=['POST'])
def logout():
    data = request.json
    token = data.get('token')
    
    if token:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM sessions WHERE token = ?', (token,))
        conn.commit()
        conn.close()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)


