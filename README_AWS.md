### Set AWS Profile

```
vi ~/.aws/credentials

[profile-name]
aws_access_key_id = <aws_access_key_id>
aws_secret_access_key = <aws_secret_access_key>

```

### Login to AWS ECR

```
aws ecr get-login-password --region {AWS_REGION} --profile {AWS_PROFILE} | docker login --username AWS --password-stdin {ECR_URL}
aws ecr get-login-password --region us-east-1 --profile personal | docker login --username AWS --password-stdin 672256646492.dkr.ecr.us-east-1.amazonaws.com
```

### Docker Build
```
docker build -t project-apple-repository .
docker build --no-cache -t project-apple-repository .
docker buildx build --no-cache --platform linux/amd64 -t project-apple-repository .
docker buildx build --platform linux/amd64 -t project-apple-repository .
```

### Build Tag
```
docker tag project-apple-repository:latest 672256646492.dkr.ecr.us-east-1.amazonaws.com/project-apple-repository:latest
```

### Push to AWS ECR
```
docker push 672256646492.dkr.ecr.us-east-1.amazonaws.com/project-apple-repository:latest
```