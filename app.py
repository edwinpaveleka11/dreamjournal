from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dream_journal'

mysql = MySQL(app)

# Halaman utama - menampilkan semua mimpi
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dreams ORDER BY dream_date DESC")
    dreams = cur.fetchall()
    cur.close()
    
    # Hitung statistik
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM dreams")
    total_dreams = cur.fetchone()[0]
    
    cur.execute("SELECT dream_type, COUNT(*) as count FROM dreams GROUP BY dream_type")
    dream_stats = cur.fetchall()
    cur.close()
    
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
        
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO dreams (title, description, dream_date, mood, dream_type, tags)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, description, dream_date, mood, dream_type, tags))
        mysql.connection.commit()
        cur.close()
        
        flash('Dream berhasil ditambahkan!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add.html')

# Halaman detail mimpi
@app.route('/dream/<int:id>')
def view_dream(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dreams WHERE id = %s", (id,))
    dream = cur.fetchone()
    cur.close()
    
    if dream:
        return render_template('view.html', dream=dream)
    else:
        flash('Dream tidak ditemukan!', 'danger')
        return redirect(url_for('index'))

# Halaman edit mimpi
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_dream(id):
    cur = mysql.connection.cursor()
    
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
        mysql.connection.commit()
        cur.close()
        
        flash('Dream berhasil diupdate!', 'success')
        return redirect(url_for('index'))
    
    cur.execute("SELECT * FROM dreams WHERE id = %s", (id,))
    dream = cur.fetchone()
    cur.close()
    
    if dream:
        return render_template('edit.html', dream=dream)
    else:
        flash('Dream tidak ditemukan!', 'danger')
        return redirect(url_for('index'))

# Hapus mimpi
@app.route('/delete/<int:id>')
def delete_dream(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM dreams WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    
    flash('Dream berhasil dihapus!', 'success')
    return redirect(url_for('index'))

# Search mimpi
@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    cur = mysql.connection.cursor()
    search_query = f"%{query}%"
    cur.execute("""
        SELECT * FROM dreams 
        WHERE title LIKE %s OR description LIKE %s OR tags LIKE %s
        ORDER BY dream_date DESC
    """, (search_query, search_query, search_query))
    dreams = cur.fetchall()
    cur.close()
    
    return render_template('search.html', dreams=dreams, query=query)

if __name__ == '__main__':
    app.run(debug=True)