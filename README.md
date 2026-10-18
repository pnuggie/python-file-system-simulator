# Python File System Simulator

## Overview
A simulated file management system built in Python. 
This project started as a simple file storage program and gradually expanded into a more realistic file explorer, featuring persistent storage, search, editing, deletion, storage limits, and file metadata.
Currently on v4 (final).

## Features

### v1: basic
- Created files with names, content, and authors
- Viewed stored files
- Searched for files
- Deleted files

### v2: authenticaion
- Added password authentication
- Added three login attempts before access is denied
- Refactored authentication into a reusable login() function
- Improved code organisation for future development

### v3: persistent file storage and file editing
- Added persistent file storage using text files
- Files can now be saved and loaded between program sessions
- Added the ability to edit existing files

### v4: simulated storage size and metadata (Final)
- Simulated storage system based on file content size
- Configurable storage limit
- Storage usage warnings when nearing capacity
- Prevents files and rewrites from being created if storage is exceeded
- Metadata that can update when a file is rewritten ('created' and 'modified')

The simulator uses a simplified storage model where each character in a file's content represents 1 byte.

e.g. hello = 5 'bytes' of storage used

The system tracks total usage and prevents files being added if they exceed the storage limit.

## Skills demonstrated
- Python programming
- Lists and dictionaries
- Functions and code organisation
- File handling and persistent storage
- User input validation
- Problem solving and debugging

## Potential future features
- Graphical user interface
- User accounts with separate files
- More advanced file organisation, including folders, tags, and favourites
- Improved storage methods
- Ability to edit more than just file content
- Order by largest/smallest sized file

## Why did I make this?
~~Because I wanted to~~ To practise Python programming while exploring how a simple file management system could be developed. The project has been expanded gradually to improve functionality, organisation, and usability.
