from flask import Flask, jsonify, request
import json

app_pms = Flask(__name__)


# executor = executor(max_workers=3)

@app_pms.route('/api/v1/hotels/1/bookings', methods=['GET'])
def getReservation():
    arrival = request.args.get('arrival')
    client = request.args.get('surname')
    client_info = '{ “booking_id”: "qwertyuiop_id",' \
                  ' “name”: "", “surname”: "{0}", ' \
                  ' “arrival_date”: "{1}",' \
                  ' “departure_date”: "2020-02-02", ' \
                  ' “room_category”: 1, ' \
                  ' “bed_type”: 2, ' \
                  ' “meals”: 3,' \
                  ' “full_price”: "100",' \
                  ' “pay_status”: 1,' \
                  ' “left_to_pay”: 90, ' \
                  ' “card_last_4_digit”: 5555}'.format(client, arrival)
    ans = {'bookings': [
        {
            'person_id': 1,
            'info': json.dumps(client_info)}
    ]
    }
    print('getReservation ans: {0}'.format(ans))
    return jsonify(ans)

if __name__ == '__main__':
    app_pms.run(debug=True, host='0.0.0.0', port=5000)