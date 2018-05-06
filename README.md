# Idomoo-Python-SDK

<img src="https://blog.idomoo.com/hs-fs/hub/433650/file-2115299887-png/new_logo_in_PNG.fw.png?t=1518623729465&width=673&name=new_logo_in_PNG.fw.png" alt="drawing" style="width: 200px;"/>


Idomoo's API is designed for developers or anyone who’s comfortable creating custom-coded solutions.
The API is designed using standard HTTP (RESTful) protocols and can be implemented using a variety of programming languages and frameworks.
This is a python implementation of the above API.

- API version: 2.0
- Package version: 0.0.1-beta (This means that both the API and client are subject to changes)

You can Read the full API reference [here](https://academy.idomoo.com/support/home). (Please do!)

 - Python 2.7 and 3.4+

 - Idomoo Account and Credits.

Read below on how to get your credentials

## Finding the Account ID and API Secret Key
If you don't have an idomoo Account, you can create one at [https://pv.idomoo.com](https://pv.idomoo.com)

You can find the Account ID in the Storybuilding Suite by following these steps:

1. Make sure you are logged in to the Storybuilding Suite.
2. Click your name or account icon at the top right of the interface.
3. Find the Account ID to the right of your name, in parentheses.

You can find the API Secret Key in the Storybuilding Suite by following these steps:

1. From the top-right account menu (the one showing your registered name), click Settings.
2. Click the API Keys tab.
3. Your API Secret Key as available to copy in this page.


## Installation & Usage

### pip install


```sh
pip install git+https://github.com/Idomoo-RnD/idomoo-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

## Getting Started

### Creating the client 

#### Using The configuration object
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

2) In the code
```python
import idomoo
config = idomoo.Configuration()
config.api_secret_key = "SECRETE_KEY"
config.account_id = "ACCOUNT_ID"
config.region = "USA"
pv = idomoo.IdomooClient(configuration=config)
```
## Documentation for API Endpoints
All URIs are relative to *https://usa-api.idomoo.com/api/v2*

The API includes two main levels:

[Generate API](docs/GenerateApi.md)

[Metadata API](docs/MetadataApi.md)

## Security
- **Type**: HTTP basic authentication

You can read more about the API Authorization mechanism [here](docs/Security.md)

# Troubleshoots and Contributing
If you have any questions, bug reports, and feature requests, please [open an issue](https://github.com/Idomoo-RnD/idomoo-python-sdk/issues/new) on Github.

## Author

dev.support@idomoo.com

