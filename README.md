
# Idomoo-Python-SDK

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/4052681764/original/SPp1y8hUo2QDdFoYjEud7egQJv1Vu0B_Yg.png" align="center">


Idomoo's API is designed for developers or anyone who’s comfortable creating custom-coded solutions.
The API is designed using standard HTTP (RESTful) protocols and can be implemented using a variety of programming languages and frameworks.

This is a python implementation of the above API.

- API version: 2.0
- Package version: 0.0.1-beta (This means that both the API and client are subject to changes)

You can, and should, read the full API reference [here](https://academy.idomoo.com/support/solutions/folders/4000023886).
## Requirments
 - Python 2.7 and 3.4+

 - Idomoo Account and Credits.

### Finding the Account ID and API Secret Key
If you don't have an idomoo Account, you can create one on [Idomoo's Storybuilding Suite](https://pv.idomoo.com).

You can find the Account ID in the Storybuilding Suite by following these steps:

1. Make sure you are logged in to the Storybuilding Suite.
2. Click your name or account icon at the top right of the interface.
3. Find the Account ID to the right of your name, in parentheses.

You can find the API Secret Key in the Storybuilding Suite by following these steps:

1. From the top-right account menu (the one showing your registered name), click Settings.
2. Click the API Keys tab.
3. Your API Secret Key as available to copy in this page.


## Installation & Usage

Idomoo uses pip to install the SDK package. To install, type the following in the command line application of your choice:


```sh
pip install git+https://github.com/Idomoo-RnD/idomoo-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

## Getting Started

### Creating the Client by Using the Configuration Object
We allow 2 ways to initiate the basic configuration object

1) Using Env variables:

* IDOMOO_API_REGION - (USA/EUR)
* IDOMOO_ACCOUNT_ID
* IDOMOO_API_SECRET_KEY

```python
import idomoo
configuration = idomoo.Configuration()
client = idomoo.IdomooClient(configuration=configuration)
```

2) Using the code itself:
```python
import idomoo
config = idomoo.Configuration()
config.api_secret_key = "SECRETE_KEY"
config.account_id = "ACCOUNT_ID"
config.region = "USA"
client = idomoo.IdomooClient(configuration=config)
```
## Documentation for API Endpoints
All URIs are relative to *https://usa-api.idomoo.com/api/v2*

The API, and therefor SDK, include two main levels:

[Generate SDK](docs/GenerateSDK.md) - use this SDK to generate videos.

[Metadata SDK](docs/MetadataSDK.md) - user this SDK to upload scenes, get information about scene and storyboards, and get information about your account.

## Security
- **Type**: HTTP basic authentication

You can read more about the API Authorization mechanism [here](docs/Security.md)


## Troubleshoots and Contributing
If you have any questions, bug reports, and feature requests, please [open an issue](https://github.com/Idomoo-RnD/idomoo-python-sdk/issues/new) on Github.

## Author

dev.support@idomoo.com

