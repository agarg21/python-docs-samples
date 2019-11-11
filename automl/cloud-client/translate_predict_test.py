#!/usr/bin/env python

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import translate_predict

project_id = os.environ['GCLOUD_PROJECT']


def test_predict(capsys):
    model_id = 'TRL3128559826197068699'
    translate_predict.predict(project_id, model_id, 'resources/input.txt')
    out, _ = capsys.readouterr()
    assert 'Translated content: ' in out
