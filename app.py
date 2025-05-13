from flask import Flask, render_template, request, redirect, url_for
from typing import List, Dict

app = Flask(__name__)

# Dummy database: list of dictionaries
entries: List[Dict[str, object]] = []

@app.route('/')
def home():
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    title = request.form.get('title')
    if title:
        entries.append({'title': title, 'completed': False})
    return redirect(url_for('home'))

@app.route('/toggle/<int:index>', methods=['POST'])
def toggle_complete(index: int):
    if 0 <= index < len(entries):
        entries[index]['completed'] = not entries[index]['completed']
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete_entry(index: int):
    if 0 <= index < len(entries):
        entries.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
