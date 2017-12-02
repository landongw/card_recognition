THIS EXAMPLE SESSION SHOWS RUNNING TRAINING SET CREATION:

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