import os
import aws_cdk as cdk
from iac.iac_stack import EC2Stack 

app = cdk.App()

EC2Stack(
    app, "EC2Stack", 
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
        region=os.getenv('CDK_DEFAULT_REGION')
    ),
)

app.synth()
