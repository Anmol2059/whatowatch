from flask import Flask, render_template, request, redirect, url_for, session
from processing import preprocess
from processing.display import Main

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

displayed = []

# Initialize global variables
movies = None
new_df = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
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
    selected_movie_name = session.get('selected_movie_name', None)
    if not selected_movie_name:
        return redirect(url_for('index'))

    info = preprocess.get_details(selected_movie_name)
    return render_template('describe.html', movie_name=selected_movie_name, info=info)


@app.route('/movies', methods=['GET', 'POST'])
def movies_page():
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
