from . import admin
from ..decorators import admin_required
from flask_login import login_required

@admin.route('/')
@login_required
@admin_required
def index():
	return "Administration"