# ThoughtWorks Merchant's Guide Challenge


## Start the API


```bash
docker-compose up -d
```

# FRONTEND
In terminal, go to frontend dir, type and run 
```bash
npm start
```

The app will start at http://localhost:3000

## Whats the flow?
User inputs the data/query.  
The string is prepared in frontend (ReactJs) and sent to API (Python/Flask) that will return the converted value as Json.