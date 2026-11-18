"""tsfm-trl — TRL for time-series foundation models.

One API over every open TSFM: load it, forecast with it, fine-tune it (forecasting
and classification), and post-train it against a reward.

    from tsfm_trl import ModelHub, ForecastTrainer, TrainingConfig
    from tsfm_trl.data import SeriesDataset

    m  = ModelHub.load("timesfm-2.5", device="auto")
    pr = m.predict([context], horizon=21)          # point + 0.1..0.9 quantiles
    cfg = TrainingConfig(ctx=512, horizon=21, budget="fs16")
    ft = ForecastTrainer(m, cfg).fit({"windows": w, "info": info})

Every capability question ("can this model be fine-tuned? does it emit quantiles?")
is answered by the registry + adapters with a *reason*, never a silent skip.
"""
from .errors import CapabilityError, TSFMTRLError, UnknownModelError, UnavailableError
from .model import ModelHub
from .model.base import LEVELS, Pred, TSFMModel
from .training.checkpoints import load_finetuned
from .training.classify import ClassificationTrainer
from .training.config import BUDGETS, TrainResult, TrainingConfig
from .training.forecast import ForecastTrainer
from .training.reward import RewardSpec, RewardTrainer

__version__ = "0.1.0"
__all__ = ["ModelHub", "TSFMModel", "Pred", "LEVELS", "load_finetuned", "TrainingConfig",
           "TrainResult", "BUDGETS", "ForecastTrainer", "ClassificationTrainer", "RewardTrainer",
           "RewardSpec", "TSFMTRLError", "UnknownModelError", "CapabilityError",
           "UnavailableError", "__version__"]
