# CiteAs-on-requirements

## Overview description

GitHub action for using the [CiteAs](https://citeas.org/) [API](https://citeas.org/api) to generate a software citation ACKNOWLEDGEMENTS.md document automatically from a requirements.txt file.

### Keywords

keywords: ctation, automatic-documentation, automated-documentation, github-actions, citeas

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

        uses: DanNBullock/citeas-on-requirements@master

        # Path to requirements.txt file
        with:
          inputFile: "requirements.txt"
      - name: Commit changes
        uses: test-room-7/action-update-file@v1
        with:
          file-path: 'ACKNOWLEDGMENTS.md'
          commit-msg: Update ACKNOWLEDGMENTS.md
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Inputs

| Input                                             | Description                                        |Default                                        |
|------------------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| `inputFile`  | Path to the requirements.txt file    |  "requirements.txt"
| `citaionMethod`  | Index to select the output format of citations : ['APS','Harvard','Nature','MLA','Chicago','Vancouver']    | [not yet implemented] |

### IMPORTANT USAGE NOTE

In essence, this GitHub action is just a wrapper around the [CiteAs](https://citeas.org/) [API](https://citeas.org/api).  While [CiteAs](https://citeas.org/) is a great resource, it is not perfect.  In particular, it currently appears to have some trouble with prompts that are based upon simply the package name (as would be the case for information coming from the requirements.txt file)--CiteAs functionality with DOIs or repository URLs seems to work more reliabily.  It is hoped that as CiteAs develops and becomes more robust, so too will the output of this resource.


## Project / Codebase overview

- src: contains the main codebase (duplicated in main.py, an admittedly bad practice; should be treated as a module)
- test: contains various test requirement.txt-like documents

## Project / codebase provenance

### Rationale

This project is hoped to help adress an apparent gap in the open-source and scientific-software landscape.  Namely, the lack of an automated method for generating software citations within and/or for scientific software packages.  The consequences of this shortcoming have been discussed at length elsewhere [citations].  With the provison of this capability, it is hoped that the hurdles to the production of software bibliographies (which would otherwise have to be produced manually) are reduced.

### Support elements

#### Authors

- [Daniel Bullock](https://github.com/DanNBullock) (iisdanbul@gmail.com)

#### Contributors

[Be the first!]

#### Funding sources

[todo]

#### References

[todo]

### Development elements

#### License

[todo]

#### Changelog

[todo]

#### Support

[todo]

#### Contributing

Contributions are welcome and encouraged, particularly in the following areas:

- Capability enhancment (e.g. items from roadmap below)
- Code streamlining & improvement (the initial implementation of this code is likely inelegant and inefficient)
- General bug / error reports (via the issues page)
- Questions / suggestions / comments (also via the issues page)

#### Roadmap

Here are some capabilites that are hoped to be added soon:
- Methods for alternative software manfifest formats (e.g. [Dockerfiles](https://github.com/DanNBullock/citeas-on-requirements/issues/3) and [pyproject-toml](https://github.com/DanNBullock/citeas-on-requirements/issues/2))
- Methods for automatedly finding software manifest files (rather than relying on _inputFile_ yml variable input or assumptions)
- Methods for handling and combining outputs from multiple software manifest files in the same repository (e.g. Dockerfile + requirements.txt)
- Boilerplate text to serve as the header for the default ACKNOWLEDGEMENTS.md document output.

#### Citation

[todo]
