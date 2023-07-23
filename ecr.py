import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html
ecr_client = boto3.client('ecr')

repository_name = "my-cloud-native-repo"
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr/client/create_repository.html
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)


#########THIS CAN ALSO BE DONE USING THE GUI QUICKER! but just wanted to illustrate how boto3 can be used to do this as well :)