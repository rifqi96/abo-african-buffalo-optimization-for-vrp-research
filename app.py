from flask import Flask, request, jsonify
from Main import Main

app = Flask(__name__)

@app.route('/')
def home():
    with app.app_context():
        response = jsonify({
            'message':'Welcome to the Main App'
        })
        return response

@app.route('/results')
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
                'locations':res['graph'].getNodes(),
                'demands':res['graph'].getDemands(),
                'cost':res['buffalo'].getTotalDistance()
            })
        response = jsonify(data)
        return response

@app.route('/results/<int:depot_index>/<float:lp1>/<float:lp2>/<float:speed>/<int:buffalo_size>/<int:trial_size>/<int:bg_not_updating>/<int:max_demands>', methods=['GET','POST'])
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
                'locations':res['graph'].getNodes(),
                'demands':res['graph'].getDemands(),
                'cost':res['buffalo'].getTotalDistance()
            })
        response = jsonify(data)
        return response

if __name__ == '__main__':
    app.run()