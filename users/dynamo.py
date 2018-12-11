import os
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import json
import uuid

ddb = boto3.resource('dynamodb',
                         endpoint_url="http://localhost:8000")
ddb_table = "users"

table = ddb.Table(ddb_table)
ret = table.scan()
print(ret["Items"])