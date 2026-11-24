import json
import time
def mock_sagemaker_endpoint(payload):
    cibil=payload.get("cibil",0)
    salary=payload.get("salary",0)

    if cibil>=750 and salary>=50000:
        return{"status":"Approved","confidence_score":0.96}
    elif cibil>=650 and salary >=30000:
        return{"status":"Under Review","confidence_score":0.89}
    else:
        return{"status":"Rejected","confident_score":0.72}
    
# THE NOTIFICATION SERVICE (Amazon SNS Simulation)

def sns__email_dispatch(subject,message):
