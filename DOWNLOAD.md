Dataset **Heat Sink Surface Defect** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/x2bi7quyczxr2pc7yhye3/heat-sink-surface-defect-DatasetNinja.tar?rlkey=swf2vo7uari7xmvg00wt4lak0&dl=1)

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