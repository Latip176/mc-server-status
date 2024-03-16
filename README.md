# mc-server-status

Rest API for fetch Status Server Minecraft Java &amp; Bedrock

# fetch data

tipe have two tipe: `java` and `bedrock`

## java

```
/api/{tipe}?ip=..
```

## bedrock

```
/api/{tipe}?ip=..&port=..
```

### info

port `default` is `19132` for Bedrock and Java is None

# tech

- FastAPI
- mcstatus
