# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:25:51 2021

@author: Max Lipitz
"""


"""


Options For Typographical Imaging System

Please forgive any spelling or Grammer mistakes.
(I'm only Human')

General Options
"""
#Folder In which the Images will be placed as input
#This is the Input Folder   
Img_Folder='Your_Images' 

#The folder where the Output Files will be written to
#You do not need to make this folder it will be automatically made
OutputLocation ='Your_Images_Out'

#Folder To which the images will be sent when done
#You do not need to make this folder it will be automatically made
CompletedImageLocation = 'Your_Images_Done'


# This will tell the program weather to move the image to the CompletedImageLocation
# Folder when its Typographical Image Has been Renderd
# You do not need to make this folder it will be automatically made
Move_Image_When_Done=False

# Weather or not to creat SVG files of the output
Create_SVG=False

# Backround Color: it can be defined is such ways as
# Orange, purple, snow, and many more go to this webste for more info
# https://matplotlib.org/stable/gallery/color/named_colors.html
# You can also put in Average which will give you the mean color.
# You may also define it in Color Hex such as #666666 This is 40% Gray Color
bc_color='black'


# This allows the system to seek out synonyms for labels it does require internet
# once a synonyns is found a text file will be written in the synonyn folder. 
# You do not need to make this folder it will be automatically made. You are more 
# than encorged to modify these files to suite your needs
Use_Synonyms =False


"""
Input Image Size Option
"""
# The Maximum image size allowable it is recomended to stay bellow 3000
# For a Graphics card with 8Gb of RAM: (The larger the long it will take)
MaxSize = 3000

# If the image it above the MaxSize the image will be rescaled
# so that the largest length is this value
# Pleae Note the large the iamge the loger it will take
MaxResSizeSize=2250

# The minimum image size allowable it is recomended to stay above 1000 
# however using the scale can make it larger
MinSize = 1000

#I f the image it below the MinSize the image will be rescaled
# so that the largest length is this value
MinReSize = 1000
"""
Output Image Option
"""
# Upon finishing the typographic Image a copy with increase brightness 
# will also be made
Boost_Brightness=True

# How much to boost the brighness
Brightness_Booster=1.8

# Whould you like to increase the satuation of the brightend up image 
# Another copy will be made
Boost_Saturation=True

# How much to boost the Saturation
Saturation_Booster=1.2



"""
Depth Map Options
"""
# There are two depthmap nural nets each one trained on a different dataset. 
# Both are perfectly servecable however for best of the best resault follows
# Recomendations: nyu or kitti
# nyu: trained on the nyu depth map dataset which was mad with a Microsoft Kinect
# It is ideal for indor spaces such as living rooms and kitchens, bed rooms etc.
# Theother setting is kitti, trained on the kitti dataset this one is more ideal 
# for outdoors and city streets and what have you.  
AdaBins_Dataset='nyu'

"""
Neural Network COCO Dataset Trained Options
"""
# Allows you to skip any label detected Nural Net(NN) Trained on MS COCO
COCOSKIP=[]

#The Min Confidence of Nural Net(NN) Trained on MS COCO 
#This is defined from a value 0 to 1:
#Think of like a confidance score and multiply the trheshold by 100
#Such that 0.5 would mean that only items thet network belives to be 
#50% and greater what it says it is will be detected
COCO_Thresh=0.5

#Whcih Network Are you using all come from FaceBook Detectron2 
#More Info about this one and other can be found here
#https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md
#Please note that if the network is not downloaded it will be autimatically 
#Downloaded. Furthermore This Network Cuently selected is the onw with the 
#highest acuracy and the most computationally expensive the lowest power one is this:
#COCO-InstanceSegmentation/faster_rcnn_R_50_C4_1x.yaml
COCO_Network = "COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml"

"""
Neural Network LVIS Dataset Trained Options
"""
#Allows you to skip any label detected Nural Net(NN) Trained on FB LVIS
#It is recomended that baby be on the skip list. Otherwise anyone who is
#bald or has perfect skin will be Identified as a baby
LVISKIP=['baby']


#it is recomended that the LVIS_Thresh be set at 0.25 or 25%
#This is due to LVIS being a sparse dataset the acuracy of the Network
# is only around 25% percent. This will improve in time stay tuned
LVIS_Thresh=0.25


#This Network Cuently selected is the onw with the 
#highest acuracy and the most computationally expensive the lowest power one is this:
#LVISv0.5-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml
LVIS_Network = "LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml"


"""
Neural Network PanopticSegmentation Trained Options
"""
#Allows you to skip any label detected Nural Net(NN) COCO Pantopic Dataset
PANSKIP=[]

#highest acuracy and the most computationally expensive the lowest power one is this:
#COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.yaml
PAN_Network = "COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml"

'''
Overlap Options 
The system automatically finds and negtiates overlaps 
These are some settings
'''

#This setting allows you to control wether duplicate detection made by the COCO
# Nural Net are inorded or acnologed by other nural nets. Recmonded remain true
# Circumstances this would be usefule is if the first network made a detection 
# another did not.  
Double_Skip_List1=True

#This setting allows you to control wether duplicate detection made by the LVIS
# Nural Net are inorded or acnologed by other nural nets
Double_Skip_List2=True


"""
Facial Recognition and detection Options
"""

# when activated only detections labeld, "person". 
# will be run through facial recognition.
# The facial Recoginiton comes from OSS-celeb-detection Network
# built in facial recognition. That is based on the MTCNN_face_detection_alignment. 
# Created by facenet Guru David Sandberg  
Use_Facial_Rec = True

# When selected all detected faces will be run through key point detection
# This means that it will attempt to find and Mask out Facial Features
# Those Featurse are; Left and Right Eye, Left amd Right Eye-Brow, Nose, 
# Top Lip, Bottom Lip, and Mout.
Use_Facial_Features=True

#Runs the detected face through the OSS-celeb-detection Nural Network
#courtesy of the good folks at Giphy
#It conssits of 2305 celeberty faces attached to a FreeBase ID which is used 
#To Get a general description of the celebrty which is added to the 
#Word Cloud: Please note that once the celberty has been detected 
#a text file will be created that will be used in the future. You are free
#to modify this file as you see fit. 
# To add to the file all you must do is add words to text file with regular spaces. 
# If you would like to add to the Alias or Description catagory use underscores(_) in lue of spaces.  
Use_Celeb_Facial_ID = False

#This allows you to identify custom faces see the file on custome faces
#Etilted HowToCustomFaces.txt or .pdf
Use_Custom_Facial_ID = True

# This will tell the system to weaather to assign a gender to a face and by extention a person.
# I am fully aware that gender is not binary it is spectrum. However, this 
# computer is binary and as resault can only distinguish between Male and Female.
# You are more than welcome to assign a gender by assigning Use_Gender to 
# anything other than False (Which will turn gender ID off). For example 
# Use_Gender='Fluid' (Note you must put '' around the word otherwise it will not work).
# Furthermore, you can change any of the genders in the PeopleInfo folder text files. For 
# example Gender:Female Can be changed to Gender:Fluid as long as there is no spaces.
# One finale note defining a gender here will make it the same for every one in 
# the image. That can be changed in the output text files and re running the program.
Use_Gender = True

#In a similar way to how the gender works you can either disable Emotion identification
#or you can dfine your own which will define it for everyone in the image.
#as before this cam be changed in the output text files and re running the program.  
Use_Emotions=True


#Set the confidance threshold for Celeberty Nural Network. Between 0 and 1  
Celeb_Thresh=0.6

#Set the confidance threshold for Custome Face System. Between 0 and 100 
Custom_Face_Thresh=60


"""
WordCloud Enhanced Features
WordCloud Enhanced is some modification I have made to the wordcloud generator
It allows you to have multiple fonts in a sinlge detection. Note: it will 
not embed fonts when exprting as an SVG. For more info Read the file 
The_Great_River_of_Fonts.txt
To learn more about WordCloud Enhanced please read the file (Word Cloud Enhanced Info.txt)
"""
WordCloud_Enhanced =True

# Will Seek out folders in the font folder with the same name as the label
# This mean that you can define a custome font for a label
Label_Fonts=True

# This allows you to diversify the custom fonts for by adding some extra random ones 
Extra_Fonts=False

#The number of extra random fonts you want to add
Num_Extra_Fonts = 1

# There are three different Font Modes None, 'Local' , and 'Many'
# None: Uses the default font built into the WordCloud API that font is DroidSansMono
# Local:Picks a random font from the font folder and uses it on one object
# Many: Picks a random font from each word: only works with WordCloud_Enhanced.
# Note many can not be used with font embed.
Font_Diversity='Many'
# An easter egg that I have added is that if you set Font Diversity to ComicSins,
# It will set all fonts to Comic Sans MS Regular. I Personaly do not mind the font.
# One of the "benifits" of dyslexia is that I do not have an eye for typefaces.
# As a matter of fact my grandfather to this day still sends E-mails in big blue.
# Comic Sans. However, for the many who see the font as a, "cardinal sin" I thought
# they might enjoy to hate this. Rest asure the font is isolated and 
# will not interfer with the normal operations.
# Please Enjoy ComicSins. ;)


# In the event that a mask size is too small that no words are place. 
# Which Oftern happens with smaller facial features such as the eyes and lips
# Small words the number and size of which you choose can be focable placed in 
# at a random spot in the area. 
Small_Mask_Words = False

# The size of the forcable placed fonts
# Use caution with different scales
Too_Small_Mask_Font_Size=7

Num_XSmal_Words=7


#All letters are CAPITOLIZED
CAP_LOCKS_ON=False

#all letters are lowercase
All_Lower_Case=False

#All Words First Letters are Capitolized 
First_Letter_Capitol=True

#aLl LeTeres ArE RanDomly CaptolLized
Random_Capitol_Letters=False

"""
Stock WordCloud Features
These were written by the brilliant WordCloud creator Andreas Mueller

* Written by me
"""
#How Far the words are from the edge of the mask*
margin=2

#The ratio of times to try horizontal fitting as 
#opposed to vertical. If prefer_horizontal < 1, the algorithm will try 
#rotating the word if it doesn’t fit. 
#(There is currently no built-in way to get only vertical words.)
prefer_horizontal=0.9

#Scaling between computation and drawing. 
#For large word-cloud images, using scale instead of larger canvas size 
#is significantly faster, but might lead to a coarser fit for the words.
scale=3


#The maximum number of words.
max_words=2000 

#Smallest font size to use. Will stop when there is no more room in this size.
min_font_size=4 


#The words that will be eliminated. If None, 
#the build-in STOPWORDS list will be used. 
#Ignored if using generate_from_frequencies.
stopwords=None 

#Random Seed for Recoloring and placment of words I have set to 42. Chosen* 
#because of the works of Douglas Adams and Jackie Robinsons' Numbers*
#Setting to None Will make it truly random
random_state=42 

#Maximum font size for the largest word. If None, height of the image is used.
max_font_size=500 

#Step size for the font. font_step > 1 might speed up computation but give a worse fit.
font_step=1 

# Importance of relative word frequencies for font-size. With relative_scaling=0, 
# only word-ranks are considered. With relative_scaling=1, a word that is twice 
# as frequent will have twice the size. If you want to consider the word 
# frequencies and not only their rank, relative_scaling around .5 often looks good. 
# If ‘auto’ it will be set to 0.5 unless repeat is true, in which case it will be set to 0.
relative_scaling=0  

#If mask is not None and contour_width > 0, draw the mask contour.
contour_width=0 

#Mask contour color.
contour_color='steelblue' 

#Whether to repeat words and phrases until max_words or min_font_size is reached.
repeat=True 

#Whether to include numbers as phrases or not.
include_numbers=False 

#Minimum number of letters a word must have to be included.
min_word_length=0 




