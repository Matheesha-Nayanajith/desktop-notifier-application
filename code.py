#let there is no data initially
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

if (covidData != None):
    #converting data into JSON format
    data = covidData.json()['Success']
    
#repeating the loop for multiple times
    while(True):
        notification.notify(
            #title of the notification,
            title = "COVID19 Stats on {}".format(datetime.date.today()),

#the body of the notification
    message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
            totalcases = data['cases'],
            todaycases = data['todayCases'],
            todaydeaths = data['todayDeaths'],
            active = data["active"]),
    
