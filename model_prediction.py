
import os
import warnings
import tensorflow as tf
import tensorboard as tb
import copy
import numpy as np
import pandas as pd
import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping, LearningRateMonitor
from pytorch_lightning.loggers import TensorBoardLogger
import torch
from pytorch_forecasting import Baseline, TemporalFusionTransformer, TimeSeriesDataSet
from pytorch_forecasting.data import GroupNormalizer
from pytorch_forecasting.metrics import SMAPE, PoissonLoss, QuantileLoss, MAE, MAPE, RMSE
from pytorch_forecasting.models.temporal_fusion_transformer.tuning import optimize_hyperparameters
from pathlib import Path
import pickle
from pytorch_lightning.callbacks import ModelCheckpoint

from model_training import trainer, tft, val_dataloader

best_model_path = trainer.checkpoint_callback.best_model_path
best_tft = TemporalFusionTransformer.load_from_checkpoint(best_model_path)
raw_predictions, x = best_tft.predict(val_dataloader, mode="raw", return_x=True)
