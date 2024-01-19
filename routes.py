from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app.models import Blockchain

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        height = int(request.form['height'])
        
        # Add blockchain to MongoDB
        Blockchain.add_blockchain(name, status, height)
        
        # Redirect to blockchains route
        return redirect(url_for('get_blockchains'))

    return render_template('index.html')

@app.route('/blockchains', methods=['GET'])
def get_blockchains():
    result = Blockchain.get_blockchains()
    return jsonify({'success': True, 'result': result})
