from fastapi import FastAPI

app=FastAPI()
#  just made a list of items to return the right items for the right get request 
lists={
"market":{
   "carrots":"1$",
   "chips":"2$",
   "milk":"3$",
},
"game shop":{
   "game1":"40$",
   "game2":"20$",
   "game3":"12$",
}

}
# the first GET request for the endpoint '/home'
@app.get('/home')
# this function below is to handle the request and return the string "testing"
def home():
    return "testing"

# the second GET request for the endpoint '/list/market'
@app.get('/list/market')
# this function below is to handle the request for '/list/market' and return the value of the "market" key from the "lists" dictionary
def market():
    return lists["market"]

# the third GET request for the endpoint '/list/game-shop'
@app.get('/list/game-shop')
# this function below is to handle the request for '/list/game-shop' and return the value of the "game shop" key from the "lists" dictionary
def game_shop():
    return lists["game shop"]