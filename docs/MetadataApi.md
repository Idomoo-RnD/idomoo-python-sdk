# Metadata SDK

Using this SDK you can enquire about scenes, storyboards, and your account. You can also upload scenes, create scene libraries and more.

## Account
|Function |Operation | Description|
|---|---|---|
| [get_account()](#get-account) | GET /accounts/	|Get Account Information|

#### Get Account
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    account = client.accounts.get_account()
except idomoo.ApiException as e:
    pass #Handle exception
    

```

## Scenes

|Function |Operation | Description|
|---|---|---|
| [get_scene()](#get-scene) | GET /scenes/{sceneId} | Get Scene by ID|
| [get_scenes()](#get-scenes) | GET /scenes/ |	List of Scenes|
| [upload_scene()](#upload-scene) | PUT /scenes/{sceneId} | Replace Scene |
| [replace_scene()](#replace-scene)| POST /scenes/ |	Upload New Scene|

#### Get Scene
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    scene = client.scenes.get_scene("SCENE_ID")
except idomoo.ApiException as e:
    pass #Handle exception

```
#### Get Scenes
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    scenes_list = client.scenes.get_scenes()
except idomoo.ApiException as e:
    pass #Handle exception

```
#### Upload Scene
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    scene_ref = client.scenes.upload_scene(library="LIBRARY_ID",idmfile="IDM_FILE_PATH")
except idomoo.ApiException as e:
   pass #Handle exception

```
#### Replace Scene
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    scene_ref = client.scenes.replace_scene(scene_id="SCENE_ID",idmfile="IDM_FILE_PATH")
except idomoo.ApiException as e:
    pass #Handle exception

```

## Libraries
|Function |Operation | Description|
|---|---|---|
| [create_scene_library()](#create-library) |POST /libraries/	|Create Scene Library|
| [get_scene_library()](#get-library) |GET /libraries/{libId}	|Return Specific Scene Library|
| [get_scene_libraries()](#get-libraries) |GET /libraries/	|List Scene Libraries|
| [get_scenes_from_library()](#get-scenes-from-library) |GET /libraries/{libId}/scenes/	|Return Scenes from Library|

#### Create Library

```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    library = client.libraries.create_scene_library({
        "name":"Library Name",
        "description":"Library description"
        })
except idomoo.ApiException as e:
    pass #Handle exception

```

#### Get Library
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    library = client.libraries.get_scene_library(lib_id="LIBRARY_ID")
except idomoo.ApiException as e:
    pass #Handle exception

```
#### Get Libraries
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    libraries_list = client.libraries.get_scene_libraries()
except idomoo.ApiException as e:
    pass #Handle exception

```
#### Get Scenes From Library
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    scenes_list = client.libraries.get_scenes_from_library(lib_id="LIBRARY_ID")
except idomoo.ApiException as e:
    pass #Handle exception

```

## Storyboard
|Function |Operation | Description|
|---|---|---|
| [get_storyboard()](#get-storyboard) | GET /storyboards/{storyboradId} | Get Storyboard by ID|
| [get_storyboards()](#get-storyboards) | GET /storyboards/ | List Of Storyboards|
 
 #### Get Storyboard
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    storyboard = client.storyboards.get_storyboard(storyborad_id="STORYBOARD_ID")
except idomoo.ApiException as e:
    pass #Handle exception

```
#### Get Storyboards
```python

import idomoo

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
try:
    storyboards_list = client.storyboards.get_storyboards()
except idomoo.ApiException as e:
    pass #Handle exception

```
