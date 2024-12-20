from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
import os
from .models import db, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = [
        {'name': 'Product 1', 'description': 'Description of product 1', 'price': '$10'},
        {'name': 'Product 2', 'description': 'Description of product 2', 'price': '$20'},
        {'name': 'Product 3', 'description': 'Description of product 3', 'price': '$30'},
    ]
    return render_template('index.html', user=current_user, products=products)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@main.route('/upload_image', methods=['GET', 'POST'])
@login_required
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            # Ensure the directory exists
            upload_folder = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            current_user.image_file = filename
            db.session.commit()
            flash('Your profile image has been updated!')
            return redirect(url_for('main.profile'))
    return render_template('upload_image.html')

@main.route('/edit_image', methods=['GET', 'POST'])
@login_required
def edit_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            # Ensure the directory exists
            upload_folder = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            current_user.image_file = filename
            db.session.commit()
            flash('Your profile image has been updated!')
            return redirect(url_for('main.profile'))
    return render_template('edit_image.html')
