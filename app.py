from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_flowchart', methods=['POST'])
def create_flowchart():
    try:
        data = request.json
        print("Received data:", data)  # Debugging line
        
        nodes = [f'{node["id"]}["{node["label"]}"]' for node in data['nodes']]
        edges = [f'{edge["from"]} --> {edge["to"]}' for edge in data['edges']]
        
        graph_definition = 'graph TD\n' + '\n'.join(nodes) + '\n' + '\n'.join(edges)

        return jsonify({"graph": graph_definition})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
