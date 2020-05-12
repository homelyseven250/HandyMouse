function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}


video = document.getElementById('video');

if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
      video.srcObject = stream;
      video.play();
  });
}

// Create a new poseNet method
poseNet = ml5.poseNet(video, modelLoaded);

// When the model is loaded
function modelLoaded() {
  console.log('Model Loaded!');
}

function log(text) {
  console.log(text)
}
// Listen to new 'pose' events
poseNet.on('pose', (results) => {
  poses = results[0]
  keypoints = poses["pose"]
  console.log(keypoints)
  var leftWrist = keypoints["leftWrist"]
  console.log(leftWrist)
  var leftX = leftWrist["x"]
  var leftY = leftWrist["y"]
  var rightWrist = keypoints["rightWrist"]
  var rightX = rightWrist["x"]
  var rightY = rightWrist["y"]
  httpGetAsync(`/send-data?leftX=${leftX}&leftY=${leftY}&rightX=${rightX}&rightY=${rightY}`, log)
});
