function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // true for asynchronous 
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
poseNet = ml5.poseNet(video, {
  architecture: 'MobileNetV1',
  imageScaleFactor: 0.3,
  outputStride: 16,
  flipHorizontal: true,
  minConfidence: 0.5,
  scoreThreshold: 0.5,
  nmsRadius: 20,
  detectionType: 'single',
  inputResolution: 513,
  multiplier: 1.0,
  quantBytes: 4,
});

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
