Votação
=======

Web Service de votação usado no Workshop Amazon AWS ( Python/Django com Redis NoSQL )

    $curl -l http://mydomain.com:8000/ws/votar/a/
    $true
    
    $curl -l http://mydomain.com:8000/ws/votar/a/
    $true
    
    $curl -l http://mydomain.com:8000/ws/votar/a/
    $true

    $curl -l http://mydomain.com:8000/ws/votar/b/
    $true

    $curl -l http://mydomain.com:8000/ws/resutado/
    {
        "A": 3, 
        "B": 1
    }

    * http://www.solidit.com.br *



### Consultar as imagens disponiveis

    $ ec2-describe-images -o self --region sa-east-1

### Consultar as configuracoes existentes

    $ as-describe-launch-configs --region sa-east-1
    $ as-delete-launch-config votacaolc --region sa-east-1
    $ as-create-launch-config votacaolc --image-id ami-cf0daad2 --instance-type m1.large --key workshop --group workshop --region sa-east-1

### Configurar os autoscalings groups

    $ as-describe-auto-scaling-groups --region sa-east-1
    $ as-delete-auto-scaling-group votacaogroup --force-delete --region sa-east-1
    $ as-create-auto-scaling-group votacaogroup --availability-zones sa-east-1a --launch-configuration votacaolc --load-balancers votacao --max-size 10 --min-size 1 --region sa-east-1
    $ as-create-or-update-tags votacaogroup --tag "id=votacaogroup, t=auto-scaling-group, k=Name, v=WS-Votacao, p=true" --region sa-east-1

### Criando politicas de UpScale

    $ as-put-scaling-policy votacaoUpPolicy --auto-scaling-group votacaogroup --adjustment=2 --type ChangeInCapacity --cooldown 300 --region sa-east-1

### Criando politicas de DownScale

    $ as-put-scaling-policy votacaoDownPolicy --auto-scaling-group votacaogroup --adjustment=-1 --type ChangeInCapacity --cooldown 300 --region sa-east-1

### Consultando as atividades do AutoScaling

    $ as-describe-scaling-activities --region sa-east-1

### Consultando as instancias configuradas.

    $ as-describe-auto-scaling-instances --region sa-east-1