#!/usr/bin/env python3
import boto3

# Инициализация клиента EC2
ec2_client = boto3.client('ec2', region_name='us-east-1')

def list_ec2_instances():
    try:
        # Запрос на получение списка инстансов
        response = ec2_client.describe_instances()

        # Обработка ответа
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                instance_type = instance['InstanceType']
                launch_time = instance['LaunchTime']
                
                # Получение тегов (например, Name)
                name_tag = 'N/A'
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        name_tag = tag['Value']
                
                # Вывод информации об инстансе
                print(f"Instance ID: {instance_id}")
                print(f"Name: {name_tag}")
                print(f"State: {state}")
                print(f"Instance Type: {instance_type}")
                print(f"Launch Time: {launch_time}")
                print("-" * 50)

    except Exception as e:
        print(f"Error: {str(e)}")

# Вызов функции
list_ec2_instances()
