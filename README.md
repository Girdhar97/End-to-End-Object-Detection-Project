# End-to-end-Object-Detection-Project


## Workflows: this explains what files are to be changed first and last in order

- constants
- config_entity
- artifact_entity
- components
- pipeline         
# pipeline is a flow defining what files to run first, starting from data ingestion in components folder
- app.py




## Project Configuration

```bash
#install aws cli from the following link

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

```bash
#Configure aws crediential (secret key & access key)

aws configure
```


```bash
#Create a s3 bucket for model pusher. name is mentioned in the consrtant

```



## How to run:

```bash
conda create -n signlang python=3. -y
```

```bash
conda activate signlang
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```




