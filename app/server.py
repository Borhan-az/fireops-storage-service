import os
from flask import Flask, send_from_directory, jsonify, abort

app = Flask(__name__)

STORAGE_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

@app.route('/list-files', methods=['GET'])
def list_files():
    if not os.path.isdir(STORAGE_DIRECTORY):
        return jsonify({"error": "not found"}), 404
    
    try:
        files = [f for f in os.listdir(STORAGE_DIRECTORY) if os.path.isfile(os.path.join(STORAGE_DIRECTORY, f))]
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": "Could not list files."}), 500

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    if not os.path.isdir(STORAGE_DIRECTORY):
        return jsonify({"error": " not found"}), 404

    storage_path = os.path.abspath(STORAGE_DIRECTORY)
    file_path = os.path.abspath(os.path.join(STORAGE_DIRECTORY, filename))


    if not file_path.startswith(storage_path + os.sep):
        return jsonify({"error": "forbidden"}), 403
    
    if not os.path.isfile(file_path):
        abort(404)

    try:
        return send_from_directory(directory=STORAGE_DIRECTORY, path=filename, as_attachment=True)
    except Exception as e:
        abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084, debug=False)
