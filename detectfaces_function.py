import pprint

import boto3


def detectfaces(name):
	
	client = boto3.client('rekognition')
	
	Group = "Single face "
	Noface = "Face Detected"
        Male = "No Gender"
	
	
	response = client.detect_faces(
				Image={
			    #'Bytes': b'bytes',
				'S3Object': {
				'Bucket': 'rekbucket',
				'Name': name,
				#'Version': 'string'
				}
	},
	Attributes=[
		'ALL'
		]
    
	)
	try:  
	    bool(response["FaceDetails"][1])
	    Group = "Many Face Detected"
	except IndexError:
	    if not (bool(response["FaceDetails"])):
		    Noface = "Face not found"
	    else:
       		 Gender = response["FaceDetails"][0]["Gender"]["Value"]
                 if (Gender == 'Male'):
		    Male = "Male"
      	         if (Gender == 'Female'):
                    Male = "Female"			
        
        return Group, Noface, Male
