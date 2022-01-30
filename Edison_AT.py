from deepface import DeepFace

#database is folder data model face emotion

print("Welcome to Edison AT ^-^\n")

print("----------------------------------------------------\n")

programname= "Edison AT"
version= "1.0"
devdate= "31 January 2022"
devby= "Developed by Ananda Rauf Maududi"
print(programname)
print(version)
print(devdate)
print(devby)

print("----------------------------------------------------\n")


an_emot = DeepFace.stream("database", model_name='DeepFace', actions['emotions']) #Analyze Emotion from face with using library DeepFace
print(an_emot)









