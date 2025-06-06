# Port Support Engineer Challenge – Exercise #3

Link Jira issues to GitHub repositories in Port using Jira components.

---

## What I Did

1. **Connected GitHub to Port**
   - Installed Port GitHub app
   - GitHub repositories synced automatically as `service` blueprints

2. **Created Jira Project**
   - Used company-managed Scrum template
   - Created Jira components matching GitHub repository names

3. **Connected Jira to Port**
   - Added Jira data source in Port
   - Configured credentials and synced Jira issues

4. **Updated Data Model**
   - Added relation field `related_services` of type Relation on the `jira_issue` blueprint
   - Relation points to the `service` blueprint created by GitHub integration

5. **Mapping YAML**

```yaml
resources:
  - kind: issue
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .key
          title: .fields.summary
          blueprint: "jira_issue"
          relations:
            related_services: .fields.components[].name
```