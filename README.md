# LaunchInstance-for-Python
## Boto3
### [get_caller_identity](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/get_caller_identity.html)
* __リクエスト__
```
response = client.get_caller_identity()
```
* __レスポンス__
```
{
		'UserId': 'string',
		'Account': 'string',
		'Arn': 'string'
}
```