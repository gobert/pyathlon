# Pyathlon

Import triathlon results and view results on a graph. Check the demo [here](http://gobert.pythonanywhere.com)

#### Requirements
* Python 2.7
* Sqlite3

Install dependencies with:
* ```pip install -r requirements.py```

### Usage
Start server with ```python server.py```

1. Import data on [localhost:5000/import](http://localhost:5000/import)
1. View results on [localhost:5000/view](http://localhost:5000/view)

### Deployment
To deploy to pythonanywhere
1. Go to Web UI
2. Connect to bash
3. run ```bash deploy.sh ```
4. (If necessary) [upload sqlite3 DB file](https://www.pythonanywhere.com/user/gobert/files/home/gobert/mysite)
5. From [restart webserver](https://www.pythonanywhere.com/user/gobert/webapps)
