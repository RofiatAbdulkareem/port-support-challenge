# Exercise #5 – Port Scorecard for Open PRs

## Objective
Implement a scorecard on the Service blueprint that tracks the number of *open GitHub Pull Requests (PRs)* per repository, with the following logic:
- *Gold*: Less than 5 PRs
- *Silver*: Less than 10 PRs
- *Bronze*: Less than 15 PRs

---

## 🛠 Steps Taken

1. *Added Property to Service Blueprint*
   - Property Name: open_prs
   - Type: Number
   - Description: Tracks the number of open PRs per GitHub repository.

2. *Created Scorecard Rules in Port*
   - Created a new scorecard titled *Open PRs Scorecard*.
   - Rules defined as:
     - Gold: open_prs < 5
     - Silver: open_prs < 10
     - Bronze: open_prs < 15

3. *Connected GitHub Pull Request Data*
   - Used Port’s GitHub integration to import the open_prs values.
   - Mapped the PR count to each related service (repository).

---

## Outcome
- Services are now scored based on the number of their open PRs.
- Each service in the *Catalog > Services* view displays a scorecard badge (Gold, Silver, or Bronze).
- This provides a quick health overview of code review activity per service.
