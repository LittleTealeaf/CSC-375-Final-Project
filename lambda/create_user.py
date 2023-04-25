import boto3

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    # Init the table
    table = client.Table('users')   

    # Process the request
    table.put_item(
      Item={
        
      # Use request ID from context handler to allow for multiple requests - gives uniqueness
      'request_id': context.aws_request_id,
      'first_name': event.get('first_name'),
      'last_name': event.get('last_name'),
      'email': event.get('email'),
      'university': event.get('university'),
      'degree': event.get('degree'),
      'about_me': event.get('about_me')
        }
      )
      
    # Echo the request from the response
    return {
      'statusCode': 201,
      'body': event
    }

