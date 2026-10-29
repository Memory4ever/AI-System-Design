---
updatedAt: 2026-08-07T14:04:06.000Z
agentTools:
  projectIndex: https://support.datacite.org/llms.txt
---

# What is the difference between the "created", "registered" and "published" date in the DataCite REST API?

The [DataCite REST API](https://support.datacite.org/docs/api) response includes the “registered”, "created" and "published" date. These are defined as follows:

**registered:** the date when the DOI was registered in the global handle server (in findable state).

**created:** the date when the new DOI record is created in the DataCite system.

> 📘
>
> These two dates can be exactly the same. However, if a DOI is created in draft state and then changed to findable at a later date, then the created and registered dates will be different

**published:** if the DOI metadata includes the dateType "issued" then this date will appear in the "published" field. If there is no dateType "issued" then the "published" date will be the publicationYear.

More information about [filtering list responses ](https://support.datacite.org/docs/api-queries#filtering-list-responses)

Please refer to the [DataCite Metadata Schema documentation](https://schema.datacite.org/) for definitions of the properties in the schema that relate to dates (e.g. dateType and publicationYear).