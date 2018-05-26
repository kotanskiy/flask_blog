from flask import Blueprint, render_template, request, redirect, url_for
from models import Post, Tag
from .forms import PostForm
from app import database
from flask_security import login_required

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            database.session.add(post)
            database.session.commit()
        except:
            print('Something wrong')
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(request.form, obj=post)
        form.populate_obj(post)
        database.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit.html', post=post, form=form)


@posts.route('/')
def index():
    search_value = request.args.get('search')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if search_value:
        posts = Post.query.filter(Post.title.contains(search_value) | Post.body.contains(search_value))
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=5)
    return render_template('posts/index.html', posts=posts, pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    return render_template('posts/detail.html', post=post)


@posts.route('/tag/<slug>/')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    # posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag)
