from app import app
from flask import render_template
from app.forms import DataForm
from emails_list import my_list


@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = DataForm()
    if form.validate_on_submit():
        # my_list = {1: {'mytsko', 'baran', 'budzhak', 'motso'}, 2: {'smilka', 'soltys'}}
        searching_last_name = str(form.data['last_name']).lower()
        for table, peoples in my_list.items():
            if searching_last_name in peoples:
                our_table = table
                return render_template('search_result.html', our_table=our_table)
    return render_template('main_page.html', form=form)
