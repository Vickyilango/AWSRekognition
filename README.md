# AWSRekognition
Analyzing Images and Training data for Identification of Impersonation
One of the interesting problems we solved for a customer recently is image moderation at scale. The customer processes close to 2500 user profiles everyday, each user profile consisting an average of 6 different pictures - that makes it processing 15000 user pictures daily.

The customer, who is India's well-known online matrimonial site (for the Western audience reading this, matrimonial sites are roughly equivalent to the dating sites, with blessings from elders and parents) wanted to make sure that the images that are being uploaded are validated for following criteria

Irrelevant photos. A photo is irrelevant if no face is detected
Indecently dressed, nudity.
Group photos are now allowed
Photos that are blurred are not allowed
Celebrity photographs should be rejected.
Match the face from photograph with existing users and check if someone is assuming other's identity
Enter Amazon Rekognition. Ever since Rekognition was introduced at re:invent last year, i have been planning to do this and have done successfully.



STEPS:
1) Configure your instance with AWS
2) Upload your front-end in 'Templates' folder .
3) Upload your js files in 'static' folder.
4) Add your front end to the 'runscript.py' file
5) Run ' python runscript.py'
