# Example (Mint)

This example adds a button that gets the server to send a request to another pico (the one that monitors light levels in the makerspace)


## Create button (html) (index.html)
Inside the ```index.html``` file's ```<body>``` tags add code for a button and a DIV to put the returned information:
```html
    <input id="lightLevelButton" type="button" value="Get Light Level From Makerspace Demo PicoW">
    <div id="MkspPhotoResistor"></div>
```
Give each thing a unique ```id``` ("timeBut" in this case). The ```value```  of the button shows up on the button. The text between the div tags ("Time") shows up on the webpage as a default.

## Send message on click (JavaScript) (index.html)
Inside the ```index.html``` file's ```<script>``` tags add code to detect a click on the button and send message to server:
```js
    lightLevelButton.addEventListener("click", function(){
        sendRequest("/", "photoResistor");
    })
```
The first argument ("/"), indicates the base of the webpage url (does not need to change), and the second argument is the ```action``` paramenter that's sent to the server (see the protocol). A third argument would be the ```value``` parameter that is not needed in this case.

The message is sent as a POST request.

## Server Recieve Message (code.py)
The server recieves the POST message sent to "/" and sends it to the ```handlePost``` function:
```python
async def handlePost(request):
```

Data recieved with the right style/protocol (see the main README.md file) will be accessible as:
```python
data['action']
data['value']
```

In this case the data['action'] is "photoResistor", so we create an if statement to deal with any messages who's action is "getTime".
```python
    if data['action'] == 'photoResistor':
        # send request to the Makerspace picoW with the photoresistor
        info = await postRequest("20.1.0.96:80", action="photoResistor", value="")
        print("Requested from pr Pico: ", info)
        rData = json.loads(info)
```

Notice that ```rData```, which is returned to the client (webpage) at the end of the function, is set to the "info" returned by the postRequest to the Makerspace's Testing PicoW that keeps track of the light level. So, this server is, basically, passing along the request to the Light Level Testing PicoW and returning the response from that device.

## Webpage handles the reply
The reply from the server gets caught by the ```sendRequest``` function on the webpage, in the ```//Handle responses``` section. The response is captured and put into the ```data``` dictionary (which is the ```rData``` dictionary that was returned from the server, renamed as 'data["item"]' and 'data["status"]'). In this example, the "status" is put into the DIV with the id "MkspPhotoResistor" on the webpage with:
```js
                //Handle responses
                if (data["item"] == "photoResistor") {
                    console.log("Light Level: ", data["status"]);
                    MkspPhotoResistor.innerText = data["status"];
                }
```

## Test
* Run:
```bash
python3 server.py
```
* Go to the web site's url, which is output to the terminal as, for example:
```
Server running at http://20.1.0.233:8080/
```
* Click on the "Get Light Level From Makerspace Testing PicoW" button

