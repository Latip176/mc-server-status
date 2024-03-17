# mc-server-status

Rest API for fetch Status Server Minecraft Java &amp; Bedrock

# fetch data

tipe have two tipe: `java` and `bedrock`

## java

```
/api/{tipe}?ip=..
```

## bedrock
port `default` is `19132`
```
/api/{tipe}?ip=..&port=..
```

# tech

- FastAPI
- mcstatus
