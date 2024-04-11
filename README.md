# SEEDAuditor

Welcome to SEEDAuditor, a pivotal component of the SEEDGuard.AI initiative. This project is dedicated to enhancing the security and integrity of data for AI models and corresponding datasets in software engineering. Basically this repository is for Auditing software engineering data.

## Project Overview

SEEDAuditor is an open-source effort under the broader umbrella of SEEDGuard.AI, aimed at revolutionizing AI for Software Engineering with a keen focus on data security. Our mission is to safeguard AI models against data poisoning and backdoor threats, ensuring the development of trustworthy AI systems.

### Key Features

- **Robust Security**: Implementation of robust defenses against poison attacks and backdooring threats to datasets.
- **Scalable Infrastructure**: Development of a scalable system infrastructure to support the growing needs of the AI for SE/Code domain.

### Goals

1. **Enhancing System Fault Tolerance**: Focusing on data security to protect datasets from poison attacks and ensure the integrity of the data.
2. **Optimizing Model Performance**: Implementing retraining protocols to enhance the resilience of SEEDGuard against adversarial attacks.
3. **User-Friendly Functionality**: Ensuring that the project's infrastructure and APIs are aligned with the objectives of SEEDGuard.AI, facilitating easy access and interaction for researchers and developers.


## Getting Started
reference for docker commands :
docker build -t spectralsignature:1.1 .
docker run -it -v test_path --input_dir input_path --output_dir output_path --method method_name


## Paper List

| Year-Id | Title                                                                                                                               | Venue Name | Replication Package                                                  | If Integrated | Current Contributors| 
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------- | ------------- | --------- |
|2023-2 |[MalWuKong: Towards Fast, Accurate, and Multilingual Detection of Malicious Code Poisoning in OSS Supply Chains.](https://doi.org/10.1109/ASE56229.2023.00073)        |ASE    |
|  2023-1       | [Backdooring Neural Code Search](https://arxiv.org/pdf/2305.17506.pdf)                                                                | ACL    | [link](https://github.com/wssun/BADCODE)                                                        |  | [pvinoda](https://github.com/SEEDGuard/SEEDPoisoner/tree/main/core/BadCode)

## Contributing

SEEDAuditor thrives on community contributions. Whether you're interested in enhancing its security features, expanding the API, or improving the current functionality, your contributions are welcome. Please refer to our contribution guideline at [CONTRIBUTING.md](https://github.com/SEEDGuard/SEEDPoisoner/blob/main/CONTRIBUTING.md) for more information on how to contribute. Also refer to our [Docker](https://github.com/SEEDGuard/SEEDUtils/blob/main/template/Dockerfile) template if you are coming up with new Methods for the task.

## Miscallaneous File Links
rb_function.txt {THE INPUT FILE }: https://drive.google.com/file/d/1PZmH6NthgX9hXM5DXynJSMdO9gJ1oWlh/view?usp=drive_link 

Contents to be placed in the output directory before running: https://drive.google.com/drive/folders/1425f_JM0iX7QBUdRf1j-bzOdqpOWpXEj
