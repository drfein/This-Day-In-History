import schedule, time, requests
from datetime import date

from twilio.rest import Client
from credentials import cellphoneList, twilio_account, twilio_token, twilio_number

def send_message():

    today = date.today()
    day = today.day
    month = today.month
    response = requests.get("http://numbersapi.com/" + str(month) + "/" + str(day) + "/date")
    message = response.text

    account = twilio_account
    token = twilio_token
    client = Client(account, token)

    for number in cellphoneList:
        client.messages.create(to=number,
                            from_=twilio_number,
                            body=message
                            )


# send a message in the morning
schedule.every().day.at("08:00").do(send_message)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)