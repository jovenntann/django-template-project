## Getting Started

For more information on getting started, visit the [Serverless Framework Documentation](https://www.serverless.com/framework/docs/getting-started).

### AWS Profile Setup

To set up the AWS profile on a Mac, update the AWS profile file by running the following commands in your terminal:

```
vi ~/.aws/credentials
```

This will open the credentials file in your default text editor. Add your AWS credentials in the following format:

```
[personal]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

Replace `YOUR_ACCESS_KEY` and `YOUR_SECRET_KEY` with your actual AWS access key and secret key. Save and close the file.




### Installation

1. Install Serverless globally:

```
npm install -g serverless
```

2. Create a virtual environment and activate it:

```
python3.9 -m venv ./venv
source ./venv/bin/activate
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

### Plugins

1. Install the Serverless WSGI plugin:

```
serverless plugin install -n serverless-wsgi
```

2. Install the Serverless Python Requirements plugin:

```
serverless plugin install -n serverless-python-requirements
```

### Deployment

1. Deploy the Serverless application:

```
serverless deploy --aws-profile personal
```

2. To remove the Serverless application:

```
sls remove --aws-profile personal
```

### Local Development

To serve the application locally:

```
serverless wsgi serve
```