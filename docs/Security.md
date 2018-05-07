# Security
In order to make sure you are who you say you are Idomoo offers the following security mechanisms.

Idomoo's APIs use Basic authorization. 

Basic authorization is a very simple authorization scheme that is built into the HTTP protocol. To create the value for the authorization header follow these steps:

1. Create a string from the acount ID and API Secret Key with a colon (:) between them.
2. Take the string and base64-encode it.
3. Add the word Basic followed by a space before the encoded string.


Here is an example with some dummy data:

|  |  | 
|---|---|
|Account ID | 1111 |Asynchronous
|API Secret Key | khjGLMDSJtdd7c7687ab727b47f624dc38645523b5wsJ1lPy9g2  |  
| String to encode | 1111:khjGLMDSJtdd7c7687ab727b47f624dc38645523b5wsJ1lPy9g2 |  
| Encodes as  | 	MTExMTpraGpHTE1EU0p0ZGQ3Yzc2ODdhYjcyN2I0N2Y2MjRkYzM4NjQ1NTIzYjV3c0oxbFB5OWcy  |  
|Used as | Basic MTExMTpraGpHTE1EU0p0ZGQ3Yzc2ODdhYjcyN2I0N2Y2MjRkYzM4NjQ1NTIzYjV3c0oxbFB5OWcy|
