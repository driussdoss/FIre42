
# ☁️ **Полная база по boto3 (DevOps-ready)**

---

## 🧩 1. Установка и подключение

```bash
pip install boto3
aws configure
```

(вводишь `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `region`)

---

## ⚙️ 2. Клиенты и ресурсы

```python
import boto3

# Низкоуровневый клиент (всё через методы API)
ec2 = boto3.client("ec2")

# Высокоуровневый ресурс (объектно-ориентированный интерфейс)
s3 = boto3.resource("s3")
```

---

## 🗂️ 3. Работа с **S3 (Storage)**

### ➕ Создать бакет

```python
s3 = boto3.client("s3")
s3.create_bucket(Bucket="my-new-bucket-2025")
```

### 📤 Загрузить файл

```python
s3.upload_file("local.txt", "my-new-bucket-2025", "uploads/local.txt")
```

### 📥 Скачать файл

```python
s3.download_file("my-new-bucket-2025", "uploads/local.txt", "downloaded.txt")
```

### 🗑️ Удалить файл

```python
s3.delete_object(Bucket="my-new-bucket-2025", Key="uploads/local.txt")
```

### 🧹 Удалить бакет

```python
s3.delete_bucket(Bucket="my-new-bucket-2025")
```

---

## 🖥️ 4. Работа с **EC2 (виртуальные машины)**

EC2 используется для управления серверами: запуск, остановка, удаление, получение статуса.

---

### 🚀 Запуск инстанса

```python
import boto3

ec2 = boto3.client("ec2")

instance = ec2.run_instances(
    ImageId="ami-0abcdef1234567890",  # заменить на актуальный AMI ID
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="my-keypair",  # ключ для SSH
    SecurityGroupIds=["sg-0123456789abcdef0"]
)

print("Создан EC2:", instance["Instances"][0]["InstanceId"])
```

---

### 🛑 Остановка / Запуск

```python
instance_id = "i-0123456789abcdef0"

# Остановить
ec2.stop_instances(InstanceIds=[instance_id])

# Запустить
ec2.start_instances(InstanceIds=[instance_id])
```

---

### 🧾 Получить список и состояние

```python
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"], "-", instance["State"]["Name"])
```

---

### ✏️ Изменить тип инстанса (модификация)

⚠️ Нужно остановить инстанс перед изменением типа.

```python
ec2.stop_instances(InstanceIds=["i-0123456789abcdef0"])
ec2.modify_instance_attribute(
    InstanceId="i-0123456789abcdef0",
    InstanceType={"Value": "t3.micro"}
)
ec2.start_instances(InstanceIds=["i-0123456789abcdef0"])
```

---

### ❌ Удалить (terminate)

```python
ec2.terminate_instances(InstanceIds=["i-0123456789abcdef0"])
```

---

## 🌐 5. Работа с **ELB (Elastic Load Balancer)**

Используется для балансировки нагрузки между EC2-серверами.

---

### ⚙️ Создание балансировщика (Application Load Balancer)

```python
elbv2 = boto3.client("elbv2")

response = elbv2.create_load_balancer(
    Name="my-load-balancer",
    Subnets=["subnet-0123456789abcdef0", "subnet-0abcdef1234567890"],
    SecurityGroups=["sg-0123456789abcdef0"],
    Scheme="internet-facing",
    Type="application",
    IpAddressType="ipv4"
)

print("Создан ELB:", response["LoadBalancers"][0]["DNSName"])
```

---

### 🎯 Создание Target Group

```python
target_group = elbv2.create_target_group(
    Name="my-target-group",
    Protocol="HTTP",
    Port=80,
    VpcId="vpc-0123456789abcdef0"
)
```

---

### 🔗 Привязка Target Group к балансировщику

```python
elbv2.create_listener(
    LoadBalancerArn=response["LoadBalancers"][0]["LoadBalancerArn"],
    Protocol="HTTP",
    Port=80,
    DefaultActions=[{
        "Type": "forward",
        "TargetGroupArn": target_group["TargetGroups"][0]["TargetGroupArn"]
    }]
)
```

---

## 🔐 6. Работа с **IAM (доступ и пользователи)**

### 📋 Список пользователей

```python
iam = boto3.client("iam")

users = iam.list_users()
for user in users["Users"]:
    print(user["UserName"])
```

---

### ➕ Создание пользователя

```python
iam.create_user(UserName="devops_user")
```

---

### 🔑 Создание access key

```python
key = iam.create_access_key(UserName="devops_user")
print(key["AccessKey"]["AccessKeyId"])
```

---

## 🧩 7. Работа с **CloudWatch (мониторинг)**

### 📈 Получить метрики CPU

```python
cloudwatch = boto3.client("cloudwatch")

metrics = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[{"Name": "InstanceId", "Value": "i-0123456789abcdef0"}],
    StartTime=datetime.utcnow() - timedelta(hours=1),
    EndTime=datetime.utcnow(),
    Period=300,
    Statistics=["Average"]
)

for datapoint in metrics["Datapoints"]:
    print(datapoint["Timestamp"], "-", datapoint["Average"])
```

---

## 🧰 8. Полезные приёмы для DevOps

| Задача                              | Метод                                            |
| ----------------------------------- | ------------------------------------------------ |
| Проверить количество работающих EC2 | `describe_instances()`                           |
| Проверить свободное место в S3      | `list_objects_v2()` + суммировать размеры        |
| Автоматизировать бэкап              | `upload_file()` + timestamp в имени              |
| Очистка старых файлов               | фильтрация по `LastModified` и `delete_object()` |
| Мониторинг нагрузки                 | `cloudwatch.get_metric_statistics()`             |
| Генерация отчётов                   | использовать данные `boto3` → CSV / JSON         |
| Создание пользователей CI/CD        | `iam.create_user()`, `iam.attach_user_policy()`  |

---

## 🧩 9. Пример «комплексного» DevOps-скрипта

Сценарий: остановить все EC2 в определённом регионе, сохранить логи в S3.

```python
import boto3
import datetime

region = "us-east-1"
s3_bucket = "my-devops-logs"

ec2 = boto3.client("ec2", region_name=region)
s3 = boto3.client("s3")

# Получаем список запущенных инстансов
instances = ec2.describe_instances()
running = [
    i["InstanceId"]
    for r in instances["Reservations"]
    for i in r["Instances"]
    if i["State"]["Name"] == "running"
]

# Останавливаем их
if running:
    ec2.stop_instances(InstanceIds=running)
    log = f"{datetime.datetime.now()}: stopped {running}"
    print(log)

    # Загрузка лога в S3
    s3.put_object(
        Bucket=s3_bucket,
        Key=f"logs/stop-{datetime.datetime.now().isoformat()}.txt",
        Body=log.encode("utf-8")
    )
```

---

## 🧠 Главное, что нужно запомнить

| AWS Сервис | boto3 client                 | Ключевые методы                                               |
| ---------- | ---------------------------- | ------------------------------------------------------------- |
| S3         | `boto3.client('s3')`         | `upload_file`, `download_file`, `list_objects_v2`             |
| EC2        | `boto3.client('ec2')`        | `run_instances`, `stop_instances`, `terminate_instances`      |
| ELB        | `boto3.client('elbv2')`      | `create_load_balancer`, `create_listener`, `register_targets` |
| IAM        | `boto3.client('iam')`        | `create_user`, `list_users`, `create_access_key`              |
| CloudWatch | `boto3.client('cloudwatch')` | `get_metric_statistics`, `put_metric_data`                    |

---

Хочешь, я соберу тебе следом
📘 **30 практических задач (10 простых / 10 средних / 10 продвинутых)**
по `boto3`, включая S3, EC2, ELB, IAM, CloudWatch — именно в DevOps-формате (реальные кейсы)?

