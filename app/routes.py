from app import app
from flask import render_template
from app.forms import DataForm


@app.route('/', methods=['GET', 'POST'])
def search():
    form = DataForm()
    # if form.validate_on_submit():
    #     var = "GOOD!"
    #     return render_template('result.html', var=var)
    return render_template('main_page.html', form=form)







# def index():
#     return render_template('image.html')
