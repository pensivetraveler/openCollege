# openCollege proejct - Bot

# deploy

```
heroku login
heroku git:clone -a ${appName}
git subtree push --prefix project/oc-line-bot heroku master
```

# logging

```
heroku logs --tail --app {appName} 
```
