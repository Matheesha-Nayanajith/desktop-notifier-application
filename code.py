import datetime
import requests as requests
from win10toast import ToastNotifier
import time


def main():
    toaster = ToastNotifier()
    covidData = None
    try:
        covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
    except:
        # if the data is not fetched due to lack of internet
        # reporting data
        print("Please! Check your internet connection")

    if (covidData != None):
        # converting data into JSON format
        # converting part
        data = covidData.json()['Success']

        # repeating the loop for multiple times
        while (True):
            toaster.show_toast(
                "COVID19 Stats on {}".format(datetime.date.today()),
                f"Total cases: {data['cases']}\nToday cases: {data['todayDeaths']}\n"
                f"Today deaths: {data['todayCases']}\nTotal active: {data['active']}",

                # creating icon for the notification
                # we need to download a icon of ico file format
                app_icon="Paomedia-Small-N-Flat-Bell.ico",
                # the notification stays for 50sec
                duration=50
            )
            # sleep for 4 hrs => 60*60*4 sec
            # notification repeats after every 4hrs


if __name__ == '__main__':
    while True:
        main()
        time.sleep(60 * 60 * 4)
