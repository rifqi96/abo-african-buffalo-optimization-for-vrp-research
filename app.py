from flask import Flask, request, jsonify, render_template, url_for, redirect
from Main import Main
from Graph import Graph
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'abo-vrp-anya')

@app.route('/')
def home():
    # return render_template('index.html')
    return jsonify(message="Welcome to the main app")

@app.route('/api/results')
def results():
    with app.app_context():
        data = []
        main = Main()
        main.generateResults()
        for res in main.results:
            data.append({
                'buffalo_no':res['buffalo_no'],
                'total_demands':res['total_demands'],
                'routes':res['real_nodes'],
                'graph':{
                    'name':res['graph'].getLocationNames(),
                    'coor':res['graph'].getLongLat(),
                    'node':res['graph'].getNodes(),
                    'demands':res['graph'].getDemands()
                },
                'cost':res['buffalo'].getTotalDistance()
            })
        response = jsonify(data)
        return response

@app.route('/api/results/<int:depot_index>/<float:lp1>/<float:lp2>/<float:speed>/<int:buffalo_size>/<int:trial_size>/<int:bg_not_updating>/<int:max_demands>', methods=['GET','POST'])
def customResults(depot_index, lp1, lp2, speed, buffalo_size, trial_size, bg_not_updating, max_demands):
    with app.app_context():
        data = []
        main = Main()
        results = main.generateResults(depot_index, [lp1, lp2], speed, buffalo_size, trial_size, bg_not_updating, max_demands)
        if results is None:
            return jsonify(message='Error Happens'), 500

        if results['status'] is False:
            return jsonify(message=results['message']), 500

        for res in results['data']:
            data.append({
                'buffalo_no':res['buffalo_no'],
                'total_demands':res['total_demands'],
                'routes':res['real_nodes'],
                'graph':{
                    'name':res['graph'].getLocationNames(),
                    'coor':res['graph'].getLongLat(),
                    'node':res['graph'].getNodes(),
                    'demands':res['graph'].getDemands()
                },
                'cost':res['buffalo'].getTotalDistance()
            })
        response = jsonify(data)
        return response

@app.route('/api/nodes')
def getNodes():
    with app.app_context():
        graph = Graph()
        size = len(graph.getLocationNames())
        data = []
        for i in xrange(size):
            data.append({
                'name':graph.getLocationNames()[i],
                'coor':graph.getLongLat()[i],
                'node':graph.getNodes()[i],
                'demands':graph.getDemands()[i],
                'distances': graph.getDistance()[i]
            })
        return jsonify(data)

@app.errorhandler(404)
def pageNotFound(error):
    return jsonify(message='Hi fella, are you lost?'), 404

if __name__ == '__main__':
    app.run(debug=True)