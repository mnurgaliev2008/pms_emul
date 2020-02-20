from flask import Flask, jsonify, request
import json

app_pms = Flask(__name__)

bookings = {"bookings": [
    {
        "booking_id": "1000",
        "name": "ARNOLD",
        "surname": "SCHWARZENEGGER",
        "client_id": "2000",
        "arrival": "2020-02-21T18:00:00+03:00",
        "departure": "2020-01-05T16:00:00+03:00",
        "full_price": 1500
    },
    {
        "booking_id": "1001",
        "name": "НИКОЛАЙ",
        "surname": "KOLYCHEV",
        "client_id": "2001",
        "arrival": "2020-02-21T18:00:00+03:00",
        "departure": "2020-03-05T16:00:00+03:00",
        "full_price": 1501
    },
    {
        "booking_id": "1002",
        "name": "ARNOLD",
        "surname": "KOLYCHEV",
        "client_id": "2002",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-02-22T16:00:00+03:00",
        "full_price": 1502
    },
    {
        "booking_id": "1003",
        "name": "FAINA",
        "surname": "SERGEEVNA",
        "client_id": "2003",
        "arrival": "2020-02-22T18:00:00+03:00",
        "departure": "2020-03-05T16:00:00+03:00",
        "full_price": 1503
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
            "full_price": 1500
        },
        "1001": {
            "name": "НИКОЛАЙ",
            "surname": "KOLYCHEV",
            "client_id": "2001",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-03-05T16:00:00+03:00",
            "full_price": 1501
        },
        "1002": {
            "name": "ARNOLD",
            "surname": "KOLYCHEV",
            "client_id": "2002",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-03-05T16:00:00+03:00",
            "full_price": 1502
        },
        "1003": {
            "name": "FAINA",
            "surname": "SERGEEVNA",
            "client_id": "2003",
            "arrival": "2020-02-20T18:00:00+03:00",
            "departure": "2020-03-05T16:00:00+03:00",
            "full_price": 1503
        }
    }


# executor = executor(max_workers=3)

@app_pms.route('/api/v1/', methods=['GET'])
def catch_all_url():
    print('catch_all_url', request.url)


@app_pms.route('/api/v1/hotels/1/clients', methods=['GET'])
def getClientInfo():
    client_id = request.args.get('client', None)
    name, surname, arrival, departure = getClientInfoByClientId(client_id)

    client_info = {
        "client_id": client_id,
        "name": name,
        "surname": surname,
        "arrival": arrival,
        "departure": departure,
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
        print(request.url)
        surname = request.args.get('surname', None)
        print('arrival: {0}'.format(arrival))
        if surname is not None:
            print('surname: {0}'.format(surname))
        ans_booking = []
        ans_id = []
        for item in bookings['bookings']:
            if item['arrival'].startswith(arrival):
                ans_booking.append(item)
                ans_id.append(item['booking_id'])
        ans = {"bookings": ans_booking}
        print('getAllBookings ans: {0}'.format(ans_id))
    else:
        ans = generateBooking(booking_id)
        print('BookingId {0} return {1}'.format(booking_id, ans))
    return jsonify(ans)

def getClientInfoByClientId(client_id):
    print('getClientInfoByClientId client_id: {0}'.format(client_id))
    client_id = '{0}'.format(int(client_id)-1000)
    for item in transformed_bookings.values():
        if client_id == item['client_id']:
            return (item['name'],item['surname'],item['arrival'],item['departure'])

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
                "satelite_clientid": "{0}".format(int(booking_id)+2000)
            }
        ]
    }
    custom_booking.update(booking)
    return custom_booking


if __name__ == '__main__':
    # print (getClientInfoByClientId('2000'))
    app_pms.run(debug=True, host='0.0.0.0', port=5000)
