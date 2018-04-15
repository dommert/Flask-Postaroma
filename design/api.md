# API

### Note Model

Field Name | Field Type
------------ | -------------
rid | int, auto increment, unique, required (row ID)
id | text, uuid, unique, key, required (note id)
owner | text, userID
created | datetime
title | text, required
description | text / blob
content | blob, required
textData | text
jsonData | blob
updated | datetime
deleted | bool




### Create
newNote(id,noteData)
- id
- title
- description
- content

### Read
viewNote(id)

### Update
updateNote(id, noteData)

### Delete [soft]
deleteNote(id)



# Routes

### /note/[id]
Get, Post-Update, Delete

### /note
Post

