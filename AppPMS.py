from flask import Flask, jsonify, request
import json

app_pms = Flask(__name__)


# executor = executor(max_workers=3)

@app_pms.route('/api/v1/', methods=['GET'])
def catch_all_url():
    print('catch_all_url', request.url)

@app_pms.route('/api/v1/hotels/1/bookings', methods=['GET'])
def getReservation():
    print('url:{0}'.format(request.url))
    print('args: {0}'.format(request.args))
    arrival = request.args.get('arrival')
    print('arrival: {0}'.format(arrival))
    client = request.args.get('surname')
    print('client: {0}'.format(client))
    client_info = {'booking_id': "qwertyuiop_id",  'name': '',
                    'surname': client,
                   'arrival_date':  arrival,
                   'departure_date': '2020-02-22',
                   'room_category': 1,
                   'bed_type': 2,
                   'meals': 3,
                   'full_price': "100",
                   'pay_status': 1,
                   'left_to_pay': 90,
                   'card_last_4_digit': 5555}
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