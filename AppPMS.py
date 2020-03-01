from flask import Flask, jsonify, request
import json, random

app_pms = Flask(__name__)
room_number = 0
booking_info_list = []
bookings = {"bookings": [
    {
        "booking_id": 1000,
        "name": "ARNOLD",
        "surname": "SCHWARZENEGGER",
        "client_id": "2000",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-01-05T16:00:00+03:00",
        "full_price": 1500
    },
    {
        "booking_id": "1001",
        "name": "НИКОЛАЙ",
        "surname": "KOLYCHEV",
        "client_id": "2001",
        "arrival": "2020-02-20T18:00:00+03:00",
        "departure": "2020-03-05T16:00:00+03:00",
        "full_price": 1501
    },
    {
        "booking_id": "1002",
        "name": "ARNOLD",
        "surname": "KOLYCHEV",
        "client_id": "2002",
        "arrival": "2020-02-21T18:00:00+03:00",
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
]}


def getClientFromBookings(client_id):
    print('getClientInfoByClientId client_id: {0}'.format(client_id))
    return next(((item['name'],item['surname'],item['arrival'],item['departure'], item['room_id']) for item in booking_info_list if item['client_id']=='{0}'.format(client_id)), None)


def getBooking(booking_id):
    return next((item for item in bookings['bookings'] if item['booking_id']==booking_id), None)

def getBookingInfo(booking_id, hotel_id):
    return next((item for item in booking_info_list if item['booking_id']=='{}'.format(booking_id) and item['hotel_id']=='{}'.format(hotel_id)),None)

def generateBooking(booking_id, hotel_id):
    global room_number, booking_info_list
    room_number+=1
    booking = getBooking(booking_id)
    print('tr_booking: {0}'.format(booking))
    booking_info = {
        "booking_id": booking_id,
        "name": booking['name'],
        "surname": booking['surname'],
        "client_id": booking['client_id'],
        "arrival": booking['arrival'],
        "departure": booking['departure'],
        "full_price": booking['full_price'],
        "hotel_id": "{0}".format(hotel_id),
        "room_category_id": 4,
        "room_category": "ЛЮКС",
        "room_id": "{0}".format(room_number),
        "room_number": "{0}".format(room_number),
        "bed_type": "2",
        "meals": "Завтрак",
        "pay_status": "оплачено частично",
        "left_to_pay": 10000,
        "card_last_4_digits": 1324,
        "satelites": [
            {
                "satelite_number": "01",
                "satelite_clientid": "{0}".format(int(booking_id)+2000)
            }
        ]
    }
    booking_info_list.append(booking_info)
    return booking_info

@app_pms.route('/api/v1/hotels/1/clients', methods=['GET'])
def getClientInfo():
    client_id = int(request.args.get('client', None))-1000
    name, surname, arrival, departure, room_id = getClientFromBookings(client_id)
    client_info = {
        "client_id": client_id,
        "name": name,
        "surname": surname,
        "arrival": arrival,
        "departure": departure,
        "hotel_id": "",
        "room_id": "{0}".format(room_id),
        "services": []
    }
    return jsonify(client_info)

@app_pms.route('/api/v1/hotels/<hotel_id>/bookings/<booking_id>/keys', methods=['POST'])
def postKeys(hotel_id, booking_id):
    print('postKeys: hotel_id={0}, booking_id{1}'.format(hotel_id,booking_id))
    return jsonify({})



@app_pms.route('/api/v1/hotels/<hotel_id>/bookings', methods=['GET'])
def getAllBookings(hotel_id):
    booking_id = request.args.get('booking', None)
    if booking_id is None:
        arrival = request.args.get('arrival')
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
        booking_info = getBookingInfo(booking_id,hotel_id)
        ans = booking_info if booking_info else generateBooking(booking_id, hotel_id)
        print('BookingId {0} return {1}'.format(booking_id, ans))
    return jsonify(ans)

@app_pms.route('/api/v1/hotels/1/bookings/<booking_id>/pay', methods=['POST'])
def pay(booking_id):
    print('booking_id: {0}'.format(booking_id))
    for item in booking_info_list:
        if item['booking_id']=='{0}'.format(booking_id):
            item['pay_status']='ОПЛАЧЕНО'
    return jsonify({'is_money_back': True})



if __name__ == '__main__':
    # print (getClientFromBookings(2001))
    app_pms.run(debug=True, host='0.0.0.0', port=5000)
