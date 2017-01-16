from flask import abort, flash, url_for, render_template, redirect, request
from . import client
from .. import db
from ..models import Prof, Client, Booking, Comment
from ..decorators import client_required
from flask_login import login_required, current_user
from .forms import BookingForm, CommentForm

@client.route('/')
@login_required
@client_required
def index():
	return "Client side"
	
@client.route('/profs')
@login_required
@client_required
def profs():
	profs = Prof.query.all()
	client = current_user.client
	return render_template('client/profs.html', profs=profs, client=client)
	
@client.route('/book/prof<int:prof_id>', methods=['GET', 'POST'])
@login_required
@client_required
def book(prof_id):
	form = BookingForm()
	prof = Prof.query.filter_by(id=prof_id).first()
	if prof == None:
		abort(404)
	else:
		client = current_user.client
		if form.validate_on_submit():
			booking = Booking(client=client, prof=prof, time=form.time.data,  start=form.start.data)
			db.session.add(booking)
			db.session.commit()
			flash('booking made')
			return redirect(request.args.get('next') or url_for('main.index') )
	return render_template('client/book.html', form=form, prof=prof)
	
@client.route('/bookings')
@login_required
@client_required
def bookings():
	client = current_user.client
	bookings = Booking.query.filter_by(client=client)
	return render_template('client/bookings.html', bookings=bookings, client=client)
		
@client.route('/booking<int:booking_id>', methods=['GET', 'POST'])
@login_required
@client_required
def booking(booking_id):
	client = current_user.client
	booking = Booking.query.filter_by(id=booking_id).first()
	if (booking == None) | (client != booking.client):
		abort(404)
	else:
		return render_template('client/booking.html', booking=booking, client=client)
	
@client.route('/booking<int:booking_id>/validate')
@login_required
@client_required
def validate(booking_id):
	client = current_user.client
	booking = Booking.query.filter_by(id=booking_id).first()
	if (booking == None) | (client != booking.client) | (booking.done == True):
		abort(404)
	else:
		booking.done = True
		comment = Comment(booking=booking)
		db.session.add(booking)
		db.session.add(comment)
		db.session.commit()
		flash('Booking done')
		return redirect(url_for('client.comment', booking_id = booking.id))
	
@client.route('/booking<int:booking_id>/comment', methods=['GET', 'POST'])
@login_required
@client_required
def comment(booking_id):
	form = CommentForm()
	client = current_user.client
	booking = Booking.query.filter_by(id=booking_id).first()
	comment = booking.comment
	if (booking == None) | (comment == None) | (client != booking.client):
		abort(404)
	if comment.score != None:
		abort(404)
	else:
		if form.validate_on_submit():
			comment.score = form.score.data
			comment.text = form.text.data
			db.session.add(comment)
			db.session.commit()
			return redirect(url_for('client.bookings' ))
		return render_template('client/comment.html', form=form, client=client)
	