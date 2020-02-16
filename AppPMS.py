from flask import Flask, jsonify, request
import json

app_pms = Flask(__name__)


# executor = executor(max_workers=3)

@app_pms.route('/api/v1/', methods=['GET'])
def catch_all_url():
    print('catch_all_url', request.url)


@app_pms.route('/api/v1/hotels/1/bookings', methods=['GET'])
def getAllReservation():
    print('url:{0}'.format(request.url))
    print('args: {0}'.format(request.args))
    arrival = request.args.get('arrival')
    print('arrival: {0}'.format(arrival))
    client = request.args.get('surname', 'KOLYCHEV')
    print('client: {0}'.format(client))

    ans = {
        "bookings": [
            {
                "booking_id": "1000",
                "name": "ARNOLD",
                "surname": "SCHWARZENEGGER",
                "clientid": "1111",
                "arrival": "2020-01-02T18:00:00+03:00",
                "departure": "2020-01-05T16:00:00+03:00",
                "full_price": 1125000
            },
            {
                "booking_id": "1049",
                "name": "НИКОЛАЙ",
                "surname": "ГУРБАН",
                "clientid": "1112",
                "arrival": "2020-01-21T18:00:00+03:00",
                "departure": "2020-03-05T16:00:00+03:00",
                "full_price": 1125000
            },
            {
                "booking_id": "2000",
                "name": "ARNOLD",
                "surname": "KOLYCHEV",
                "clientid": "2222",
                "arrival": "2020-01-02T18:00:00+03:00",
                "departure": "2020-01-05T16:00:00+03:00",
                "full_price": 1125000
            },
            {
                "booking_id": "2000",
                "name": "FAINA",
                "surname": "SERGEEVNA",
                "clientid": "3333",
                "arrival": "2020-01-02T18:00:00+03:00",
                "departure": "2020-01-05T16:00:00+03:00",
                "full_price": 1125000
            },
            {
                "booking_id": "2000",
                "name": "FAINA",
                "surname": "SERGEEVNA",
                "clientid": "3333",
                "arrival": "2020-01-02T18:00:00+03:00",
                "departure": "2020-01-05T16:00:00+03:00",
                "full_price": 1125000
            },
            {
                "booking_id": "2000",
                "name": "FAINA",
                "surname": "SERGEEVNA",
                "clientid": "3333",
                "arrival": "2020-01-02T18:00:00+03:00",
                "departure": "2020-01-05T16:00:00+03:00",
                "full_price": 1125000
            },
            {
                "booking_id": "2000",
                "name": "FAINA",
                "surname": "SERGEEVNA",
                "clientid": "3333",
                "arrival": "2020-01-02T18:00:00+03:00",
                "departure": "2020-01-05T16:00:00+03:00",
                "full_price": 1125000
            },
            {
                "booking_id": "2000",
                "name": "FAINA",
                "surname": "SERGEEVNA",
                "clientid": "3333",
                "arrival": "2020-01-02T18:00:00+03:00",
                "departure": "2020-01-05T16:00:00+03:00",
                "full_price": 1125000
            }
        ]
    }

    print('getReservation ans: {0}'.format(ans))
    return jsonify(ans)


if __name__ == '__main__':
    app_pms.run(debug=True, host='0.0.0.0', port=5000)
