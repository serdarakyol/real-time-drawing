# REAL TIME DRAW PROJECT
#### This is basic image processing(OpenCV) project. Camera can recognize 4 different color and draw on the output mask. If you want you can specify your own colors. Watch to see how it works on that [LINK](https://www.youtube.com/watch?v=QRh6ZDsbDUg)
#### Please remember; if enviroment light be changed, camera won't recognize the color because your objects color pixels will change.

# USAGE
#### Go to directory
```
cd real-time-drawing
```

#### Create a virtual enviroment and activate that

```
virtualenv venv
source  venv/bin/activate
```

#### You can set your colors via colorRecognize.py 
```
python colorRecognize.py 
```
#### Run colorRecognize.py and set your object colors via trackbar until you have only your object on the screen. Then save these color values on my_colors variable in colordetect.py <br /><br />

#### You are ready to run the project
```
python colordetect.py
```
