import pprint

import boto3

def detectlabels(name):
    client = boto3.client('rekognition')    
    People = Person = Human = Draw = False
    Textfound = "No text found"
    Personfound = "Person not detected"
    	
    response = client.detect_labels(
         Image={
            #'Bytes': b'bytes',
            'S3Object': {
            'Bucket': 'rekbucket',
            'Name': name,
            #'Version': 'string'
        }
    },
    
    MaxLabels=123,
    MinConfidence=90
    )
    checktext = ['Text','Letter','Document','Paper','Page','Flyer','Poster','Btochure','Logo','Handwriting','Trademark','Calligraphy','Label','Art','Doodle','Art','Doodle','Modern Art']
    checkdraw = ['Art','Drawing', 'Sketch']
    if response["Labels"][0]["Name"] in checktext:
       Textfound = "Text Found "
    else:
       for n in range(10):
          try:	   
             if (response["Labels"][n]["Name"] == 'People'):
	                   People = True
	     if (response["Labels"][n]["Name"] == 'Person'):
                           Person = True		
  	     if (response["Labels"][n]["Name"] == 'Human'):
		           Human = True 
             if response["Labels"][n]["Name"] in checkdraw:
		           Draw = True
          except IndexError:      
             if(People) and (Person) and (Human ) and not (Draw):
                   Personfound = "Person Detected"
             else:
                   Personfound = "Person not detected"
    
    return Textfound, Personfound
             
    #pprint.pprint(response)
