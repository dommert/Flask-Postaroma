# API

### Note Model

Field Name | Field Type
------------ | -------------
rid | int, auto increment (row ID)
id | text, uuid (note id)
title | text
description | text / blob



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




