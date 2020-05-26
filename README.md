## Automation of GS webpage with Selenium library (Python)
This automation is created for running in any environment where Python and Chrome are installed or in Docker.

### Requirements:
- Python 3.6.8 or higher
- Chrome 81.0.4044.122 or higher

### Setup:
- First, install required python packages. Run following command from folder where is this repository cloned: 
```console
python -m pip install -r requirements.txt
```
- Then just run project and watch ow outomation works. Parameter `--headless` can be used to run automation in background without visible browser running:
##### Substitute $NAME and $PASSWORD in above command with your credentials for GS webpage. 
```console
python main.py --name=$NAME --password=$PASSWORD --headless
```
- To make project available also for docker, `Dockerfile` is created. To run project in docker, follow [this tutorial](https://docs.docker.com/get-started/part2/).

##### Setting up is done in Ubuntu 18.04.
