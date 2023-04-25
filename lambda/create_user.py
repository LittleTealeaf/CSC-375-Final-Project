import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    # Init the table
    table = client.Table('users')   

    # Process the request
    table.put_item(
      Item={
        
      # Use request ID from context handler to allow for multiple requests - gives uniqueness
      'request_id': context.aws_request_id,
      
        }
      )
      
    # Echo the request from the response
    return {
      'statusCode': 201,
      'body': event
    }

