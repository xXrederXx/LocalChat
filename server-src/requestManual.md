## SENDING MESSAGE

```json
{
    "type":"msg",
    "msg":"<message>",
    "sender": {
      "name": "<name>"
    }
}
```

## SENDING COMMAND

cmd name > setname, active

```json
{
    "type":"cmd",
    "cmd":"<cmd name>",
    "args": ["<arg1>", "<argN>"],
    "sender": {
      "name": "<name>"
    }
}
```

## RECEIVING