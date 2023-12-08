# neo4j-python-api-sample
This is a starter / sample app for a Python API using FastAPI and neomodel

## Requirements
* Python >= 3.7
* Neo4j >= 5.11

## Installation

### Neo4j

You need a running instance of Neo4j. See the [Installation guide](https://neo4j.com/docs/operations-manual/current/installation/) here for options (including AuraDB).

Then, load the dump provided in the [data](/data/spotify.dump) folder. See how to proceed here : for [Aura](https://neo4j.com/docs/aura/auradb/importing/import-database/), or for [self-managed](https://neo4j.com/docs/operations-manual/current/backup-restore/restore-dump/).

This database was created using a [Kaggle Spotify dataset](https://www.kaggle.com/datasets/thedevastator/popularity-of-spotify-top-tracks-by-genre).

### API

To install and run the API, run the following :

```cmd
pip install pipenv
pipenv install
```

In main.py, change the value of `config.DATABASE_URL` to match your database information

Finally, run :

```cmd
pipenv run dev
```

### Querying the API

Go to [http://localhost:8000](http://localhost:8000) in your web browser and you should see the number of songs in your database.

Next, you can navigate to [http://localhost:8000/artists?page_size=10&page_number=5](http://localhost:8000/artists?page_size=10&page_number=5) and you will see a list of artists and their songs. Pick a couple of song uids for the next step.

Finally, you can create your own playlist using the following command :

```cmd
curl -X POST -H "Content-Type: application/json" -d '{
  "title": "The Hives Best Of",
  "songs": ["7r68k5cbrF0GiFGSY538MW", "05pYGBaNqoIqsy5FjsnL1o"]
}' http://localhost:8000/playlists
```

You should get a similar result. Note that the API went and fetched the properties of the songs after saving the playlist to the database.

```json
{
    "uid":"2721c44d238f4de4888ddd7f7eca834e",
    "title":"The Hives Best Of",
    "songs":[
        {"uid":"05pYGBaNqoIqsy5FjsnL1o","title":"1000 Answers","popularity":0},
        {"uid":"7r68k5cbrF0GiFGSY538MW","title":"A.K.A. I-D-I-O-T","popularity":0}
    ]}
```

### Indexes and constraints

To let neomodel figure out the constraints and indexes from the model description, run the following script :

```cmd
neomodel_install_labels src/database_models.py --db=bolt://neo4j:password@localhost:7687/spotify
```

This will look at [database_models.py](/src/database_models.py) and create constraints for properties with `unique_index=True` and indexes for properties with `index=True`.


## Customization

If you want to start tuning this sample API to your existing Neo4j database, you can use the inspection script, available from neomodel version 5.2.0 :

```cmd
# This will create a file with all classes to match your db, including indexes and constraints
neomodel_inspect_database --db=bolt://neo4j:password@localhost:7687/spotify --write-to src/custom_database_models.py
```

