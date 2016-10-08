- workon test-tmp

- √ read [Object Relational Tutorial](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html)
- IN PROGRESS read the FAQs:
    - √ [Connections, Engines](http://docs.sqlalchemy.org/en/latest/faq/connections.html)
        - √ read [Configuring Logging](http://docs.sqlalchemy.org/en/latest/core/engines.html#dbengine-logging)
        - √ read [Engine Configuration](http://docs.sqlalchemy.org/en/latest/core/engines.html)
        - √ read [Connection Pooling](http://docs.sqlalchemy.org/en/latest/core/pooling.html)
        - read [MySQL](http://docs.sqlalchemy.org/en/latest/dialects/mysql.html)
    - [MetaData / Schema](http://docs.sqlalchemy.org/en/latest/faq/metadata_schema.html)
    - [SQL Expressions](http://docs.sqlalchemy.org/en/latest/faq/sqlexpressions.html)
    - [ORM Configuration](http://docs.sqlalchemy.org/en/latest/faq/ormconfiguration.html)
    - [Performance](http://docs.sqlalchemy.org/en/latest/faq/performance.html)
    - [Sessions / Queries](http://docs.sqlalchemy.org/en/latest/faq/sessions.html)
- read [Quickie Intro to Object States](http://docs.sqlalchemy.org/en/latest/orm/session_state_management.html#session-object-states)
- read [Basic relationship patterns](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#relationship-patterns)
- read [customizing collection access](http://docs.sqlalchemy.org/en/latest/orm/collections.html#custom-collections)
- read [SQL Expression Language Tutorial](http://docs.sqlalchemy.org/en/latest/core/tutorial.html)
- read [the Zen of Eager Loading](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html#zen-of-eager-loading)
- read [Relationship Loading Techniques](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html)

- what is the difference between filter() and filter_by()?
    - [filter_by()](http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.filter_by): uses keyword arguments
    - [filter()](http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.filter):
        - uses SQL expressions, comma separated implicitly `_and()`ed together
        > The criterion is any SQL expression object applicable to the WHERE clause of a select. String expressions are coerced into SQL expression constructs via the text() construct.

