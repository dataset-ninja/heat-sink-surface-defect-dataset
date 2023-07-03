import os

import cv2
import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/almaz/Downloads/Heat_Sink_Surface_Defect_Dataset/jsons"
    batch_size = 30

    def create_ann(mask_path):
        labels = []

        mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
        img_height = mask_np.shape[0]
        img_wight = mask_np.shape[1]

        mask_np = cv2.imread(mask_path)
        mask_np = cv2.cvtColor(mask_np, cv2.COLOR_BGR2RGB)
        mask_np = np.reshape(mask_np, (-1, 3))
        unique_colors = np.unique(mask_np, axis=0)

        for color in unique_colors:
            color = list(color)
            if str(color) in color2class:
                obj_class = color2class[str(color)]
                mask_np = cv2.imread(mask_path)
                mask_np = cv2.cvtColor(mask_np, cv2.COLOR_BGR2RGB)
                mask_np = np.all(mask_np == np.array(color), axis=2).astype(np.uint8)
                num_labels, labels_im = connectedComponents(mask_np)
                for i in range(1, num_labels):
                    bmap = labels_im == i
                    label = sly.Label(obj_class=obj_class, geometry=sly.Bitmap(bmap))
                    labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    scratch_obj_class = sly.ObjClass("scratch area", sly.Bitmap)
    stain_obj_class = sly.ObjClass("stain area", sly.Bitmap)

    color2class = {
        "[128, 0, 0]": scratch_obj_class,
        "[0, 128, 0]": stain_obj_class,
    }

    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta(obj_classes=[scratch_obj_class, stain_obj_class])
    api.project.update_meta(project.id, meta.to_json())

    ds_name = "ds0"
    dataset = api.dataset.create(project.id, ds_name)

    all_items = [
        item for item in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, item))
    ]

    progress = tqdm(desc=f"Create dataset {ds_name}", total=len(all_items))

    for items in sly.batched(all_items, batch_size=batch_size):
        item_paths = [os.path.join(dataset_path, item) for item in items]
        imgs_paths = [os.path.join(item_path, "img.png") for item_path in item_paths]
        anns_paths = [os.path.join(item_path, "label.png") for item_path in item_paths]

        imgs_names = [f'{item.split("_")[0]}.png' for item in items]

        img_infos = api.image.upload_paths(dataset.id, imgs_names, imgs_paths)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(mask_path) for mask_path in anns_paths]
        api.annotation.upload_anns(img_ids, anns)

        progress.update(len(items))

    return project
