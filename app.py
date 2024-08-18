from flask import Flask, render_template, jsonify,request
import longchain as lg

app = Flask(__name__)

license_chain = lg.LicenseChain()
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/creater')
def creater():
    return render_template('creater.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/mine_nft', methods=['POST'])
def mine_nft():
    json_data = request.get_json()
    license_key = json_data.get('license_key')
    software_id = json_data.get('software_id')
    user_id = json_data.get('user_id')
    metadata = json_data.get('metadata')

    try:
        block = license_chain.mint_nft(license_key, software_id, user_id, metadata)
        response = {'message': 'NFT mined successfully!', 'block': block}
        return jsonify(response), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': license_chain.get_chain(),
        'length': len(license_chain.get_chain())
    }
    return jsonify(response), 200

@app.route('/validate_license', methods=['POST'])
def validate_license():
    json_data = request.get_json()
    license_key = json_data.get('license_key')
    software_id = json_data.get('software_id')
    user_id = json_data.get('user_id')

    # Validate the license
    is_valid = license_chain.is_license_valid(license_key, software_id, user_id)

    if is_valid:
        response = {'message': 'License is valid.'}
        return jsonify(response), 200
    else:
        response = {'message': 'License is invalid or not found.'}
        return jsonify(response), 404





if __name__ == ('__main__'):
    app.run(debug=True)