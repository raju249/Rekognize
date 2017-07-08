# Rekognize

Rekognize is basically an image processing project that uses Amazon Rekognition and Amazon Polly.

It also uses Raspberry PI (information below of how it's used.)

<img src="http://core0.staticworld.net/images/article/2015/02/raspberry-pi-2-angle-100569133-orig.png" width="250"> + 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/AWS_Simple_Icons_AWS_Cloud.svg/2000px-AWS_Simple_Icons_AWS_Cloud.svg.png" width="250"> = Rekognize

There are 2 modules for this project

### Server

This is the module that interacts with AWS and is responsible for maintaining the reference image vectors mapped to name of the image in person.
This information will be in turn used by Raspberry PI for saying a welcome message along with person's name. This text to speech conversion is done by Amazon Polly and the sound file in transferred to PI for playing. Server uses `Flask` framework to build APIs that will be used by PI.

**Only Server Module interacts with AWS and not PI. PI will communicate with Server to get its work done.**

### Raspberry

PI has a camera and speaker attached to it. Camera is used for clicking live image every 15 seconds and is sent to Server. Server then does the procecssing by calling AWS Rekognition APIs and sends a json response to PI to process along with an audio file to play.

#### Development Credits

* @raju249 (me)

#### Installation Instructions

* Project is in development phase, coming soon Stay tuned :)

