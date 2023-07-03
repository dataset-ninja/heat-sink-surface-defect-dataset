Please visit dataset [homepage](https://www.kaggle.com/datasets/kaifengyang/heat-sink-surface-defect-dataset) to download the data. 

Afterward, you have the option to download it in the universal supervisely format by utilizing the *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Heat Sink Surface Defect Dataset', dst_path='~/dtools/datasets/Heat Sink Surface Defect Dataset.tar')
```
