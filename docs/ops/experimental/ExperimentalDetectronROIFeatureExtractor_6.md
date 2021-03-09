## ExperimentalDetectronROIFeatureExtractor <a name="ExperimentalDetectronDetectionOutput"></a> {#openvino_docs_ops_experimental_ExperimentalDetectronROIFeatureExtractor_6}

**Versioned name**: *ExperimentalDetectronROIFeatureExtractor-6*

**Category**: Pool

**Short description**: ExperimentalDetectronROIFeatureExtractor is the ROIAlign operation applied over a feature pyramid.

**Detailed description**: ExperimentalDetectronROIFeatureExtractor maps input ROIs to the levels of the pyramid depending on the sizes of ROIs and parameters of the operation, and then extracts features via ROIAlign from corresponding pyramid levels. For more details please see the math formulas below and the following sources:

* [Feature Pyramid Networks for Object Detection](https://arxiv.org/pdf/1612.03144.pdf)
* [Facebook AI / detectron](https://ai.facebook.com/tools/detectron/)
* [ONNX / ROI Align](https://github.com/onnx/onnx/blob/rel-1.5.0/docs/Operators.md#RoiAlign)
* [NNEF / ROI Align](https://www.khronos.org/registry/NNEF/specs/1.0/nnef-1.0.2.html#roi-resize)

**Attributes**:

* *output_size*

    * **Description**: *output_size* attribute specifies the width and height of the output tensor.
    * **Range of values**: a positive integer number
    * **Type**: int
    * **Default value**: None
    * **Required**: *yes*

* *sampling_ratio*

    * **Description**: *sampling_ratio* attribute specifies the number of sampling points per the output value. If 0, then use adaptive number computed as ceil(roi_width / output_width), and likewise for height.
    * **Range of values**: a non-negative integer number
    * **Type**: int
    * **Default value**: 0
    * **Required**: *yes*

* *pyramid_scales*

    * **Description**: *pyramid_scales* enlists `image_size / layer_size[l]` ratios for pyramid layers `l=1,...,L`, where `L` is the number of pyramid layers, and `image_size` refers to network's input image. Note that pyramid's largest layer may have smaller size than input image, e.g. `image_size` is 640 in the XML example below.
    * **Range of values**: a list of positive integer numbers
    * **Type**: int[]
    * **Default value**: None
    * **Required**: *yes*

* *aligned*

    * **Description**: *aligned* attribute specifies add offset to ROI sizes or not.
    * **Range of values**:
      * `true` - add offset to ROI size 
      * `false` - do not add offset to ROI size 
    * **Type**: bool
    * **Default value**: false
    * **Required**: *no*

**Inputs**:

*   **1**: 2D input tensor of type *T* describing the rois as 4-tuples: [x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>]. Batch size is the number of rois. Coordinates *x* and *y* are refer to the input *image_size*. **Required**.

*   **2**, ..., **L**: Pyramid of 4D input blobs with feature maps. Batch size must be 1. The number of channels must be the same for all layers of the pyramid. The layer width and height must equal to the `layer_size[l] = image_size / pyramid_scales[l]`. **Required**.

**Outputs**:

*   **1**: 4D output tensor of type *T*. Batch size equals to number of rois. Channels number is the same as for all images in the input pyramid. Required.

*   **2**: 2D output tensor of type *T* with same shape as 0 input. Required.

**Types**

* *T*: any supported floating point type.


**Mathematical Formulation**

*ExperimentalDetectronROIFeatureExtractor* applies the *ROIAlign* algorithm to the pyramid layers:

* output[i, :, :, :] = ROIAlign(inputPyramid[j], rois[i])
* j = PyramidLevelMapper(rois[i])

PyramidLevelMapper maps the ROI to the pyramid level using the following formula:

* j = floor(2 + log<sub>2</sub>(sqrt(w * h) / 224)

Here 224 is the "canonical" size, 2 is the pyramid starting level, and w, h are the ROI width and height.

**Example**

```xml
<layer ... type="ExperimentalDetectronROIFeatureExtractor">
    <data aligned="false" output_size="7" pyramid_scales="4,8,16,32,64" sampling_ratio="2"/>
    <input>
        <port id="0">
            <dim>1000</dim>
            <dim>4</dim>
        </port>
        <port id="1">
            <dim>1</dim>
            <dim>256</dim>
            <dim>200</dim>
            <dim>336</dim>
        </port>
        <port id="2">
            <dim>1</dim>
            <dim>256</dim>
            <dim>100</dim>
            <dim>168</dim>
        </port>
        <port id="3">
            <dim>1</dim>
            <dim>256</dim>
            <dim>50</dim>
            <dim>84</dim>
        </port>
        <port id="4">
            <dim>1</dim>
            <dim>256</dim>
            <dim>25</dim>
            <dim>42</dim>
        </port>
    </input>
    <output>
        <port id="5" precision="FP32">
            <dim>1000</dim>
            <dim>256</dim>
            <dim>7</dim>
            <dim>7</dim>
        </port>
        <port id="6" precision="FP32">
            <dim>1000</dim>
            <dim>4</dim>
        </port>
    </output>
</layer>
```