Dataset **Heat Sink Surface Defect Dataset** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/M/I/dH/Y56vem270lHlyv3UfxOMWyMY4Yxe0dI7Y1E1mipSj696QO7pDt1v1olOjyQBTqxeJkfADNY12i5NSLmYzwNXgU9wocRCmTLBd0W2z8XTTAK4vALD0cE6wdWzEknQ.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Heat Sink Surface Defect Dataset', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/kaifengyang/heat-sink-surface-defect-dataset/download?datasetVersionNumber=1)