# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The Prescience-Client Authors. All rights reserved.

import os
from com.ovh.mls.prescience.core.enum.input_type import InputType
from com.ovh.mls.prescience.core.enum.problem_type import ProblemType
from com.ovh.mls.prescience.core.enum.scoring_metric import ScoringMetric

DEFAULT_PRESCIENCE_API_URL = 'https://prescience-api.ai.ovh.net'
DEFAULT_WEBSOCKET_URL = 'wss://prescience-websocket.ai.ovh.net'

DEFAULT_LABEL_NAME = 'label'
DEFAULT_PROBLEM_TYPE = ProblemType.CLASSIFICATION
DEFAULT_INPUT_TYPE = InputType.CSV
DEFAULT_SCORING_METRIC = ScoringMetric.ACCURACY

DEFAULT_PRESCIENCE_CONFIG_PATH = f'{os.environ["HOME"]}/.prescience'
DEFAULT_PRESCIENCE_CONFIG_FILE = 'config.yaml'


EXCEPTION_HANDLING_RAISE = 'raise'
EXCEPTION_HANDLING_PRINT = 'print'
DEFAULT_EXCEPTION_HANDLING = EXCEPTION_HANDLING_PRINT