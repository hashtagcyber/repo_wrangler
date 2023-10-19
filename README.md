# repo_wrangler
Manage Github Organization settings via PR

### Summary
Repo Wrangler is a Github Action/Docker container that allows you to manage: 
- [ ] Actions Settings
    - [ ] Organization Action Setting
    - [ ] Allowed Actions List
- [ ] Repository Rulesets
    - [ ] Require Pull Requests for main branch
    - [ ] Require PR Approvals for main branch
    - [ ] Require Status Checks to pass before merging \(Workflows/Actions)
    - [ ] Other Branch Protection Rules

### Why This?
Github Safe Settings is reccomended as part of Github's documentation, but it's a bit too complex for my needs, and I'd prefer to do simple API calls when a PR is approved. Additionally, events like the [CodeCov breach](https://about.codecov.io/security-update/) in 2021 have made me wary of inviting 3rd Parties into our CI/CD pipeline. 

### How Does It Work?
1. Fork this repo into your organization
2. Create a new Github App and grant it `Administration: Read and Write` access
3. Generate a new client secret for the app and store it as a `GHAPP_CLIENT_SECRET` in your repository secrets 
4. Grant AppDev teams the ability to create PRs against your new repo
4. When a PR is merged, the `UpdateOrgSettings` workflow will run.