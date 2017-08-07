# Cassiopeia Set-Up Guide

1. Install Anaconda. Type the following anywhere in your terminal.
```bash
wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh
```
2. In the same directory where you just install the script, run it (if you're not sure whether or not you're in the same directory, type ```ls -l``` and you should see a file named ```Anaconda3-4.4.0-Linux-x86_64.sh```).
```bash
bash Anaconda3-4.4.0-Linux-x86_64.sh
```
3. After the script is done running, verify that the script ran successfully. (Running the following command should output ```Pyhton 3.6.1```)
```bash
python --version
```
4. Install the python libraries cassiopeia, merakicommons, and datapipelines.
```bash
mkdir PythonLibs
cd PythonLibs
git clone https://github.com/meraki-analytics/cassiopeia.git
git clone https://github.com/meraki-analytics/merakicommons.git
git clone https://github.com/meraki-analytics/datapipelines.git
```
5. Switch over to the v3-development branch of cassioepia.
```bash
cd cassiopeia
git checkout v3-development
cd ..
```
6. Add the file paths of the 3 libraries to your ```PYTHONPATH``` environment variable.
```bash
echo "export PYTHONPATH=$PYTHONPATH:$(pwd)/cassiopeia" >> ~/.bashrc
echo "export PYTHONPATH=$PYTHONPATH:$(pwd)/merakicommons" >> ~/.bashrc
echo "export PYTHONPATH=$PYTHONPATH:$(pwd)/datapipelines" >> ~/.bashrc
```
7. Add your API key as an environment variable. You get this value from the Riot Games Developer Portal (we all did this a couple meetings back).
```bash
echo "export DEV_KEY='{insert your dev key here}'" >> ~/.bashrc
```
8. Restart your shell (you can also just close and re-open your terminal).
```bash
source ~/.bashrc
```
9. Verify that all your environment variables were entered sucessfully.
```bash
tail ~/.bashrc
```
Your output for step 9 should look something like this: