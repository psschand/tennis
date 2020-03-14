'''
Created on Mar 10, 2020

@author: surya
'''
import demjson
import simplejson as json
from flask import Flask, flash, render_template, redirect, url_for, request, session, jsonify
from module.database import Database
from flask import abort

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()


@app.route('/batch', methods=['POST'])
def batch():
    """
    Execute multiple requests, submitted as a batch.
    """
    try:
        requests = json.loads(request.data)
    except ValueError as e:
        abort(400)

    responses = []

    for index, req in enumerate(requests):

        # body = req.get('body', None)
        if db.insert(req):
            response = "successful"
        else:
            response = "failed"

        responses.append({
            "response": response
        })

    return json.dumps(responses)


@app.route('/hello', methods=['GET'])
def hello():
    """
       initial  Test endpoint
    """
    return jsonify({'hello': 'world'})


@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data=data)


@app.route('/add/')
def add():
    return render_template('add.html')


@app.route('/addtennis', methods=['POST', 'GET'])
def addtennis():
    """
        insert data from UI
    """
    if request.method == 'POST' and request.form['save']:
        # print(request.form)
        if db.insert(request.form):
            flash("new tennis data has been added")
        else:
            flash("new tennis data can not be added")

        return redirect(url_for('index'))
    else:
        # return redirect(url_for('index'))
        data = request.get_json()
        if db.insert(data):
            return jsonify({"new tennis data has been added", data})
        else:
            return jsonify({" new  tennis data can not be added", data})


@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data=data)


@app.route('/updatetennis', methods=['POST'])
def updatetennis():
    """
        Endpoind to update the data
    """
    if request.method == 'POST' and request.form['update']:
        if db.update(session['update'], request.form):
            flash('tennis data has been updated')

        else:
            flash('tennis data can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/delete/<int:id>/')
def delete(id):
    """
        end point to delete a particular id
    """
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data=data)


@app.route('/deletetennis', methods=['POST'])
def deletetennis():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('tennis data has been deleted')

        else:
            flash('tennis data can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0",debug=True)
    # app.run(debug=True)
