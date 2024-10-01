import json

def lambda_handler(event, context):
    fruit = event['fruit']
    print("This is the Event")
    if fruit == 'apple':
        return {
            'statusCode': 200,
           
            'body': json.dumps(f"I Love {fruit}")
        }
    
    return {
        'statusCode': 200,
       
        'body': json.dumps(f"No Thanks, I don't like {fruit}")
    }
