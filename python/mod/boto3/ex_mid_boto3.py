Средний (автоматизация и фильтрация)

Цель: понимать, как фильтровать, обрабатывать ответы и применять DevOps-подход.

Запусти несколько EC2-инстансов (2 штуки) и выведи их публичные IP.

Фильтруй только “running” EC2 при помощи describe_instances(Filters=[...]).

Создай IAM-пользователя с именем deploy-bot.

Сгенерируй ему access key и выведи в консоль.

Назначь пользователю политику AmazonS3ReadOnlyAccess.

Создай новый S3 бакет и включи версионирование через put_bucket_versioning().

Создай CloudWatch alarm на CPU Utilization для определённого EC2.

Собери статистику CPU за последние 2 часа через get_metric_statistics().

Создай Target Group и ELB, затем выведи DNS имя балансировщика.

Привяжи EC2 к Target Group (через register_targets()).
