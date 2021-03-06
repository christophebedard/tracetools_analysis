# Copyright 2019 Robert Bosch GmbH
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

"""Base data model module."""


class DataModel():
    """
    Container with pre-processed data for an analysis to use.

    Contains data for an analysis to use. This is a middleground between trace events data and the
    output data of an analysis. It uses pandas `DataFrame` directly.
    """

    def __init__(self) -> None:
        pass

    def print_data(self) -> None:
        """Print the data model."""
        raise NotImplementedError
