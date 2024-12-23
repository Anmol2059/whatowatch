from flask import Flask, render_template, request, redirect, url_for, session, flash
from processing import preprocess
from processing.display import Main
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Global variables
displayed = []
movies = None
new_df = None

# Authentication functions
def check_user_exists(username):
    if not os.path.exists('users.txt'):
        return False
    with open('users.txt', 'r') as f:
        for line in f:
            stored_username = line.strip().split(',')[0]
            if stored_username == username:
                return True
    return False

def validate_login(username, password):
    if not os.path.exists('users.txt'):
        return False
    with open('users.txt', 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                return True
    return False

def save_user(username, password):
    with open('users.txt', 'a') as f:
        f.write(f"{username},{password}\n")

# Authentication routes
@app.route('/')
def landing():
    if 'username' in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if validate_login(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_user_exists(username):
            return render_template('signup.html', error="Username already exists")
        
        save_user(username, password)
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Movie recommendation routes
@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    global new_df
    if request.method == 'POST':
        selected_movie_name = request.form.get('movie_name')
        session['selected_movie_name'] = selected_movie_name
        recommendations = {
            'tags': preprocess.recommend(new_df, selected_movie_name, 'Files/similarity_tags_tags.pkl'),
            'genres': preprocess.recommend(new_df, selected_movie_name, 'Files/similarity_tags_genres.pkl'),
            'production': preprocess.recommend(new_df, selected_movie_name, 'Files/similarity_tags_tprduction_comp.pkl'),
            'keywords': preprocess.recommend(new_df, selected_movie_name, 'Files/similarity_tags_keywords.pkl'),
            'cast': preprocess.recommend(new_df, selected_movie_name, 'Files/similarity_tags_tcast.pkl'),
        }
        return render_template('recommend.html', movie_name=selected_movie_name, recommendations=recommendations, zip=zip)
    return render_template('recommend.html', movies=new_df['title'].values)

@app.route('/describe', methods=['GET'])
def describe():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    selected_movie_name = session.get('selected_movie_name', None)
    if not selected_movie_name:
        return redirect(url_for('home'))
    
    # Fetch movie details
    info = preprocess.get_details(selected_movie_name)
    
    # Prepare cast information
    cast = []
    if len(info[14]) > 0:  # Ensure there are cast members
        for cast_id in info[14][:5]:  # Limit to top 5 cast members
            try:
                url, biography = preprocess.fetch_person_details(cast_id)
                cast.append((url, biography))
            except Exception as e:
                print(f"Error fetching cast details for ID {cast_id}: {e}")
    else:
        print("No cast information available.")
        
    return render_template(
        'describe.html',
        movie_name=selected_movie_name,
        info=info,
        cast=cast
    )

@app.route('/movies', methods=['GET', 'POST'])
def movies_page():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    global movies
    if request.method == 'POST':
        page_number = int(request.form.get('page_number', 0))
    else:
        page_number = 0
    
    start = page_number * 10
    movie_list = movies.iloc[start:start + 10]
    return render_template('movies.html', movies=movie_list, page_number=page_number, fetch_posters=preprocess.fetch_posters)

if __name__ == '__main__':
    with Main() as bot:
        bot.main_()
        new_df, movies, movies2 = bot.getter()
        app.run(debug=True)