#  -*- coding: utf-8 -*-


from flask import Flask, request, jsonify
from flask_cors import CORS
from chargetracker import process_coordinates

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/api/sendCoordinates', methods=['POST'])
# @cross_origin()
def send_coordinates():
    print("latitude")
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']

    # Pass the coordinates to the chargetracker.py file for processing
    process_coordinates(latitude, longitude)

    return jsonify({'message': 'Coordinates received and processed'})

if __name__ == '__main__':
    app.run()



# from flask import Flask, request, jsonify
# from chargetracker import process_coordinates

# app = Flask(__name__)

# @app.route('/api/sendCoordinates', methods=['POST'])
# def send_coordinates():
#     data = request.json
#     latitude = data['latitude']
#     longitude = data['longitude']

#     # Pass the coordinates to the process_coordinates function
#     process_coordinates(latitude, longitude)

#     return jsonify({'message': 'Coordinates received and processed'})

# if __name__ == '__main__':
#     app.run()












