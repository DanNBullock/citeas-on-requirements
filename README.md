# CiteAs-on-requirements

## Overview

[GitHub action](https://github.com/features/actions) for using the [CiteAs](https://citeas.org/) [API](https://citeas.org/api) to generate a software citation ACKNOWLEDGEMENTS.md document automatically from a [requirements.txt](https://learnpython.com/blog/python-requirements-file/) file.

**[See usage note below for issues relating to citation output quality](#important-usage-note)**

### Keywords

keywords: [citation](https://github.com/topics/citation), [automatic-documentation](https://github.com/topics/automatic-documentation), [automated-documentation](https://github.com/topics/automated-documentation), [github-actions](https://github.com/topics/github-actions), [citeas](https://github.com/topics/citeas)

## Usage

### Example Workflow

```yaml
name: Citation update
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: Self test
        id: generateCitation
        description: "GitHub action which builds citations from requirements.txt"
        uses: DanNBullock/citeas-on-requirements@master

        # The input requirements.txt file (as a string?)
        with:
          inputFile: "requirements.txt"
          # [0 = 'APS', 1 = 'Harvard', 2 = 'Nature', 3 = 'MLA', 4 = 'Chicago', 5 = 'Vancouver']
          formatSelect: 2
      - name: Commit changes
        uses: test-room-7/action-update-file@v1
        description: "GitHub action to commit the specific updated file"
        with:
          file-path: 'ACKNOWLEDGMENTS.md'
          commit-msg: Update ACKNOWLEDGMENTS.md
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Inputs

| Input                                             | Description                                        |Default                                        |
|------------------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| `inputFile`  | Path to the requirements.txt file    |  "requirements.txt"
| `formatSelect`  | Index to select the output format of citations : [0: 'APS', 1: 'Harvard', 2: 'Nature', 3: 'MLA', 4: 'Chicago', 5: 'Vancouver']    | 2 |

### IMPORTANT USAGE NOTE

In essence, this [GitHub action](https://github.com/features/actions) is just a wrapper around the [CiteAs](https://citeas.org/) [API](https://citeas.org/api).  While [CiteAs](https://citeas.org/) is a great resource, it is not perfect.  In particular, it currently appears to have some trouble with prompts that are based upon simply the package name (as would be the case for information coming from the requirements.txt file)--CiteAs functionality with DOIs or repository URLs seems to work more reliabily.  It is hoped that as [CiteAs develops](https://github.com/ourresearch/citeas-api/commits/master) and becomes more robust, so too will the output of this resource.

### Recomendations on obtaining a requirements.txt file

The operation of this [GitHub action](https://github.com/features/actions) is predicated upon the assumption that an accepted "manifest-type" file (e.g. `requirements.txt`, `Dockerfile`, `pyproject.toml`) is present in the repository--although currently **only** `requirements.txt` is accepted.  A `requirements.txt` file can be generated manually or, using [pipreqs](https://pypi.org/project/pipreqs/) or other such methods, automatically.  There is even an existing GitHub action for automatically generating a `requirements.txt`, [pipreqs-action](https://github.com/marketplace/actions/automatic-requirements-txt-for-python-projects), which can do this as well.  However, it's worth noting that for this GitHub action implementation, the versioning information that is transcribed to the output `requirements.txt` _is not_ coming from your local environment / setup.  In any case, for the purposes of this GitHub action (and citation more generally), having a poorly versioned `requirements.txt` is better than not having one at all.

## Project / Codebase overview

- src: contains the main codebase (duplicated in main.py, an admittedly bad practice; should be treated as a module)
- test: contains various test requirement.txt-like documents

## Project / codebase provenance

### Rationale

This project is hoped to help adress an apparent gap in the open-source and scientific-software landscape.  Namely, the lack of an automated method for generating software citations within and/or for scientific software packages.  The consequences of this shortcoming have been discussed at length elsewhere (see [Citations](#publications) for some of these publications).  With the provison of this capability (or at least this proof of concept), it is hoped that the hurdles to the production of software bibliographies--which would otherwise have to be produced manually--are reduced.

### Support elements

#### Authors

- [Daniel Bullock](https://github.com/DanNBullock) (iisdanbul@gmail.com)

#### Contributors

[Be the first!]

### Development elements

#### License

Apache License 2.0

#### Support

[todo]

#### Contributing

Contributions are welcome and encouraged, particularly in the following areas:

- Capability enhancment (e.g. items from roadmap below)
- Code streamlining & improvement (the initial implementation of this code is likely inelegant and inefficient)
- General bug / error reports (via the [issues page](https://github.com/DanNBullock/citeas-on-requirements/issues))
- Questions / suggestions / comments (also via the [issues page](https://github.com/DanNBullock/citeas-on-requirements/issues))

#### Roadmap

Here are some capabilites that are hoped to be added soon:
- Methods for alternative software manfifest formats (e.g. [Dockerfiles](https://github.com/DanNBullock/citeas-on-requirements/issues/3) and [pyproject-toml](https://github.com/DanNBullock/citeas-on-requirements/issues/2))
- Methods for automatedly finding software manifest files (rather than relying on _inputFile_ yml variable input or assumptions)
- Methods for handling and combining outputs from multiple software manifest files in the same repository (e.g. Dockerfile + requirements.txt)
- Boilerplate text to serve as the header for the default ACKNOWLEDGEMENTS.md document output.

#### Citations

##### Software

(Ironically, made via zbib.org)
- Piwowar, H., Priem, J., Howison, J., & Meyer, C. (2021). Citeas [Python]. OurResearch. https://github.com/ourresearch/citeas-api

##### Publications

- Du, C., Cohoon, J., Priem, J., Piwowar, H., Meyer, C., & Howison, J. (2021, October). CiteAs: Better Software through Sociotechnical Change for Better Software Citation. In Companion Publication of the 2021 Conference on Computer Supported Cooperative Work and Social Computing (pp. 218-221).

- Stephan Druskat, Jurriaan H. Spaaks, Neil Chue Hong, Robert Haines, and James Baker. 2021. Citation File Format (CFF) - Specifications. (2021).

- James Howison and Julia Bullard. 2016. Software in the scientific literature: Problems with seeing, finding, and using software mentioned in the biology literature. Journal of the Association for Information Science and Technology 67, 9(2016), 2137–2155. https://doi.org/10.1002/asi.23538

- James Howison and James D. Herbsleb. 2011. Scientific software production: incentives and collaboration. In Proceedings of the ACM 2011 conference on Computer supported cooperative work - CSCW ’11 (Hangzhou, China). ACM Press, 513. https://doi.org/10.1145/1958824.1958904

- Daniel S. Katz, Daina Bouquin, Neil P. Chue Hong, Jessica Hausman, Catherine Jones, Daniel Chivvis, Tim Clark, Mercè Crosas, Stephan Druskat, Martin Fenner, Tom Gillespie, Alejandra Gonzalez-Beltran, Morane Gruenpeter, Ted Habermann, Robert Haines, Melissa Harrison, Edwin Henneken, Lorraine Hwang, Matthew B. Jones, Alastair A. Kelly, David N. Kennedy, Katrin Leinweber, Fernando Rios, Carly B. Robinson, Ilian Todorov, Mingfang Wu, and Qian Zhang. 2019. Software Citation Implementation Challenges. (2019). arxiv:1905.08674http://arxiv.org/abs/1905.08674

- Erik H. Trainer, Chalalai Chaihirunkarn, Arun Kalyanasundaram, and James D. Herbsleb. 2015. From Personal Tool to Community Resource: What’s the Extra Work and Who Will Do It?. In Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social Computing(CSCW ’15). ACM, New York, NY, USA, 417–430. https://doi.org/10.1145/2675133.2675172

- Barker, M., Chue Hong, N. P., Katz, D. S., Lamprecht, A. L., Martinez-Ortiz, C., Psomopoulos, F., Harrow, J., Castro, L. J., Gruenpeter, M., Martinez, P. A., and Honeyman, T. (2022). Introducing the FAIR Principles for research software. Scientific Data, 9(1), 1-6.

- Smith, A. M., Katz, D. S., & Niemeyer, K. E. (2016). Software citation principles. PeerJ Computer Science, 2, e86.

- Barker, M., Hong, N. P. C., Katz, D. S., Leggott, M., Treloar, A., van Eijnatten, J., & Aragon, S. (2021). Research software is essential for research data, so how should governments respond?.

- Jay, C., Haines, R., & Katz, D. S. (2020). Software must be recognised as an important output of scholarly research. arXiv preprint arXiv:2011.07571.
