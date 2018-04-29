from flask import Flask, request, jsonify, render_template
from Main import Main
from Graph import Graph

app = Flask(__name__)

@app.route('/')
def home():
    with app.app_context():
        return render_template('index.html')

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
                'node':graph.getNodes()[i]
            })
        return jsonify(data)

if __name__ == '__main__':
    app.run()