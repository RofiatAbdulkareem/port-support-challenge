# GitHub Workflow Not Triggering

If a self-service action in Port stays “IN PROGRESS” and doesn’t trigger a GitHub workflow, here are three key checks the customer should go through.

---

## Troubleshooting Steps

1. *Can you confirm that the GitHub App is installed and authorized for the repo where the workflow is located?*  
   Without this, Port can’t trigger any workflows.

2. **Does your workflow file include workflow_dispatch at the top?**  
   Port needs this trigger to start GitHub workflows manually.

3. **Did you double-check the action configuration in Port (org, repo, workflow file name)?**  
   A mismatch in any of these fields will silently cause the action to fail or hang.