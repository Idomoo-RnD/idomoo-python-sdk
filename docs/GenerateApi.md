# Generate API:
Allowing to generate a video by using either a pre-made storyboard or by editing scenes together on-the-fly. Choosing to create a storyboard using Storybuilding Suite means you only need the data itself, as the storyboard already includes the artistic and logical decisions for the video. With scenes, you, the developer, is handling the scene selection logic, as well as, the data and other artistic decisions.
The are 2 ways to generate video in idomoo's platform.

1. Generate a storyboard object

```python
import idomoo
from idomoo import StoryboardData, StoryboardAPIRequest, helpers

# Create Idomoo PVaaS Client instance
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)

# Define The Desired Output Format


# Populate the request data in a StoryBoard Request Object
name = 'My Name'
bday = '00/00/1991'
sb_request = StoryboardAPIRequest(storyboard_id='1234')
sb_request.data.append(StoryboardData(key='name', val=name))
sb_request.data.append(StoryboardData(key='bday', val=bday))
sb_request.output = helpers.MP4()

# Generate the Video
client.storyboards.generate(sb_request)
```

2. Generate a collection of scenes
```python
import idomoo
from idomoo import IdomooClient, Timeline, Scene, Media, TextProperties, SceneAPIRequest, helpers, Text

configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
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
client.scenes.generate(scene_request)

```

# Concurrency
The concurrency allowed for API calls is 10 per minute.
If more is needed, please contact support: support@idomoo.com.



# Asynchronous API
Idomoo's API is asynchronous.
When you send an API call you get a near instantaneous response.

The successful response includes the link to the video, image, or landing page.
The video has not yet been generated. Instead, the request has been added to a queue and is processed when it reaches the top of the queue.

To check if your video is ready, you can use a URL that will update you with the progress. Find the URL under the "check_status_url" property in the response.

When you check the URL you are presented with a status update similar to this:

```json
{
  "status": "VIDEO_AVAILABLE",
  "id": "1281/0000/583g401zlu1gk730q142732a31o22i672n3z24q"
}
```

**The status updates with the following options:**

| Status | Description |
|---|---|
| IN_PROCESS  | The API request arrived and is being processed.|
| IN_QUEUE | The video is waiting to be rendered. |
| RENDERING	 | The video is being rendered at the moment |
| VIDEO_AVAILABLE | The process is finished and the video is ready. |
| ERROR | Something went wrong, with descriptions, as per a regular API call. |
|NOT_EXIST | The ID does not exist. |