Dataset **Heat Sink Surface Defect** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/t/R6/CqJTbTpb8CE4RIDfU512eI5tPejLBGrvKU8JFnqBPOL6f9rjkce38JWBQTgNNCR8MnKCNTYGokpt0iBiBSIN6QqoiXKtQFdPHzc7m9VLeO1soVRMTa1ZRpgQyX2Y.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Heat Sink Surface Defect', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/kaifengyang/heat-sink-surface-defect-dataset/download?datasetVersionNumber=1).