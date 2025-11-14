## Contributing to Charm

Thanks for your interest in Charm.

We’re currently building our v1 release, featuring a federated runtime and middleware layer.

See the [docs](https://github.com/CharmAIOS/Charm/tree/main/docs) to learn more about Charm.


## Getting Started

1. Fork & Clone
   ```bash
   git clone https://github.com/<yourname>/CharmOS.git
   cd CharmOS
2. Install Dependencies
   ```bash
   npm install
   pip install -r requirements.txt
3. Run Development Mode
   ```bash
   npm run dev
   python scripts/dev_runner.py

See (TBD) for detailed setup instructions.

## How to Contribute
1.	Create a new branch from main
    ```bash
    git checkout -b feat/<your-feature-name>

2.	Make your changes and commit
    ```bash
    git commit -m "feat: add transport correlation metadata support"

3.	Push and open a Pull Request
      ```bash
      git push origin feature/<your-feature-name>"
4.	Describe:
- What you changed
- Why it’s needed
- How to test it

### Development Workflow

1.	Check [contracts](https://github.com/CharmAIOS/Charm/tree/main/docs/contracts/uac) to confirm the current frozen schemas.
2.	Choose a [route](https://github.com/CharmAIOS/Charm/blob/main/docs/pipeline.md) and open an Issue using the corresponding template (For now, Charm focuses on a single reference route:
**CrewAI → LangGraph**).
3.	Use [fixtures](https://github.com/CharmAIOS/Charm/tree/main/docs/fixtures) as the golden sample to write your tests, then run npm run test:<lane>.
4.	Submit a PR — the CI will only verify your lane’s tests and ensure contracts remain intact.
5.	Before major merges, we run test:e2e across the full pipeline.

## Issues, Bugs, and Feature Requests
You can read the [contributing guidelines](https://opensource.guide/) before you begin

1. Report bugs or suggest features under Issues
2. Check existing issues
3. Follow the issue templates

## Current Development Focus
We’re currently prioritizing **Agent Portability** — building the core pipeline that makes agents portable across frameworks.

Please familiarize yourself with:
- [**Pipeline Overview**](https://github.com/CharmAIOS/Charm/blob/main/docs/pipeline.md)
- [**Fixtures**](https://github.com/CharmAIOS/Charm/tree/main/docs/fixtures): static sample agents used for validation and testing.

Contributions related to this route are highly welcome. If you want to help in one of these areas, comment under the relevant GitHub Issue or @ucmind in Discussions.

## Community Guidelines
We follow the [contributing guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines) to ensure respectful and collaborative contributions.

