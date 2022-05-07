# Version 2 of the starting kit for the ICPR2022-ODOR-Competition



## How to use the simple baseline model

0. Install any IDE capable of working with jupyter notebooks, e.g. Jupyter Notebook from https://jupyter.org
1. Install icevision according to the instructions provided at https://airctic.com.
2. Run the `download_imgs.py` script to download the images for the training set.
3. Train the model using the `train_baseline.ipynb` notebook. Feel free to adapt hyperparameters and modify the training procedure to improve the results.
4. Generate predictions using the `predict_baseline.ipynb` script.


## How to submit your results
0. Download the testset images using the `download_testimgs.py` script.
1. Generate predictions on the testset by running the `predict_baseline.ipynb` notebook.
2. Create a zip containing your results file only (`baseline_predictions.json` by default) and upload the zip to codalab.

