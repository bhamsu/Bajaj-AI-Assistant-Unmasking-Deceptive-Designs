
# Importing all the required modules
import torch
import torchvision
import numpy as np
from PIL import Image
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator
from torchvision.transforms import functional

class FeatureExtractionUsingFasterRCNN:

    def __init__(self, path):

        # self.model = None
        self.path = path
        self.filename = ""
        # Load the pre-trained ResNet-50 model (feature extraction backbone)
        # self.backbone = torchvision.models.resnet50(pretrained = True)
        self.backbone = torchvision.models.resnet50(weights = None)

        # Remove the classification head i.e. the last two layers
        self.backbone = torch.nn.Sequential(*list(self.backbone.children())[:-2])

    def model(self):

        # Define the number of output channels from the backbone
        # For ResNet-50, the final feature map has 2048 channels
        in_channels = 2048  # This is the number of input channels to the RPN and ROI heads
        self.backbone.out_channels = 2048

        # Create an AnchorGenerator
        rpn_anchor_generator = AnchorGenerator(
            sizes = ((32, 64, 128, 256, 512),),
            aspect_ratios = ((0.5, 1.0, 2.0),) * 5
        )

        # Create the ROI (Region of Interest) Align module
        roi_align = torchvision.ops.MultiScaleRoIAlign(
            featmap_names = ['0'], output_size = 7, sampling_ratio = 2
        )

        # Create the Region Proposal Network (RPN) and ROI Heads
        rpn_head = torchvision.models.detection.rpn.RPNHead(
            in_channels = in_channels,
            num_anchors = rpn_anchor_generator.num_anchors_per_location()[0]
        )

        # Specify the required arguments for RoIHeads
        roi_head = torchvision.models.detection.roi_heads.RoIHeads(
            box_roi_pool = roi_align,
            box_head = None,  # Replace with the box head you want to use
            box_predictor = None,  # Replace with the box predictor you want to use
            fg_iou_thresh = 0.5,  # Set the foreground IoU threshold
            bg_iou_thresh = 0.5,  # Set the background IoU threshold
            batch_size_per_image = 512,  # Set the batch size per image
            positive_fraction = 0.25,  # Set the positive fraction
            bbox_reg_weights = None,  # Replace with the desired weights for bounding box regression
            score_thresh = 0.05,  # Set the score threshold for object detection
            nms_thresh = 0.5,  # Set the NMS threshold
            detections_per_img = 100  # Set the maximum number of detections per image
        )

        # Create the Faster R-CNN model
        self.model = FasterRCNN(
            self.backbone,
            num_classes = 3,  # Replace with the number of classes in your dataset
            rpn_anchor_generator = rpn_anchor_generator,
            rpn_head = rpn_head,
            roi_heads = roi_head
        )

        # Set the model to evaluation mode
        self.model.eval()


    def extract(self, filename):

        # Load an image
        image = Image.open(self.path + filename).convert('RGB')
        self.filename = filename

        # Preprocess the image
        image_tensor = functional.to_tensor(image)
        image_tensor = functional.normalize(image_tensor, mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])  # Normalize
        image_tensor = image_tensor.unsqueeze(0)  # Batch dimension

        # Use the feature extraction backbone
        # 'features' contains the feature maps extracted from the image
        with torch.no_grad():
            features = self.model.backbone(image_tensor)

        return features


    def saveFeatures(self, features):

        # Convert the features tensor to a NumPy array
        features_np = features.cpu().numpy()

        # Save the NumPy array to a file
        np.save(self.path + 'FasterRCNN_features_' + self.filename[0:-4] + '.npy', features_np)
        print("Faster R-CNN Features successfully extracted, and stored at " + self.path + 'FasterRCNN_features_' + self.filename[0:-4] + '.npy' + "...")

    def __call__(self, *args, **kwargs):
        self.model()
        feature = self.extract(kwargs['filename'])
        print("Feature extracted from image using Faster R-CNN...")
        # self.saveFeatures(feature)
        return feature

    def __del__(self):
        pass