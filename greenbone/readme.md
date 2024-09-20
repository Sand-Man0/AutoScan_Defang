#1 pull and run docker file

2# get cli access into gvmd

as root
``` chmod -R 777 / ```
``` apt update && apt install -y procps ```
now list all proccesses and kill running processes related to gvmd 
``` ps -u gvmd```
```
kill pid
example : kill 31
```

install nano for editing
```apt install nano```

now cli access into gvmd
as gvmd

```nano /usr/local/bin/start-gvmd```

and edit this line :
  ``` [ -z "$GVMD_ARGS" ] && GVMD_ARGS="" ```
  and make it:
  ``` [ -z "$GVMD_ARGS" ] && GVMD_ARGS="--port=9390 --listen=0.0.0.0" ```

  now run 
    ``` /bin/sh /usr/local/bin/start-gvmd ```
    Everything should work
