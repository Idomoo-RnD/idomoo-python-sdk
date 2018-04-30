# Idomoo-Python-SDK
- API version: 2.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### pip install


```sh
pip install git+https://github.com/Idomoo-RnD/idomoo-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import idomoo 
```

## Getting Started


```python
from idomoo import IdomooClient, StoryboardData, StoryboardAPIRequest, helpers

# Create Idomoo PVaaS Client instance
pv = IdomooClient(region='usa', account_id='ACCOUNT_ID',
                  api_secret_key='API_SECRET_KEY')

# Define The Desired Output Format
name = 'My Name'
bday = '00/00/1991'

# Create a StoryBoard Request Object
sb_request = StoryboardAPIRequest(storyboard_id='1234')
sb_request.data.append(StoryboardData(key='name', val=name))
sb_request.data.append(StoryboardData(key='bday', val=bday))
sb_request.output = helpers.MP4()

# Generate the Video
pv.storyboards.generate(sb_request)
```


```python
from idomoo import IdomooClient, Timeline, Scene, Media, TextProperties, SceneAPIRequest, helpers, Text

pv = IdomooClient(region='usa', account_id='ACCOUNT_ID',
                  api_secret_key='API_SECRET_KEY')
timeline = Timeline()

scene = Scene(scene_id=1234)

image = Media(key='image', val='https://mypic.png', alignment_scale='fit')
scene.media.append(image)

txt_ph = Text(key='text1')

txt_props1 = TextProperties(text='Hello')
txt_props1.color = "rgb(1,1,255)"
txt_ph.val.append(txt_props1)

txt_props2 = TextProperties(text='My Name')
txt_props2.color = "rgb(255,128,56)"
txt_props2.font_path = 'https://myfonts.com/ariel.ttf'
txt_ph.val.append(txt_props2)
scene.text.append(txt_ph)

timeline.scenes.append(scene)

scene_request = SceneAPIRequest(timeline=timeline, output=helpers.MP4())
pv.scenes.generate(scene_request)

```


## Documentation for API Endpoints

All URIs are relative to *https://usa-api.idomoo.com/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**get_account**](docs/AccountApi.md#get_account) | **GET** /accounts/ | Get Account Informaion
*LibraryApi* | [**create_scene_library**](docs/LibraryApi.md#create_scene_library) | **POST** /libraries/ | Create Scene Library
*LibraryApi* | [**get_scene_libraries**](docs/LibraryApi.md#get_scene_libraries) | **GET** /libraries/ | List Scene Libraries
*LibraryApi* | [**get_scene_library**](docs/LibraryApi.md#get_scene_library) | **GET** /libraries/{libId} | Return Specific Scene Library
*LibraryApi* | [**get_scenes_from_library**](docs/LibraryApi.md#get_scenes_from_library) | **GET** /libraries/{libId}/scenes/ | Return Scenes from Library
*SceneApi* | [**generate_scenes**](docs/SceneApi.md#generate_scenes) | **POST** /scenes/generate/ | Generate Video from Scenes
*SceneApi* | [**get_scene**](docs/SceneApi.md#get_scene) | **GET** /scenes/{sceneId} | Get Scene by ID
*SceneApi* | [**get_scenes**](docs/SceneApi.md#get_scenes) | **GET** /scenes/ | List of Scenes
*SceneApi* | [**replace_scene**](docs/SceneApi.md#replace_scene) | **PUT** /scenes/{sceneId} | Replace Scene
*SceneApi* | [**upload_scene**](docs/SceneApi.md#upload_scene) | **POST** /scenes/ | Upload New Scene
*StoryboardApi* | [**generate_storyboard**](docs/StoryboardApi.md#generate_storyboard) | **POST** /storyboards/generate/ | Generate Video From Storyboard
*StoryboardApi* | [**get_storyboard**](docs/StoryboardApi.md#get_storyboard) | **GET** /storyboards/{storyboradId} | Get Storyboard by ID
*StoryboardApi* | [**get_storyboards**](docs/StoryboardApi.md#get_storyboards) | **GET** /storyboards/ | List Of Storyboards


## Documentation For Authorization


## Basic authentication

- **Type**: HTTP basic authentication


## Author

dev.support@idomoo.com

