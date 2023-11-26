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

1. Install the Serverless Requirements:

```
serverless plugin install -n serverless-wsgi
serverless plugin install -n serverless-python-requirements
serverless plugin install -n serverless-domain-manager
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



To attach a subdomain to your serverless application, you can use the serverless-domain-manager plugin. However, if your domain is not hosted on AWS Route 53, you will need to manually configure your DNS settings in your domain provider to point to the AWS resources created by the plugin.

Here's how you can do it:

1. Install the serverless-domain-manager plugin:

```
npm install serverless-domain-manager --save-dev
```

2. Add the plugin to your serverless.yml file:

```
plugins:
  - serverless-wsgi
  - serverless-python-requirements
  - serverless-domain-manager
```

3. Configure the custom domain in the custom section of your serverless.yml file:

```
custom:
  wsgi:
    app: app.app
  customDomain:
    domainName: subdomain.yourdomain.com
    basePath: 'api'
    stage: ${self:provider.stage}
    createRoute53Record: false
```

In this configuration, replace subdomain.yourdomain.com with your actual subdomain. The basePath is the path prefix for your API, and stage is the deployment stage of your service. The createRoute53Record is set to false because your domain is not managed by Route 53.

4. Deploy your service:

```
sls delete_domain
sls deploy
``````

After deploying, the plugin will output the distribution domain name of your API Gateway. You will need to create a CNAME record in your domain provider's DNS settings to point your subdomain to this distribution domain name.

Please note that DNS changes can take up to 48 hours to propagate.

```
✔ Service deployed to stack aws-python-flask-api-dev (79s)

endpoint: ANY - https://gyow88t88j.execute-api.us-east-1.amazonaws.com
functions:
  api: aws-python-flask-api-dev-api (10 MB)
Serverless Domain Manager:
  Domain Name: sls.tappy.com.ph
  Target Domain: d-kme68a0py3.execute-api.us-east-1.amazonaws.com -- this is what we need to create on a dns records
  Hosted Zone Id: Z1UJRXOUMOOFQ8
```