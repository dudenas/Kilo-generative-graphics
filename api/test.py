from datetime import datetime

def handler(request):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': {
            'test': 'API connection successful',
            'timestamp': str(datetime.now()),
            'status': 'working',
            'message': 'Hello from Vercel serverless function!'
        }
    }