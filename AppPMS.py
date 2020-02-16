from flask import Flask, jsonify, request
import json

app_pms = Flask(__name__)


# executor = executor(max_workers=3)

@app_pms.route('/api/v1/', methods=['GET'])
def catch_all_url():
    print('catch_all_url', request.url)

@app_pms.route('/api/v1/hotels/1/clients', methods=['GET'])
def getClientInfo():
    client_id = request.args.get('client', None)
    client_info = {
        "client_id": client_id,
        "name": "Два",
        "surname": "KOLYCHEV2",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-02-22T16:00:00+03:00",
        "hotel_id": "",
        "room_id": "6",
        "services": []
    }
    return jsonify(client_info)

@app_pms.route('/api/v1/hotels/1/bookings', methods=['GET'])
def getAllBookings():
    print('url:{0}'.format(request.url))
    print('args: {0}'.format(request.args))
    booking_id = request.args.get('booking', None)
    if booking_id is None:

        arrival = request.args.get('arrival')
        print('arrival: {0}'.format(arrival))
        ans = {
            "bookings": [
                # {
                #     "booking_id": "1000",
                #     "name": "ARNOLD",
                #     "surname": "SCHWARZENEGGER",
                #     "clientid": "1111",
                #     "arrival": "2020-02-02T18:00:00+03:00",
                #     "departure": "2020-01-05T16:00:00+03:00",
                #     "full_price": 1125000
                # }
                # {
                #     "booking_id": "1049",
                #     "name": "НИКОЛАЙ",
                #     "surname": "ГУРБАН",
                #     "clientid": "1112",
                #     "arrival": "2020-01-21T18:00:00+03:00",
                #     "departure": "2020-03-05T16:00:00+03:00",
                #     "full_price": 1125000
                # },
                {
                    "booking_id": "2000",
                    "name": "ARNOLD",
                    "surname": "KOLYCHEV",
                    "clientid": "2222",
                    "arrival": "2020-02-20T18:00:00+03:00",
                    "departure": "2020-02-22T16:00:00+03:00",
                    "full_price": 1125000
                }
                # {
                #     "booking_id": "2000",
                #     "name": "FAINA",
                #     "surname": "SERGEEVNA",
                #     "clientid": "3333",
                #     "arrival": "2020-01-02T18:00:00+03:00",
                #     "departure": "2020-01-05T16:00:00+03:00",
                #     "full_price": 1125000
                # }
                # {
                #     "booking_id": "2000",
                #     "name": "FAINA",
                #     "surname": "SERGEEVNA",
                #     "clientid": "3333",
                #     "arrival": "2020-01-02T18:00:00+03:00",
                #     "departure": "2020-01-05T16:00:00+03:00",
                #     "full_price": 1125000
                # },
                # {
                #     "booking_id": "2000",
                #     "name": "FAINA",
                #     "surname": "SERGEEVNA",
                #     "clientid": "3333",
                #     "arrival": "2020-01-02T18:00:00+03:00",
                #     "departure": "2020-01-05T16:00:00+03:00",
                #     "full_price": 1125000
                # },
                # {
                #     "booking_id": "2000",
                #     "name": "FAINA",
                #     "surname": "SERGEEVNA",
                #     "clientid": "3333",
                #     "arrival": "2020-01-02T18:00:00+03:00",
                #     "departure": "2020-01-05T16:00:00+03:00",
                #     "full_price": 1125000
                # },
                # {
                #     "booking_id": "2000",
                #     "name": "FAINA",
                #     "surname": "SERGEEVNA",
                #     "clientid": "3333",
                #     "arrival": "2020-01-02T18:00:00+03:00",
                #     "departure": "2020-01-05T16:00:00+03:00",
                #     "full_price": 1125000
                # }
            ]
        }

        print('getAllBookings ans: {0}'.format(ans))

    else:
        ans = {
            "booking_id": booking_id,
            "client_id": "1112",
            "name": "НИКОЛАЙ",
            "surname": "KOLYCHEV",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-02-22T16:00:00+03:00",
            "hotel_id": "",
            "room_category_id": 4,
            "room_category": "ЛЮКС",
            "room_id": 7,
            "room_number": "105",
            "bed_type": "2",
            "meals": "Завтрак",
            "full_price": 2310000,
            "pay_status": "оплачено частично",
            "left_to_pay": 2275000,
            "card_last_4_digits": 0,
            "satelites": [
                {
                    "satelite_number": "01",
                    "satelite_clientid": "3333"
                }
            ]
        }
        print('getBooking for booking_id {0} ans: {1}'.format(booking_id,ans))

    return jsonify(ans)


if __name__ == '__main__':
    app_pms.run(debug=True, host='0.0.0.0', port=5000)