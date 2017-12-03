THIS EXAMPLE SESSION SHOWS RUNNING TRAINING SET CREATION (MAY NOT WORK):

Landons-MBP:card_recognition landonwiedenman$ opencv_createsamples -img /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/ace_of_hearts/ah1.png -bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg.txt -info /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/annotations.lst -pngoutput -maxxangle 0.1 -maxyangle 0.1 -maxzangle 0.1
Info file name: /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/annotations.lst
Img file name: /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/ace_of_hearts/ah1.png
Vec file name: (NULL)
BG  file name: /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg.txt
Num: 1000
BG color: 0
BG threshold: 80
Invert: FALSE
Max intensity deviation: 40
Max x angle: 0.1
Max y angle: 0.1
Max z angle: 0.1
Show samples: FALSE
Width: 24
Height: 24
Max Scale: -1
Create test samples from single image applying distortions...
Open background image: /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/neg/np1.jpg
Open background image: /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/neg/np21.jpg


TODO:

- Complete troubleshooting on new model training for playing cards


CREATING POSITIVE SAMPLES IN VEC FILE:

opencv_createsamples \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-img /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/ace_of_hearts/ah1.png \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg.txt \
-info /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/annotations.lst \  // GET RID OF THIS?
-pngoutput \ // GET RID OF THIS?
-maxxangle 0.1 \
-maxyangle 0.1 \
-maxzangle 0.1


SECOND TRY ON VEC FILE:

opencv_createsamples \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-img /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/sevenhearts.png \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg.txt \
-info /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/annotations.lst \
-maxxangle 0.1 \
-maxyangle 0.1 \
-maxzangle 0.1 \



CASCADE TRAINING:
NOTE: must alter bg.txt file to contain full paths of images

opencv_traincascade \
-data /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/cascade \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg2.txt \
-numPos 30 \
-numNeg 30 \
-numStages 6 \
-featureType HAAR \
-minHitRate 0.999 \
-maxFalseAlarmRate 0.1 \
-w 24 \
-h 24



THIRD TRY:
opencv_createsamples \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-img /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/sevenhearts.png \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg.txt \
-info /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/img/annotations.lst \
-maxxangle 0.1 \
-maxyangle 0.1 \
-maxzangle 0.1



opencv_traincascade \
-data /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/cascade \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg2.txt \
-numPos 30 \
-numNeg 30 \
-numStages 5 \
-featureType HAAR \
-minHitRate 0.999 \
-maxFalseAlarmRate 0.1 \
-w 24 \
-h 24


FOURTH TRY:

VEC GENERATION:

opencv_createsamples \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-img /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/sevenhearts.png \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg.txt \
-maxxangle 0.1 \
-maxyangle 0.1 \
-maxzangle 0.1 \
-w 20 \
-h 30




CASCADE TRAINING:

opencv_traincascade \
-data /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/cascade \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg2.txt \
-numPos 40 \
-numNeg 40 \
-numStages 7 \
-featureType HAAR \
-minHitRate 1 \
-maxFalseAlarmRate 0.4 \
-w 20 \
-h 30





TROUBLSHOOTING DOCS:

https://stackoverflow.com/questions/16058080/how-to-train-cascade-properly
http://answers.opencv.org/question/10872/cascade-training-error-opencv-244-train-dataset-for-temp-stage-can-not-filled-branch-training-terminated-cascade-classifier-cant-be-trained-check-the/