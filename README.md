# End-to-End-atmospheric-cloud-image-classification

git clone project

python -m venv folder_name

cd myenv\scripts\activate.bat

1. Create template.py to create files and folders.

2. Update required installations
   
3. Create setup.py file to pack our project as a local module like numpy, pandas.
   ```bash
   pip install -r requirements.txt
   python setup.py

4. create demo1.py to check demos

5. Logger function to take logs. Also add exception and utils module
   Inside src/cnnClassifier/__init__.py, write the log function.

7. Inside demo1.py, write:

   ```python
   from cnnClassifier import logger
   logger.info("welcome")


8. create common.py inside utils folder to build defined modules to call in our project

Data preparation: upload dataset in google drive or s3 bucket.      
Data download to local system: method in research/trials.ipynb folder      
zipFile gets added in research folder (delete it later)     

#Workflows for data preparation 
Update config.yaml >>> Update secrets.yaml [Optional] >>> Update params.yaml >>> Update the entity >>> Update the configuration manager in src config >>>
Update the components  >>> Update the pipeline


8. Update config.yaml in config folder      
       inside config/config.yaml update artifacts to do data ingestion through src/cnnClassifier/config/configuration.py

9.  Update secrets.yaml [Optional]

10. Update params.yaml
        
11. Update src/cnnClassifier/constants/__init__.py
        contains constant values used throughout the project

11. Update the entity inside src/entity folder
       retrieving constants from constants folder to build files and folders

12. Update the configuration manager in src/config
       to do data ingestion

13. Update the components folder in src/cnnClassifier/components
       create data ingestion.py to do data downloading and extraction

14. Update the pipeline
       inside pipeline folder add pipeline modules data ingestion

       Create demo2.py to check how project is working        
       delete zip files before committing

#workflows for transfer learning
Update config.yaml >>> Update secrets.yaml [Optional] >>> Update params.yaml >>> Update the entity >>> Update the configuration manager in src config >>>
Update the components  >>> Update the pipeline

15. Update config.yaml in config folder      
       inside config/config.yaml update artifacts to do base model preparation through src/cnnClassifier/config/configuration.py

15. update params.yaml to our requirements w.r.t transfer learning parameters

16. Update the entity inside src/entity folder
       retieving constants from constants folder to do transfer learning

17. Update the configuration manager in src/config
       to get config for our base model creation

18. Update the components folder in src/cnnClassifier/components
       to prepare base model from prepare_base_model.py

19. Update the pipeline
       inside pipeline folder add pipeline modules like prepare base model
       
       delete artifacts folder
       in terminal: set TF_ENABLE_ONEDNN_OPTS=0
       Create demo3.py to check how project is working        
       delete zip files before committing

#workflows for model training
Update config.yaml >>> Update secrets.yaml [Optional] >>> Update params.yaml >>> Update the entity >>> Update the configuration manager in src config >>>
Update the components  >>> Update the pipeline

20. Update config.yaml in config folder      
       inside config/config.yaml update artifacts to do model training through src/cnnClassifier/config/configuration.py from updated_base_model
      
21. update params.yaml to our requirements w.r.t model training parameters like epochs

22. Update the entity inside src/entity folder
       retieving constants from constants folder to do model training

23. Update the configuration manager in src/config
       to get config for our model training

       change file name in src/cnnClassifier/config/configuration.py w.r.t unzipped data folder name

24. Update the components folder in src/cnnClassifier/components
       to do model training from model_trainer.py

25. Update the pipeline
       inside pipeline folder add pipeline modules model trainer
       
       delete artifacts folder
       in terminal: set TF_ENABLE_ONEDNN_OPTS=0
    
       Demo-Image-Classification\myenv\Lib\site-packages\keras\src\optimizers\base_optimizer.py
       go inside to line 210 and hash function def _check_variables_are_known(self, variables):
       also go to lines 305 - 310 to hash it (optional if didnt work)
    
       Create demo4.py to check how project is working        
       delete zip files before committing

#workflows for model evaluation

login aws in local IDE

```bash
aws configure
```

setup an s3 bucket for model storage s3://mlflow-cloud-classification

build ec2 virtual machine

set up ubuntu machine
setup key-value pair and select ssh,http,https and run instance

connect the instance

run the following commands on ec2 machine

```bash
sudo apt update

sudo apt install python3-pip

sudo pip3 install pipenv

sudo pip3 install virtualenv

mkdir mlflow

cd mlflow

pipenv install mlflow

pipenv install awscli

pipenv install boto3

pipenv shell


## Then set aws credentials
aws configure


#Finally 
mlflow server -h 0.0.0.0 --default-artifact-root s3://mlflow-cloud-classification

#inside instances go to security>>security groups>>inbound rules>>customtcp>>5000>>0.0.0.0>>save changes
again inside instances go for public IPv4 DNS and copy it

#open Public IPv4 DNS to the port 5000
ec2-54-147-36-34.compute-1.amazonaws.com:5000

login with dagshub and connect our repository to dagshub
then click on remote(green color button)>>experiments>>copy mlflow tracking >>> click mlflow UI

MLFLOW_TRACKING_URI=https://dagshub.com/leansesection/Cloud-Image-Classifier.mlflow \
MLFLOW_TRACKING_USERNAME=leansesection \
MLFLOW_TRACKING_PASSWORD=a4776519c84f46332fa634b6310babd5d4d994bb \
python script.py

edit this in below format and run in gitbash terminal 

```bash

set MLFLOW_TRACKING_URI=http://ec2-34-227-74-65.compute-1.amazonaws.com:5000/ (edit accordingly)

set MLFLOW_TRACKING_USERNAME=leansesection

set MLFLOW_TRACKING_PASSWORD=a4776519c84f46332fa634b6310babd5d4d994bb

```
```
#set uri in your local terminal and in your code 
set MLFLOW_TRACKING_URI=http://ec2-54-147-36-34.compute-1.amazonaws.com:5000/
```


Update config.yaml >>> Update secrets.yaml [Optional] >>> Update params.yaml >>> Update the entity >>> Update the configuration manager in src config >>>
Update the components  >>> Update the pipeline

26. Update the entity inside src/entity folder
       retieving constants from constants folder to do transfer learning

27. Update the configuration manager in src/config
       to get config for our model training

    Also change the mlflow_uri in configuration.py
   

29. update components folder

30. Update the pipeline

     inside pipeline folder add pipeline modules model evaluation

     if not willing to connect to mlflow hash line 20 in stage4 pipeline

32. create demo5.py to check how model is working

30. Update the main.py by pasting demo5.py
    
    use main.py to run mlflow pipeline

32. Build prediction.py in pipeline folder

33. build app.py file
    add template

```bash
python app.py
```
   
32. Update the dvc.yaml

dvc is to stop doing same download and running same file again and again
dont forget to hash # evaluation.log_into_mlflow() in pipeline stage 04

```bash
dvc init  
dvc repro
```

