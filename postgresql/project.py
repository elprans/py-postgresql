'project information'

#: project name
name = 'py-postgresql'

#: IRI based project identity
identity = 'http://python.projects.postgresql.org/'

author = 'James William Pye <x@jwp.name>'
description = 'Driver and tools library for PostgreSQL'

# Set this to the target date when approaching a release.
date = None
tags = set(('documentation','fixes'))
version_info = (1, 0, 2)
version = '.'.join(map(str, version_info)) + (date is None and 'dev' or '')
