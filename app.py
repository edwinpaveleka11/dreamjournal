import os
from dotenv import load_dotenv

from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from urllib.parse import urlparse

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

# Parse connection string
DATABASE_URL = os.getenv('DATABASE_URL')

# Fungsi untuk mendapatkan koneksi database
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Halaman utama - menampilkan semua mimpi
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute("SELECT * FROM dreams ORDER BY dream_date DESC")
    dreams = cur.fetchall()
    
    # Hitung statistik
    cur.execute("SELECT COUNT(*) as total FROM dreams")
    total_dreams = cur.fetchone()['total']
    
    cur.execute("SELECT dream_type, COUNT(*) as count FROM dreams GROUP BY dream_type")
    dream_stats = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template('index.html', dreams=dreams, total_dreams=total_dreams, dream_stats=dream_stats)

# Halaman tambah mimpi baru
@app.route('/add', methods=['GET', 'POST'])
def add_dream():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        dream_date = request.form['dream_date']
        mood = request.form['mood']
        dream_type = request.form['dream_type']
        tags = request.form['tags']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO dreams (title, description, dream_date, mood, dream_type, tags)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, description, dream_date, mood, dream_type, tags))
        conn.commit()
        cur.close()
        conn.close()
        
        flash('Dream berhasil ditambahkan!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add.html')

# Halaman detail mimpi
@app.route('/dream/<int:id>')
def view_dream(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM dreams WHERE id = %s", (id,))
    dream = cur.fetchone()
    cur.close()
    conn.close()
    
    if dream:
        return render_template('view.html', dream=dream)
    else:
        flash('Dream tidak ditemukan!', 'danger')
        return redirect(url_for('index'))

# Halaman edit mimpi
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_dream(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        dream_date = request.form['dream_date']
        mood = request.form['mood']
        dream_type = request.form['dream_type']
        tags = request.form['tags']
        
        cur.execute("""
            UPDATE dreams 
            SET title=%s, description=%s, dream_date=%s, mood=%s, dream_type=%s, tags=%s
            WHERE id=%s
        """, (title, description, dream_date, mood, dream_type, tags, id))
        conn.commit()
        cur.close()
        conn.close()
        
        flash('Dream berhasil diupdate!', 'success')
        return redirect(url_for('index'))
    
    cur.execute("SELECT * FROM dreams WHERE id = %s", (id,))
    dream = cur.fetchone()
    cur.close()
    conn.close()
    
    if dream:
        return render_template('edit.html', dream=dream)
    else:
        flash('Dream tidak ditemukan!', 'danger')
        return redirect(url_for('index'))

# Hapus mimpi
@app.route('/delete/<int:id>')
def delete_dream(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM dreams WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    
    flash('Dream berhasil dihapus!', 'success')
    return redirect(url_for('index'))

# Search mimpi
@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    search_query = f"%{query}%"
    cur.execute("""
        SELECT * FROM dreams 
        WHERE title ILIKE %s OR description ILIKE %s OR tags ILIKE %s
        ORDER BY dream_date DESC
    """, (search_query, search_query, search_query))
    dreams = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('search.html', dreams=dreams, query=query)

if __name__ == '__main__':
    app.run(debug=True)