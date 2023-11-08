**Heat Sink Surface Defect Dataset** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the surface defect detection domain. 

The dataset consists of 1000 images with 7118 labeled objects belonging to 2 different classes including *stain area* and *scratch area*.

Images in the Heat Sink Surface Defect dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. The dataset was released in 2022 by the State Key Laboratories of Transducer Technology, Chinese Academy of Sciences.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/heat-sink-surface-defect-dataset/raw/main/visualizations/horizontal_grid.webm)
