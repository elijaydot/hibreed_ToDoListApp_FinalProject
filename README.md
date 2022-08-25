# Hibreed_ToDoListApp_FinalProject

This is a Flask Project for an Activity Management Application(To-do list), as a final project for the Python Programming class with [Hibreed.io](https://www.hibreed.io/)

## Key Features
The users of the Activity Management Application should be able to
* Create an activity & save the item into database
* Retrieve/display activities to frontend
* Delete activity
* Update activity

### Functionalities
* The activity should have: date created, activity, when activity should be done, the duration of the activity, person to do the activity and comment.
* The date created should not be editable
* Bonus: the user should be able to mark an item as done(not compulsary)

---

## Setup the Environment (Windows OS)

* Create a virtualenv with Python 3.10 and activate it.  
```bash
python3 -m pip install --user virtualenv
# You should have Python 3.10 available in your host. 
# Create a virtual environment 
# Use a command similar to this one:
python3 -m virtualenv todolistapp
todolistapp/scripts/activate.ps1
```
* Run `pip install -r requirements.txt` to install the necessary dependencies

### Running `run.py`

* ensure to be in the right path on the terminal, then run  `python run.py`
* This would run and start the server at http://127.0.0.1:5000
* open this url in a browser

## Here is a sample look of the project
![msrdc_kE1ALywhAc](https://user-images.githubusercontent.com/5082075/186767101-2f3d7ae1-a358-4b04-9295-5465021c8d8f.png)


PS: please do note that this implementation is for development purpose.
To deploy to a live server, you have to disable debugging and any sensitive data.
You can find more details here [Deploying to Production](https://flask.palletsprojects.com/en/2.2.x/deploying/).
