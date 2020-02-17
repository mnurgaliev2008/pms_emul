from flask import Flask, jsonify, request
import json

app_pms = Flask(__name__)

bookings = {"bookings": [
    {
        "booking_id": "1000",
        "name": "ARNOLD",
        "surname": "SCHWARZENEGGER",
        "client_id": "2000",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-01-05T16:00:00+03:00",
        "full_price": 1125000
    },
    {
        "booking_id": "1001",
        "name": "НИКОЛАЙ",
        "surname": "KOLYCHEV",
        "client_id": "2001",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-03-05T16:00:00+03:00",
        "full_price": 1125000
    },
    {
        "booking_id": "1002",
        "name": "ARNOLD",
        "surname": "KOLYCHEV",
        "client_id": "2002",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-02-22T16:00:00+03:00",
        "full_price": 1125000
    },
    {
        "booking_id": "1003",
        "name": "FAINA",
        "surname": "SERGEEVNA",
        "client_id": "2003",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-03-05T16:00:00+03:00",
        "full_price": 1125000
    }
    # {
    #     "booking_id": "2000",
    #     "name": "FAINA",
    #     "surname": "SERGEEVNA",
    #     "client_id": "3333",
    #     "arrival": "2020-01-02T18:00:00+03:00",
    #     "departure": "2020-01-05T16:00:00+03:00",
    #     "full_price": 1125000
    # },
    # {
    #     "booking_id": "2000",
    #     "name": "FAINA",
    #     "surname": "SERGEEVNA",
    #     "client_id": "3333",
    #     "arrival": "2020-01-02T18:00:00+03:00",
    #     "departure": "2020-01-05T16:00:00+03:00",
    #     "full_price": 1125000
    # },
    # {
    #     "booking_id": "2000",
    #     "name": "FAINA",
    #     "surname": "SERGEEVNA",
    #     "client_id": "3333",
    #     "arrival": "2020-01-02T18:00:00+03:00",
    #     "departure": "2020-01-05T16:00:00+03:00",
    #     "full_price": 1125000
    # },
    # {
    #     "booking_id": "2000",
    #     "name": "FAINA",
    #     "surname": "SERGEEVNA",
    #     "client_id": "3333",
    #     "arrival": "2020-01-02T18:00:00+03:00",
    #     "departure": "2020-01-05T16:00:00+03:00",
    #     "full_price": 1125000
    # }
]}
transformed_bookings = {
        "1000": {
            "name": "ARNOLD",
            "surname": "SCHWARZENEGGER",
            "client_id": "2000",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-01-05T16:00:00+03:00",
            "full_price": 1125000
        },
        "1001": {
            "name": "НИКОЛАЙ",
            "surname": "KOLYCHEV",
            "client_id": "2001",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-03-05T16:00:00+03:00",
            "full_price": 1125000
        },
        "1002": {
            "name": "НИКОЛАЙ",
            "surname": "KOLYCHEV",
            "client_id": "2002",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-03-05T16:00:00+03:00",
            "full_price": 1125000
        },
        "1003": {
            "name": "FAINA",
            "surname": "SERGEEVNA",
            "client_id": "2003",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-03-05T16:00:00+03:00",
            "full_price": 1125000
        }
    }


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
    booking_id = request.args.get('booking', None)
    if booking_id is None:
        arrival = request.args.get('arrival')
        print('arrival: {0}'.format(arrival))
        ans = bookings

        # print('getAllBookings ans: {0}'.format(ans))
    else:
        ans = generateBooking(booking_id)
        print('BookingId {0} return {1}'.format(booking_id, ans))
    return jsonify(ans)


def generateBooking(booking_id):
    booking = transformed_bookings[booking_id]
    print('tr_booking: {0}'.format(booking))
    custom_booking = {
        "booking_id": booking_id,
        "hotel_id": "",
        "room_category_id": 4,
        "room_category": "ЛЮКС",
        "room_id": 7,
        "room_number": "105",
        "bed_type": "2",
        "meals": "Завтрак",
        "pay_status": "оплачено частично",
        "left_to_pay": 2275000,
        "card_last_4_digits": 0,
        "satelites": [
            {
                "satelite_number": "01",
                "satelite_clientid": "id_{0}".format(booking_id)
            }
        ]
    }
    custom_booking.update(booking)
    return custom_booking


if __name__ == '__main__':
    app_pms.run(debug=True, host='0.0.0.0', port=5000)
