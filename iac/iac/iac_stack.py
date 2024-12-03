from aws_cdk import (
    aws_ec2 as ec2,
    core as cdk,
)
from constructs import Construct

class EC2Stack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Crear una VPC (opcional, pero recomendado)
        vpc = ec2.Vpc(
            self, "MyVpc",
            max_azs=2,  # Define el número de zonas de disponibilidad
        )

        # Security Group para la instancia EC2
        security_group = ec2.SecurityGroup(
            self, "InstanceSG",
            vpc=vpc,
            security_group_name="InstanceSG",
            description="Permitir tráfico SSH, HTTP y HTTPS",
            allow_all_outbound=True,
        )

        # Permitir acceso SSH
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Permitir acceso SSH"
        )

        # Permitir acceso HTTP
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "Permitir tráfico HTTP"
        )

        # Permitir acceso HTTPS
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "Permitir tráfico HTTPS"
        )

        # Amazon Machine Image (AMI)
        ami = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        # Crear la instancia EC2
        instance = ec2.Instance(
            self, "MyInstance",
            instance_type=ec2.InstanceType("t2.micro"),  # Tipo de instancia
            machine_image=ami,
            vpc=vpc,
            security_group=security_group,
            key_name="vockey",  # Usando tu key pair "vockey"
        )

        # Agregar un nombre a la instancia (Tag opcional)
        cdk.Tags.of(instance).add("Name", "MyCDKInstance")
