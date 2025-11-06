## Contributing to Charm

Thanks for your interest in Charm.

Our mission is to abstract away today’s fragmented AI development and execution environments — enabling agents to be built and run together through a unified interface.

By doing so, Charm aims to help AI applications evolve into a truly connected ecosystem and become a natural part of human society.

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
    git checkout -b feature/<your-feature-name>

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

### Development Workflow (TBD)
1.	Check /contracts/README.md to confirm the current frozen schemas.
2.	Choose a lane and open an Issue using the corresponding template.
3.	Use /fixtures as the golden sample to write your tests, then run npm run test:<lane>.
4.	Submit a PR — the CI will only verify your lane’s tests and ensure contracts remain intact.
5.	Once a week, during Integration Day, we run test:e2e and merge to main.

## Issues, Bugs, and Feature Requests
You can read the [ contributing guidelines](https://opensource.guide/) before you begin

1. Report bugs or suggest features under Issues
2. Check existing issues
3. Use clear titles and include:
  - Steps to reproduce
  - Expected vs. actual behavior
  - Logs or screenshots (if relevant)
## Current Focus Areas
We’re currently prioritizing:
- contracts
- adapters
- transport
- Mock fixtures and validation scripts

If you want to help in one of these areas, comment under the relevant GitHub Issue or tag @team in Discussions.

## Community Guidelines
We follow the [contributing guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines) to ensure respectful and collaborative contributions.

