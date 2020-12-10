REGEX for fall events in Dutch
==============================
*Jenia Kim*

The repo contains the [vocabularies](vocabularies/) and [code](code/) used for baseline experiments in detecting fall events in clinical notes in Dutch.

The vocabularies were constructed based on (a) a sample of clinical notes describing falls, (b) interviews with nurses at the Amsterdam UMC, and (c) lexical augmentation with synonyms.

Examples of usage can be found in [this notebook](examples/examples.ipynb).

The experiments are described in detail in the [report](report/Detecting_Fall_Incidents_in_Clinical_Notes__Vocabulary_Based_Approach.pdf). The three configurations are:

- **Experiment 1**
    - vocab_v01
    - no pp_rules
- **Experiment 2**
    - vocab_v02
    - no pp_rules
- **Experiment 3**
    - vocab_v02
    - pp_rules_v01

The best results are achieved with the third configuration.

Please note that the results in the report are document-based, while the code in this repo is sentence-based.
